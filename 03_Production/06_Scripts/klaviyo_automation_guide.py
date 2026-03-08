import requests
import re
import os

# --- CONFIGURATION ---
KLAVIYO_API_KEY = "YOUR_KLAVIYO_PRIVATE_API_KEY"
CAMPAIGN_NAME = "Spring Cleaning Your Routine"
CAMPAIGN_SUBJECT = "Spring cleaning... for your face?"
HTML_FILE_PATH = "../05_HTML_Drafts/March/20260302_Spring_Cleaning_Routine.html"
REGISTRY_FILE_PATH = "../04_Assets/product_image_registry.md"

def load_registry(file_path):
    """
    Parses the product image registry file to find product names and their URLs.
    Returns a dictionary: { "Product Name": "URL" }
    """
    registry = {}
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Simple regex to find "- **Name**" followed by "  - URL: [URL]"
            # Note: This is a basic parser and might need adjustment based on exact formatting.
            pattern = re.compile(r'- \*\*(.*?)\*\*\n\s+- URL: (\[.*?\]|http.*?)')
            matches = pattern.findall(content)
            for name, url in matches:
                if "PASTE_URL_HERE" not in url:
                    registry[name.strip()] = url.strip()
    except FileNotFoundError:
        print(f"Error: Registry file not found at {file_path}")
    return registry

def replace_images(html_content, registry):
    """
    Replaces [PASTE_URL_HERE] placeholders in the HTML with actual URLs from the registry.
    This requires the HTML to have some way to identify which product goes where.
    
    Current HTML uses generic [PASTE_URL_HERE]. 
    To make this work automatically, the HTML needs unique placeholders like:
    {{ product_images['Opuntia-C Relief Cleansing Balm'] }}
    
    For this example, we will just print what *would* happen.
    """
    # specific logic for this template
    # We would need to map specific HTML sections to product names manually or via data attributes
    # For demonstration, let's pretend we are replacing based on context or just print the available images
    print("Available images in registry:", registry.keys())
    
    # In a real implementation, you would use a templating engine like Jinja2
    # template = Template(html_content)
    # html_content = template.render(product_images=registry)
    
    return html_content

def create_campaign(api_key, name, subject, html_content):
    """
    Creates a campaign in Klaviyo using the API.
    """
    url = "https://a.klaviyo.com/api/campaigns/"
    headers = {
        "Authorization": f"Klaviyo-API-Key {api_key}",
        "Content-Type": "application/vnd.api+json",
        "revision": "2024-02-15"
    }
    
    payload = {
        "data": {
            "type": "campaign",
            "attributes": {
                "name": name,
                "audiences": {
                    "included": ["LIST_ID_OR_SEGMENT_ID"] # You need a list ID
                },
                "send_strategy": {
                    "method": "immediate"
                },
                "message": {
                    "subject": subject,
                    "preview_text": "Time to shed the winter layers.",
                    "from_email": "hello@depology.com",
                    "from_label": "Depology",
                    "content": {
                        "html": html_content
                    }
                }
            }
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"Successfully created campaign: {name}")
        return response.json()
    else:
        print(f"Failed to create campaign: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    # 1. Load HTML
    try:
        with open(HTML_FILE_PATH, 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"HTML file not found: {HTML_FILE_PATH}")
        exit()

    # 2. Load Registry
    registry = load_registry(REGISTRY_FILE_PATH)
    
    # 3. Replace Placeholders (Mock)
    # real_html = replace_images(html_content, registry)
    
    # 4. Upload to Klaviyo (Commented out for safety)
    # print("Uploading to Klaviyo...")
    # create_campaign(KLAVIYO_API_KEY, CAMPAIGN_NAME, CAMPAIGN_SUBJECT, html_content)
    
    print("Script execution completed (dry run).")
