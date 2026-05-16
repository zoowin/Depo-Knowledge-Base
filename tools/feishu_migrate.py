#!/usr/bin/env python3
"""
Feishu Bitable Data Migration Tool
Migrates local Markdown data to Feishu EDM OS tables.

Usage:
  python3 tools/feishu_migrate.py --action migrate-topics
  python3 tools/feishu_migrate.py --action migrate-promotions
  python3 tools/feishu_migrate.py --action migrate-campaigns
  python3 tools/feishu_migrate.py --action check-pending

Setup: Add to .env file:
  FEISHU_APP_ID=cli_xxxxxxxxxx
  FEISHU_APP_SECRET=xxxxxxxxxxxxxxxx
  FEISHU_APP_TOKEN=xxxxxxxxxxxxxx        # from bitable URL /base/XXXX
  FEISHU_TABLE_CALENDAR=tblXXXXXX       # Campaign Calendar table_id
  FEISHU_TABLE_DRAFTS=tblXXXXXX         # Draft Workshop table_id
  FEISHU_TABLE_PERFORMANCE=tblXXXXXX    # Performance Dashboard table_id
  FEISHU_TABLE_TOPICS=tblXXXXXX         # Topic Pool table_id
  FEISHU_TABLE_PROMOTIONS=tblXXXXXX     # Promotion Calendar table_id
  FEISHU_CHAT_EMAIL=oc_3a7115c5c5b70ed83ed3435765b4492d
"""

import sys, json, argparse, requests
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


def load_config():
    """Load credentials from .env file."""
    env_path = BASE_DIR / '.env'
    if not env_path.exists():
        raise FileNotFoundError('.env file not found. See script header for setup instructions.')
    config = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, _, val = line.partition('=')
            config[key.strip()] = val.strip()
    required = ['FEISHU_APP_ID', 'FEISHU_APP_SECRET', 'FEISHU_APP_TOKEN']
    for k in required:
        if k not in config:
            raise ValueError(f'.env missing {k}')
    return config


def get_tenant_access_token(app_id, app_secret):
    """Get Feishu tenant access token."""
    r = requests.post(
        'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
        json={'app_id': app_id, 'app_secret': app_secret}
    )
    r.raise_for_status()
    data = r.json()
    if data.get('code') != 0:
        raise ValueError(f'Feishu auth failed: {data}')
    return data['tenant_access_token']


def feishu_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }


def create_record(token, app_token, table_id, fields):
    """Create a single record in a Feishu bitable table."""
    r = requests.post(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records',
        headers=feishu_headers(token),
        json={'fields': fields}
    )
    r.raise_for_status()
    data = r.json()
    if data.get('code') != 0:
        raise ValueError(f'Create record failed: {data}')
    return data['data']['record']['record_id']


def get_records(token, app_token, table_id, filter_str=None, page_size=100):
    """Get all records from a Feishu bitable table."""
    params = {'page_size': page_size}
    if filter_str:
        params['filter'] = filter_str
    r = requests.get(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records',
        headers=feishu_headers(token),
        params=params
    )
    r.raise_for_status()
    data = r.json()
    if data.get('code') != 0:
        raise ValueError(f'Get records failed: {data}')
    return data['data']['items']


def update_record(token, app_token, table_id, record_id, fields):
    """Update a record in a Feishu bitable table."""
    r = requests.put(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}',
        headers=feishu_headers(token),
        json={'fields': fields}
    )
    r.raise_for_status()
    data = r.json()
    if data.get('code') != 0:
        raise ValueError(f'Update record failed: {data}')
    return data


def send_chat_message(token, chat_id, text):
    """Send a message to a Feishu group chat."""
    r = requests.post(
        'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id',
        headers=feishu_headers(token),
        json={
            'receive_id': chat_id,
            'msg_type': 'text',
            'content': json.dumps({'text': text})
        }
    )
    r.raise_for_status()
    return r.json()


# ─── Migration Functions ──────────────────────────────────────────────────────

