import re
import os
import sys
import glob

print("Script started...")

# --- Theme Configuration (The "Rules") ---
THEME_CONFIG = {
    "colors": {
        "primary": "#000000",       # Main text/buttons
        "secondary": "#666666",     # Subtext
        "accent": "#4CAF50",        # Highlights (green)
        "background": "#f4f4f4",    # Email background
        "container": "#ffffff",     # Content background
        "hero_bg": "#e6f0e6",       # Hero section background
        "product_bg": "#f9f9f9"     # Product/Goals background
    },
    "fonts": {
        "main": "Arial, sans-serif"
    },
    "layout": {
        "width": "600px",
        "padding": "20px"
    }
}

# --- Product URL Configuration (The "Links") ---
PRODUCT_URLS = {
    # Exact name match from Markdown -> URL
    "Opuntia-C Relief Cleansing Balm": "https://depology.com/products/opuntia-c-relief-cleansing-balm",
    "Argireline™ MPS Solution": "https://depology.com/products/peptide-complex-10-argireline-peptide-serum",
    "Cica Redness Relief Serum": "https://depology.com/products/cica-h-a-calm-repair-serum",
    
    # General CTAs
    "REFRESH YOUR ROUTINE": "https://depology.com/collections/shop-all",
    "SHOP SPRING ESSENTIALS": "https://depology.com/collections/shop-all",
    "SHOP ALL": "https://depology.com/collections/shop-all"
}

def get_css():
    c = THEME_CONFIG["colors"]
    f = THEME_CONFIG["fonts"]
    l = THEME_CONFIG["layout"]
    
    return f"""
    <style>
        body {{ margin: 0; padding: 0; font-family: {f['main']}; background-color: {c['background']}; }}
        .container {{ max-width: {l['width']}; margin: 0 auto; background-color: {c['container']}; }}
        .header {{ text-align: center; padding: {l['padding']}; background-color: {c['container']}; }}
        .hero {{ background-color: {c['hero_bg']}; padding: 40px {l['padding']}; text-align: center; }}
        .hero h1 {{ color: #333; margin-bottom: 10px; }}
        .hero p {{ font-size: 18px; color: {c['secondary']}; margin-bottom: 20px; }}
        .btn {{ display: inline-block; background-color: {c['primary']}; color: #fff; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 4px; }}
        .content {{ padding: 40px {l['padding']}; color: #333; line-height: 1.6; }}
        .content h2 {{ color: {c['primary']}; text-align: center; }}
        .goals {{ background-color: {c['product_bg']}; padding: {l['padding']}; margin-top: 20px; border-left: 4px solid {c['accent']}; }}
        .product-section {{ padding: 40px {l['padding']}; background-color: #fff; }}
        .product {{ margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 20px; }}
        .product h3 {{ color: #333; }}
        .product ul {{ padding-left: 20px; color: #555; }}
        .footer {{ background-color: #333; color: #fff; text-align: center; padding: {l['padding']}; font-size: 12px; }}
    </style>
    """

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'subject': '',
        'preview': '',
        'hero': {},
        'body': {},
        'products': [],
        'footer_cta': {},
        'date_code': ''
    }

    # Extract Date Code from filename
    filename = os.path.basename(file_path)
    date_match = re.match(r'(\d{8})', filename)
    if date_match:
        data['date_code'] = date_match.group(1)

    # Extract Subject and Preview
    subject_match = re.search(r'\*\*Subject Line Options\*\*.*?\d\.\s+(.*?)\n', content, re.DOTALL)
    if subject_match:
        data['subject'] = subject_match.group(1).strip()
    
    preview_match = re.search(r'\*\*Preview Text\*\*\s+(.*?)\n', content, re.DOTALL)
    if preview_match:
        data['preview'] = preview_match.group(1).strip()

    # Split by sections
    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)
    
    for section in sections:
        if 'Hero Section' in section:
            data['hero']['headline'] = extract_value(section, 'Headline')
            data['hero']['subheadline'] = extract_value(section, 'Sub-headline')
            data['hero']['cta'] = extract_value(section, 'CTA Button')
            
        elif 'Body Section' in section:
            data['body']['headline'] = extract_value(section, 'Headline')
            # Copy might be multi-line, so we capture until the next ** or end of section
            copy_match = re.search(r'\*\*Copy:\*\*\s+(.*?)(?=\n\*\*|\n---|$)', section, re.DOTALL)
            if copy_match:
                data['body']['copy'] = copy_match.group(1).strip().replace('\n', '<br>')
            
            goals_match = re.search(r'\*\*Spring Skin Goals:\*\*(.*?)(?=\n---|$)', section, re.DOTALL)
            if goals_match:
                goals_text = goals_match.group(1).strip()
                goals_list = [line.strip('* ').strip() for line in goals_text.split('\n') if line.strip().startswith('*')]
                data['body']['goals'] = goals_list

        elif 'Product Section' in section:
            data['products_headline'] = extract_value(section, 'Headline')
            
            # Find all products
            prod_matches = re.finditer(r'\*\*\d\.\s+(.*?)\*\*(.*?)(?=\*\*\d\.|\*\*CTA|$)', section, re.DOTALL)
            for match in prod_matches:
                prod_name_raw = match.group(1)
                prod_desc_raw = match.group(2)
                
                name = prod_name_raw.strip()
                desc_lines = [line.strip('* ').strip() for line in prod_desc_raw.split('\n') if line.strip().startswith('*')]
                
                # Extract real product name from description if possible (e.g., "**Product Name:** Description")
                product_key = name # Default to headline
                for line in desc_lines:
                    # Look for bold text at start of line
                    key_match = re.match(r'\*\*(.*?)\*\*:', line)
                    if key_match:
                        product_key = key_match.group(1).strip()
                        break
                
                link_match = re.search(r'\[SHOP\s+(.*?)\]', prod_desc_raw)
                link_text = f"SHOP {link_match.group(1)}" if link_match else "SHOP NOW"
                
                data['products'].append({
                    'name': name,
                    'product_key': product_key,
                    'description': desc_lines,
                    'cta': link_text
                })
            
            section_cta = extract_value(section, 'CTA Button')
            if section_cta:
                data['footer_cta'] = section_cta

    return data

