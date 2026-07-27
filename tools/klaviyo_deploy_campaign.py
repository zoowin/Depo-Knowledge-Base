#!/usr/bin/env python3
"""One-step: create template + create campaign + assign. Zero tokens consumed."""
import sys, io, json, argparse, requests
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_api_key():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    for line in env_path.read_text().splitlines():
        if line.startswith('KLAVIYO_API_KEY='):
            return line.split('=', 1)[1]
    raise ValueError('.env missing KLAVIYO_API_KEY')

API_KEY = load_api_key()
HEADERS = {
    'Authorization': f'Klaviyo-API-Key {API_KEY}',
    'Content-Type': 'application/json',
    'revision': '2024-10-15',
    'Accept': 'application/json',
}
BASE = 'https://a.klaviyo.com/api'


def create_template(name, html):
    r = requests.post(f'{BASE}/templates/', headers=HEADERS, json={
        'data': {'type': 'template', 'attributes': {'name': name, 'html': html, 'editor_type': 'CODE'}}
    })
    r.raise_for_status()
    tid = r.json()['data']['id']
    print(f'[1/3] Template created: {tid}')
    return tid


def update_template(template_id, html):
    """PATCH existing template HTML (reuse after content tweaks — avoids template clutter)."""
    r = requests.patch(
        f'{BASE}/templates/{template_id}/',
        headers=HEADERS,
        json={'data': {'type': 'template', 'id': template_id,
                       'attributes': {'html': html}}}
    )
    r.raise_for_status()
    print(f'Template updated: {template_id}')


# Standard audiences per CLAUDE.md (4 included + 9 excluded)
STD_INCLUDED = ['QPetUg', 'X9GvQv', 'XQqrAQ', 'YbRy3S']
STD_EXCLUDED = ['RNUDwR', 'RsM7QF', 'TCpjZJ', 'TWCwGW', 'U9crDJ',
                'UzTR6W', 'VFjbHB', 'XVbFC5', 'XWFhWE']


def create_campaign(name, subject, preview_text, list_id=None, included_ids=None,
                    excluded_ids=None, send_time=None,
                    from_email='support@depology.com', from_label='Dēpology'):
    send_strategy = {'method': 'immediate'} if not send_time else {
        'method': 'static',
        'options_static': {'datetime': send_time, 'is_local': False}
    }
    if included_ids:
        included = included_ids
    elif list_id:
        included = [list_id]
    else:
        included = STD_INCLUDED

    if excluded_ids is not None:
        excluded = excluded_ids
    elif included_ids or list_id:
        excluded = STD_EXCLUDED
    else:
        excluded = STD_EXCLUDED
    payload = {
        'data': {
            'type': 'campaign',
            'attributes': {
                'name': name,
                'audiences': {'included': included, 'excluded': excluded},
                'send_strategy': send_strategy,
                'send_options': {'use_smart_sending': True},
                'tracking_options': {'is_tracking_clicks': True, 'is_tracking_opens': True},
                'campaign-messages': {
                    'data': [{
                        'type': 'campaign-message',
                        'attributes': {
                            'channel': 'email',
                            'label': name,
                            'content': {
                                'subject': subject,
                                'preview_text': preview_text,
                                'from_email': from_email,
                                'from_label': from_label,
                            }
                        }
                    }]
                }
            }
        }
    }
    r = requests.post(f'{BASE}/campaigns/', headers=HEADERS, json=payload)
    r.raise_for_status()
    data = r.json()['data']
    cid = data['id']
    mid = data['relationships']['campaign-messages']['data'][0]['id']
    print(f'[2/3] Campaign created: {cid}')
    return cid, mid


def assign_template(message_id, template_id):
    r = requests.post(
        f'{BASE}/campaign-message-assign-template/',
        headers=HEADERS,
        json={
            'data': {
                'type': 'campaign-message',
                'id': message_id,
                'relationships': {
                    'template': {'data': {'type': 'template', 'id': template_id}}
                }
            }
        }
    )
    r.raise_for_status()
    print(f'[3/3] Template assigned to message {message_id}')


def main():
    p = argparse.ArgumentParser(description='Deploy Klaviyo campaign from local HTML')
    p.add_argument('html_file', help='Path to campaign HTML')
    p.add_argument('--name', required=True, help='Campaign name')
    p.add_argument('--subject', required=True, help='Email subject line')
    p.add_argument('--preview', required=True, help='Preview text')
    p.add_argument('--list-id', default=None,
                   help='Single audience list ID override. Uses standard excluded segments unless --excluded-ids is set.')
    p.add_argument('--included-ids', default=None,
                   help='Comma-separated included list/segment IDs. Overrides --list-id.')
    p.add_argument('--excluded-ids', default=None,
                   help='Comma-separated excluded list/segment IDs. Use empty string for no exclusions. Default: standard excluded segments.')
    p.add_argument('--send-time', help='ISO send time, e.g. 2026-04-05T10:00:00.000Z')
    args = p.parse_args()

    html = Path(args.html_file).read_text(encoding='utf-8')
    print(f'HTML loaded: {len(html)} chars')

    tid = create_template(f'{args.name}_template', html)
    included_ids = [x.strip() for x in args.included_ids.split(',') if x.strip()] if args.included_ids else None
    excluded_ids = None
    if args.excluded_ids is not None:
        excluded_ids = [x.strip() for x in args.excluded_ids.split(',') if x.strip()]

    cid, mid = create_campaign(
        args.name,
        args.subject,
        args.preview,
        list_id=args.list_id,
        included_ids=included_ids,
        excluded_ids=excluded_ids,
        send_time=args.send_time,
    )
    assign_template(mid, tid)

    print(f'\nDone!')
    print(f'  Campaign: https://www.klaviyo.com/campaign/{cid}/wizard')
    print(f'  Template: https://www.klaviyo.com/email-editor/{tid}/edit')


if __name__ == '__main__':
    main()