TOPIC_CATEGORIES = {
    'Educational': ['Winter Skin Science', 'Ingredient Deep Dive', 'Mechanism of Action',
                    'Routine Building', 'Myth Busting', 'Ingredient Pairing', 'Problem & Solution'],
    'Social Proof': ['Customer Spotlight', 'Expert Validation', 'UGC Compilation',
                     'Before & After', 'Press Mention'],
    'Promo': ['Archive Sale', 'Warehouse Clearance', 'Bundle Offer', 'Seasonal Sale',
              'Flash Sale', 'Gift with Purchase'],
    'Lifestyle': ['Spring cleaning your skincare cabinet', 'Self-Care Sunday',
                  'Holiday Gifting', 'Travel Skincare'],
    'Testing': ['The "Notox" Movement', 'Skin Streaming', '"Overnight Wrapping" / Slugging 2.0',
                'Salmon Sperm (PDRN) vs. Peptides', 'Retinol vs Retinal', 'Skin Cycling Routine',
                'Sandwich Method Retinol', 'Copper Peptides', 'Barrier Repair'],
}

TOPIC_PRIORITIES = {
    'Archive Sale': 5, 'The "Notox" Movement': 5, 'Customer Spotlight': 4,
    'Barrier Repair': 4, 'Ingredient Deep Dive': 4, 'Skin Cycling Routine': 4,
}


def migrate_topics(token, cfg):
    """Migrate topic-pool.md data to Feishu Topic Pool table."""
    table_id = cfg.get('FEISHU_TABLE_TOPICS')
    if not table_id:
        print('ERROR: FEISHU_TABLE_TOPICS not set in .env')
        return

    count = 0
    for category, topics in TOPIC_CATEGORIES.items():
        for topic in topics:
            fields = {
                'Topic': topic,
                'Category': category,
                'Priority': TOPIC_PRIORITIES.get(topic, 3),
                'Status': 'Available',
                'Source': 'Manual',
            }
            try:
                create_record(token, cfg['FEISHU_APP_TOKEN'], table_id, fields)
                count += 1
                print(f'  ✓ [{category}] {topic}')
            except Exception as e:
                print(f'  ✗ [{category}] {topic}: {e}')

    print(f'\n✅ Topic Pool migration complete: {count} topics added')


PROMOTIONS = [
    {'Event Name': 'Archive Sale', 'Start Date': '2026-02-02', 'End Date': '2026-02-09',
     'Level': 'Middle', 'Discount Code': 'VIP20', 'Discount Type': 'VIP Extra 20% OFF',
     'Status': 'Completed', 'Email Count': 9},
    {'Event Name': "Valentine's Day Sale", 'Start Date': '2026-02-14', 'End Date': '2026-02-14',
     'Level': 'Small', 'Discount Code': '', 'Discount Type': '15% OFF',
     'Status': 'Completed', 'Email Count': 1},
    {"Event Name": "Women's Day Sale", 'Start Date': '2026-03-08', 'End Date': '2026-03-08',
     'Level': 'Small', 'Discount Code': '', 'Discount Type': '15% OFF',
     'Status': 'Completed', 'Email Count': 1},
    {'Event Name': 'Easter Weekend Sale', 'Start Date': '2026-04-05', 'End Date': '2026-04-06',
     'Level': 'Small', 'Discount Code': 'EASTER20', 'Discount Type': '20% OFF',
     'Status': 'Completed', 'Email Count': 2},
    {"Event Name": "Mother's Day Sale", 'Start Date': '2026-05-11', 'End Date': '2026-05-11',
     'Level': 'Small', 'Discount Code': '', 'Discount Type': '15-20% OFF',
     'Status': 'Active', 'Email Count': 1},
    {'Event Name': 'Memorial Day Sale', 'Start Date': '2026-05-20', 'End Date': '2026-05-25',
     'Level': 'Middle', 'Discount Code': 'MEM10',
     'Discount Type': 'UP TO 60% + Extra 10% MEM10 (48hrs)',
     'Status': 'Active', 'Email Count': 8},
    {'Event Name': 'July 4th Sale', 'Start Date': '2026-07-01', 'End Date': '2026-07-08',
     'Level': 'Middle', 'Discount Code': '', 'Discount Type': '20-25% OFF',
     'Status': 'Planning', 'Email Count': 6},
    {'Event Name': 'Labor Day Sale', 'Start Date': '2026-09-01', 'End Date': '2026-09-07',
     'Level': 'Middle', 'Discount Code': '', 'Discount Type': '20-25% OFF',
     'Status': 'Planning', 'Email Count': 6},
    {'Event Name': 'Halloween Sale', 'Start Date': '2026-10-31', 'End Date': '2026-10-31',
     'Level': 'Small', 'Discount Code': '', 'Discount Type': '15-20% OFF',
     'Status': 'Planning', 'Email Count': 2},
    {'Event Name': 'BFCM', 'Start Date': '2026-11-17', 'End Date': '2026-12-07',
     'Level': 'Big', 'Discount Code': '', 'Discount Type': 'Tiered discount + VIP exclusive',
     'Status': 'Planning', 'Email Count': 20},
    {'Event Name': 'Winter Clearance', 'Start Date': '2026-12-26', 'End Date': '2027-01-12',
     'Level': 'Big', 'Discount Code': '', 'Discount Type': 'Tiered discount',
     'Status': 'Planning', 'Email Count': 10},
]


