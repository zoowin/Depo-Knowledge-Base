#!/usr/bin/env python3
"""Create a Klaviyo email template from local HTML and optionally assign to a campaign message."""
import sys, json, argparse, os, requests
from pathlib import Path

def load_api_key():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    with open(env_path, 'r') as f:
        for line in f:
            if line.startswith('KLAVIYO_API_KEY='):
                return line.strip().split('=', 1)[1]
    raise ValueError('.env missing KLAVIYO_API_KEY')

API_KEY = load_api_key()
HEADERS = {
    'Authorization': f'Klaviyo-API-Key {API_KEY}',
    'Content-Type': 'application/json',
    'revision': '2024-10-15',
    'Accept': 'application/json',
}
BASE = 'https://a.klaviyo.com/api'

def create_template(name: str, html: str) -> str:
    """Create template, return template ID."""
    payload = {
        'data': {
            'type': 'template',
            'attributes': {
                'name': name,
                'html': html,
                'editor_type': 'CODE',
            }
        }
    }
    r = requests.post(f'{BASE}/templates/', headers=HEADERS, json=payload)
    r.raise_for_status()
    tid = r.json()['data']['id']
    print(f'Template created: {tid}')
    print(f'  Edit: https://www.klaviyo.com/email-editor/{tid}/edit')
    return tid

def assign_template(campaign_message_id: str, template_id: str):
    """Assign template to campaign message."""
    payload = {
        'data': {
            'type': 'campaign-message',
            'id': campaign_message_id,
            'relationships': {
                'template': {
                    'data': {
                        'type': 'template',
                        'id': template_id,
                    }
                }
            }
        }
    }
    r = requests.patch(
        f'{BASE}/campaign-messages/{campaign_message_id}',
        headers=HEADERS,
        json=payload,
    )
    r.raise_for_status()
    print(f'Template {template_id} assigned to message {campaign_message_id}')

def main():
    p = argparse.ArgumentParser(description='Create Klaviyo template from HTML file')
    p.add_argument('html_file', help='Path to HTML file')
    p.add_argument('--name', required=True, help='Template name')
    p.add_argument('--assign-to', help='Campaign message ID to assign template to')
    args = p.parse_args()

    html = Path(args.html_file).read_text(encoding='utf-8')
    print(f'HTML loaded: {len(html)} chars')

    tid = create_template(args.name, html)

    if args.assign_to:
        assign_template(args.assign_to, tid)

    print('Done.')

if __name__ == '__main__':
    main()