def extract_value(text, key):
    match = re.search(f'\*\*{key}:\*\*\s+(.*?)\n', text)
    if match:
        return match.group(1).strip()
    return None

def log_debug(message):
    print(message)
    # with open("debug_log.txt", "a", encoding="utf-8") as f:
    #     f.write(message + "\n")

def find_hero_image(date_code):
    if not date_code:
        log_debug("Debug: No date_code found.")
        return None
    
    base_dir = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\03_Production\04_Assets\images"
    target_dir = os.path.join(base_dir, date_code)
    
    log_debug(f"Debug: Checking directory: {target_dir}")
    if not os.path.exists(target_dir):
        log_debug("Debug: Directory does not exist.")
        return None
        
    # Look for hero*.*
    for file in os.listdir(target_dir):
        log_debug(f"Debug: Found file: {file}")
        if file.lower().startswith('hero') and file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            # Return relative path for HTML (assuming HTML is in .../04_Assets/html/)
            # Path from html folder to image folder: ../images/DATE/file
            found_path = f"../images/{date_code}/{file}"
            log_debug(f"Debug: Found hero image: {found_path}")
            return found_path
            
    log_debug("Debug: No hero image found in directory.")
    return None

def find_product_image(date_code, product_index, product_name):
    """
    Find product image by index (product_1.jpg) or name match.
    """
    if not date_code:
        return None
        
    base_dir = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\03_Production\04_Assets\images"
    target_dir = os.path.join(base_dir, date_code)
    
    if not os.path.exists(target_dir):
        return None
    
    # Priority 1: Exact match "product_X.png/jpg"
    # product_index is 0-based, so we look for product_{index+1}
    p_num = product_index + 1
    for ext in ['.png', '.jpg', '.jpeg', '.webp']:
        filename = f"product_{p_num}{ext}"
        if os.path.exists(os.path.join(target_dir, filename)):
            log_debug(f"Debug: Found product image by index: {filename}")
            return f"../images/{date_code}/{filename}"

    # Priority 2: Fuzzy match by name (simplified)
    # This is a bit risky but useful. Let's stick to index for now for reliability.
    
    return None

def generate_html(data):
    # Try to find hero image
    hero_image_src = find_hero_image(data.get('date_code'))
    
    # Hero Image HTML
    if hero_image_src:
        hero_html = f'<img src="{hero_image_src}" alt="{data["hero"].get("headline", "Hero Image")}" style="width: 100%; max-width: 600px; height: auto; display: block; margin-bottom: 20px;">'
    else:
        hero_html = f'''
            <div style="background-color: #ddd; width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #666;">
                [HERO IMAGE: {data['hero'].get('headline', 'Spring Image')}]
            </div>
        '''

    # Basic CSS for email
    style = get_css()

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{data['subject']}</title>
    {style}