def migrate_promotions(token, cfg):
    """Migrate promotion-calendar.md data to Feishu Promotion Calendar table."""
    table_id = cfg.get('FEISHU_TABLE_PROMOTIONS')
    if not table_id:
        print('ERROR: FEISHU_TABLE_PROMOTIONS not set in .env')
        return

    count = 0
    for promo in PROMOTIONS:
        fields = {
            'Event Name': promo['Event Name'],
            'Level': promo['Level'],
            'Discount Code': promo.get('Discount Code', ''),
            'Discount Type': promo.get('Discount Type', ''),
            'Status': promo['Status'],
            'Email Count': promo.get('Email Count', 0),
        }
        try:
            create_record(token, cfg['FEISHU_APP_TOKEN'], table_id, fields)
            count += 1
            print(f'  ✓ {promo["Event Name"]} ({promo["Level"]})')
        except Exception as e:
            print(f'  ✗ {promo["Event Name"]}: {e}')

    print(f'\n✅ Promotion Calendar migration complete: {count} events added')


MARCH_CAMPAIGNS = [
    {'Campaign Name': 'Spring Renewal', 'Month': '2026-03', 'Email Type': 'Lifestyle',
     'Send Date': '2026-03-02', 'Subject Line': 'The secret to smooth skin (Head to Toe).',
     'Status': '📊 Live', 'Product Line': 'C'},
    {'Campaign Name': 'The "Notox" Movement', 'Month': '2026-03', 'Email Type': 'Education',
     'Send Date': '2026-03-04',
     'Subject Line': 'The "Notox" Movement: Smooth skin, no appointments.',
     'Status': '📊 Live', 'Product Line': 'B'},
    {'Campaign Name': 'Real Results: 4-Week', 'Month': '2026-03', 'Email Type': 'Social Proof',
     'Send Date': '2026-03-06', 'Subject Line': 'See the difference 28 days makes',
     'Status': '📊 Live', 'Product Line': 'B'},
    {"Campaign Name": "Women's Day Sale", 'Month': '2026-03', 'Email Type': 'Promo',
     'Send Date': '2026-03-08', 'Subject Line': 'Transform Your Routine Today!',
     'Status': '📊 Live', 'Product Line': 'A', 'Discount Code': '15% OFF'},
    {'Campaign Name': '500 Dalton Rule', 'Month': '2026-03', 'Email Type': 'Education',
     'Send Date': '2026-03-10', 'Subject Line': 'Is Your Collagen Cream Underperforming?',
     'Status': '📊 Live', 'Product Line': 'A'},
    {'Campaign Name': 'Trend vs. Science', 'Month': '2026-03', 'Email Type': 'Trend',
     'Send Date': '2026-03-13', 'Subject Line': 'Is "Rice Water" worth the hype? 🍚',
     'Status': '📊 Live', 'Product Line': 'A'},
    {'Campaign Name': 'Sunday Reset (Eyes)', 'Month': '2026-03', 'Email Type': 'Lifestyle',
     'Send Date': '2026-03-15',
     'Subject Line': 'Look like you slept 8 hours (even if you didn\'t) 😴',
     'Status': '📊 Live', 'Product Line': 'B'},
    {'Campaign Name': 'Deep Dive: Retinol', 'Month': '2026-03', 'Email Type': 'Education',
     'Send Date': '2026-03-16', 'Subject Line': 'Deep Dive: Retinol for mature skin',
     'Status': '📊 Live', 'Product Line': 'C'},
]


