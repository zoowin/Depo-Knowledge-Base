import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder(filename, width, height, text, bg_color="#F5F5F0", text_color="#333333"):
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Try to load a font, otherwise use default
    try:
        # Try a few common fonts on macOS
        font_path = "/System/Library/Fonts/Helvetica.ttc"
        if not os.path.exists(font_path):
             font_path = "/Library/Fonts/Arial.ttf"
        
        # Calculate font size based on image width (approx 1/20th)
        font_size = int(width / 25)
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Wrap text
    lines = []
    words = text.split()
    current_line = []
    
    # Simple word wrap
    # Note: This is a rough estimation, for proper wrapping we'd need to measure text size
    # but for a placeholder script, manual line breaks in input or simple char count is often enough.
    # Let's just do a simple character count wrap for now.
    max_chars = 40 if width < 800 else 60
    
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars:
            current_line += (word + " ")
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    
    # Calculate total text height
    # getbbox returns (left, top, right, bottom)
    line_heights = [d.textbbox((0, 0), line, font=font)[3] - d.textbbox((0, 0), line, font=font)[1] for line in lines]
    # Add some padding between lines
    line_spacing = int(font_size * 0.5)
    total_height = sum(line_heights) + (len(lines) - 1) * line_spacing
    
    # Start drawing
    y = (height - total_height) / 2
    
    for i, line in enumerate(lines):
        # Center horizontally
        text_width = d.textlength(line, font=font)
        x = (width - text_width) / 2
        
        d.text((x, y), line, fill=text_color, font=font)
        y += line_heights[i] + line_spacing

    # Add dimensions text at bottom
    dim_text = f"{width} x {height}"
    dim_font_size = int(font_size * 0.6)
    try:
        dim_font = ImageFont.truetype(font_path, dim_font_size)
    except:
        dim_font = ImageFont.load_default()
        
    dim_width = d.textlength(dim_text, font=dim_font)
    d.text(((width - dim_width) / 2, height - dim_font_size * 2), dim_text, fill=text_color, font=dim_font)

    # Save
    img.save(filename)
    print(f"Generated: {filename}")

# Configuration
output_dir = "Depo EDM Knowledge Base/Assets/images/20260128"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Hero Image - Visual Description from Email
hero_text = "Visual: Soft sunlight, daily traces: half-used serum bottle, opened notebook, water glass + book. Clean, breathable."

# 1. Desktop Hero
create_placeholder(
    os.path.join(output_dir, "20260128_beauty_of_progress_hero_desktop.png"),
    1200, 600,
    f"HERO (Desktop)\n{hero_text}"
)

# 2. Mobile Hero
create_placeholder(
    os.path.join(output_dir, "20260128_beauty_of_progress_hero_mobile.png"),
    750, 1000,
    f"HERO (Mobile)\n{hero_text}"
)

# 3. Product Placeholders (Optional but good)
products = [
    ("Cica Recovery Serum", "Soothes visible redness"),
    ("Matrixyl 3000 Collagen Serum", "Hydrates & plumps fine lines"),
    ("Pro-Firming Overnight Dream Mask", "Works while you sleep")
]

for i, (prod_name, desc) in enumerate(products, 1):
    filename = f"20260128_product_{i}_{prod_name.replace(' ', '_').lower()}.png"
    create_placeholder(
        os.path.join(output_dir, filename),
        600, 600, # Square for products usually
        f"PRODUCT {i}\n{prod_name}\n{desc}"
    )