</head>
<body>
    <div style="display:none;font-size:1px;color:#333333;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">
        {data['preview']}
    </div>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <img src="https://depology.com/cdn/shop/files/Depology_Logo_Black_150x.png" alt="Depology" width="150">
        </div>

        <!-- Hero -->
        <div class="hero">
            {hero_html}
            <h1>{data['hero'].get('headline', '')}</h1>
            <p>{data['hero'].get('subheadline', '')}</p>
            {f'<a href="{PRODUCT_URLS.get(data["hero"].get("cta"), "#")}" class="btn">{data["hero"].get("cta", "SHOP NOW")}</a>' if data['hero'].get('cta') else ''}
        </div>

        <!-- Body -->
        <div class="content">
            <h2>{data['body'].get('headline', '')}</h2>
            <p>{data['body'].get('copy', '')}</p>
            
            {generate_goals_html(data['body'].get('goals'))}
        </div>

        <!-- Products -->
        <div class="product-section">
            <h2 style="text-align: center; margin-bottom: 30px;">{data.get('products_headline', 'Featured Products')}</h2>
            {generate_products_html(data['products'], data.get('date_code'))}
            
            {f'<div style="text-align:center; margin-top:30px;"><a href="{PRODUCT_URLS.get(data.get("footer_cta"), "#")}" class="btn">{data.get("footer_cta", "SHOP ALL")}</a></div>' if data.get('footer_cta') else ''}
        </div>

        <!-- Footer -->
        <div class="footer">
            <p>© 2026 Depology. All rights reserved.</p>
            <p>Unsubscribe | View in Browser</p>
        </div>
    </div>
</body>
</html>
    """
    return html

def generate_goals_html(goals):
    if not goals:
        return ""
    items = "".join([f"<li>{g}</li>" for g in goals])
    return f'<div class="goals"><ul>{items}</ul></div>'

def generate_products_html(products, date_code=None):
    html = ""
    for i, p in enumerate(products):
        # Try to find image
        img_src = find_product_image(date_code, i, p['name'])
        
        if img_src:
            img_html = f'<img src="{img_src}" alt="{p["name"]}" style="width: 100%; height: auto; margin-bottom: 15px; display: block;">'
        else:
            img_html = f'''
            <div style="background-color: #f0f0f0; width: 100%; height: 200px; margin-bottom: 15px; display: flex; align-items: center; justify-content: center; color: #888;">
                [PRODUCT IMAGE: {p['name']}]
            </div>
            '''
            
        desc_list = "".join([f"<li>{d}</li>" for d in p['description']])
        
        # Determine Product URL
        # 1. Try exact name match (product_key)
        # 2. Try headline match (name)
        # 3. Fallback to #
        product_url = PRODUCT_URLS.get(p.get('product_key'), PRODUCT_URLS.get(p['name'], "#"))
        
        html += f"""
        <div class="product">
            <!-- Product Image -->
            {img_html}
            <h3>{p['name']}</h3>
            <ul>{desc_list}</ul>
            <a href="{product_url}" style="color: #000; font-weight: bold; text-decoration: underline;">{p['cta']} &rarr;</a>
        </div>
        """
    return html

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_email_html.py <markdown_file_path>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    log_debug(f"Processing {input_path}...")
    try:
        data = parse_markdown(input_path)
        log_debug("Markdown parsed successfully.")
        
        # Debug: Check data and URL lookup
        hero_cta = data.get('hero', {}).get('cta')
        footer_cta = data.get('footer_cta')
        
        log_debug(f"Hero CTA (repr): {repr(hero_cta)}")
        log_debug(f"Hero CTA URL: {PRODUCT_URLS.get(hero_cta, 'NOT FOUND')}")
        
        log_debug(f"Footer CTA (repr): {repr(footer_cta)}")
        log_debug(f"Footer CTA URL: {PRODUCT_URLS.get(footer_cta, 'NOT FOUND')}")

        for p in data.get('products', []):
            log_debug(f"Product: {p.get('name')}, Key: {p.get('product_key')}")
            
    except Exception as e:
        log_debug(f"Error parsing markdown: {e}")
        sys.exit(1)
    
    html_content = generate_html(data)
    
    filename = os.path.basename(input_path).replace('.md', '.html')
    output_dir = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\03_Production\04_Assets\html"
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    log_debug(f"Success! HTML generated at: {output_path}")
    if data.get('date_code'):
        print(f"Checked for images in: 04_Assets/images/{data.get('date_code')}")
