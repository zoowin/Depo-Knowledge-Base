#!/usr/bin/env python3
"""Build campaign HTML from base template + replacements JSON. Zero tokens."""
import sys, io, json, argparse
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / 'production' / 'html-output'

def main():
    p = argparse.ArgumentParser(description='Build campaign HTML from base template + replacements')
    p.add_argument('replacements_json', help='JSON file with replacements array: [{"old": "...", "new": "..."}, ...]')
    p.add_argument('--base', default='R5x7wg', help='Base template name (R5x7wg or VE92sd)')
    p.add_argument('--output', required=True, help='Output HTML filename (saved to production/html-output/)')
    p.add_argument('--preview', action='store_true', help='Open in browser after build')
    args = p.parse_args()

    # Load base template
    base_file = TEMPLATES_DIR / f'{args.base}_base_template.html'
    if not base_file.exists():
        print(f'Error: base template not found: {base_file}')
        sys.exit(1)
    html = base_file.read_text(encoding='utf-8')
    print(f'Base template loaded: {args.base} ({len(html)} chars)')

    # Load replacements
    replacements = json.loads(Path(args.replacements_json).read_text(encoding='utf-8'))

    ok, miss = 0, 0
    for r in replacements:
        old, new = r['old'], r['new']
        if old in html:
            html = html.replace(old, new)
            ok += 1
        else:
            print(f'  MISS: {old[:60]}...')
            miss += 1
    print(f'Replacements: {ok} OK, {miss} MISS')

    # Save output
    out_path = TEMPLATES_DIR / args.output
    out_path.write_text(html, encoding='utf-8')
    print(f'Output: {out_path} ({len(html)} chars)')

    if args.preview:
        import webbrowser
        webbrowser.open(str(out_path))
        print('Opened in browser for preview.')

if __name__ == '__main__':
    main()