def migrate_campaigns(token, cfg):
    """Migrate historical campaign data to Feishu Campaign Calendar table."""
    table_id = cfg.get('FEISHU_TABLE_CALENDAR')
    if not table_id:
        print('ERROR: FEISHU_TABLE_CALENDAR not set in .env')
        return

    count = 0
    for camp in MARCH_CAMPAIGNS:
        fields = {
            'Campaign Name': camp['Campaign Name'],
            'Month': camp['Month'],
            'Email Type': camp['Email Type'],
            'Status': camp['Status'],
            'Subject Line': camp.get('Subject Line', ''),
            'Product Line': [camp['Product Line']] if 'Product Line' in camp else [],
            'Discount Code': camp.get('Discount Code', ''),
        }
        try:
            create_record(token, cfg['FEISHU_APP_TOKEN'], table_id, fields)
            count += 1
            print(f'  ✓ {camp["Campaign Name"]} ({camp["Send Date"]})')
        except Exception as e:
            print(f'  ✗ {camp["Campaign Name"]}: {e}')

    print(f'\n✅ Campaign Calendar migration complete: {count} campaigns added')


def check_pending(token, cfg):
    """Check Draft Workshop for records with Status = Requested."""
    table_id = cfg.get('FEISHU_TABLE_DRAFTS')
    if not table_id:
        print('ERROR: FEISHU_TABLE_DRAFTS not set in .env')
        return []

    print('Checking Draft Workshop for pending tasks...')
    records = get_records(token, cfg['FEISHU_APP_TOKEN'], table_id)
    pending = [r for r in records
               if r.get('fields', {}).get('Draft Status') == 'Requested']

    if not pending:
        print('No pending drafts found.')
        return []

    print(f'\nFound {len(pending)} pending draft(s):')
    for r in pending:
        f = r['fields']
        print(f'  • {f.get("Draft Title", "Untitled")} — Campaign: {f.get("Campaign", "?")}')

    return pending


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Feishu EDM OS Migration Tool')
    parser.add_argument('--action', required=True,
                        choices=['migrate-topics', 'migrate-promotions',
                                 'migrate-campaigns', 'check-pending', 'all'],
                        help='Action to perform')
    args = parser.parse_args()

    cfg = load_config()
    print('Authenticating with Feishu...')
    token = get_tenant_access_token(cfg['FEISHU_APP_ID'], cfg['FEISHU_APP_SECRET'])
    print('✓ Authenticated\n')

    if args.action == 'migrate-topics' or args.action == 'all':
        print('=== Migrating Topic Pool ===')
        migrate_topics(token, cfg)

    if args.action == 'migrate-promotions' or args.action == 'all':
        print('\n=== Migrating Promotion Calendar ===')
        migrate_promotions(token, cfg)

    if args.action == 'migrate-campaigns' or args.action == 'all':
        print('\n=== Migrating Campaign History ===')
        migrate_campaigns(token, cfg)

    if args.action == 'check-pending':
        check_pending(token, cfg)


if __name__ == '__main__':
    main()
