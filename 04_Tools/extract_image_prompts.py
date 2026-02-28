import re
import os
import sys

# Depology Brand Style Modifiers (Centralized Style Logic)
BRAND_STYLE = ( 
    "Professional commercial photography, skincare product photography, "
    "clean minimalist aesthetic, soft natural lighting, high resolution, 4k, "
    "clinical luxury style, white and soft green color palette, botanical elements"
)

def extract_prompts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    filename = os.path.basename(file_path).replace('.md', '')
    prompts = []
    
    # Find all Visual Reference sections
    # They usually look like:
    # **Visual Reference:**
    # * **Style:** ...
    # * **Image:** ...
    
    # We will split by sections first to know context (Hero vs Product)
    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)
    
    for section in sections:
        header_match = re.match(r'(.*?)\n', section)
        section_name = header_match.group(1).strip() if header_match else "General"
        
        vis_ref_match = re.search(r'\*\*Visual Reference:\*\*(.*?)(?=\n\*\*|\n##|$)', section, re.DOTALL)
        if vis_ref_match:
            vis_block = vis_ref_match.group(1).strip()
            print(f"Found Visual Block in {section_name}") # Debug
            
            # Extract Image description - More robust regex
            # Looks for "* **Image:**" or just "**Image:**" allowing for list markers
            img_desc_match = re.search(r'(?:\*\s+)?\*\*Image:\*\*\s+(.*?)(?=\n(?:\*|\-)|$)', vis_block, re.DOTALL)
            style_match = re.search(r'(?:\*\s+)?\*\*Style:\*\*\s+(.*?)(?=\n(?:\*|\-)|$)', vis_block, re.DOTALL)
            
            if img_desc_match:
                base_desc = img_desc_match.group(1).strip()
                style_desc = style_match.group(1).strip() if style_match else ""
                print(f"Extracted Image: {base_desc[:30]}...") # Debug

                
                # Construct the final DALL-E prompt
                final_prompt = (
                    f"{base_desc}. "
                    f"Style details: {style_desc}. "
                    f"{BRAND_STYLE}"
                )
                
                prompts.append({
                    'section': section_name,
                    'description': base_desc,
                    'dalle_prompt': final_prompt
                })
                
    return prompts, filename

def save_prompts(prompts, filename):
    output_dir = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\03_Production\04_Assets\prompts"
    output_file = os.path.join(output_dir, f"{filename}_prompts.md")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# AI Image Prompts for: {filename}\n\n")
        f.write("> Use these prompts in ChatGPT Plus (DALL-E 3).\n\n")
        
        for idx, p in enumerate(prompts, 1):
            f.write(f"## {idx}. {p['section']} Image\n")
            f.write(f"**Context:** {p['description']}\n\n")
            f.write("```text\n")
            f.write(p['dalle_prompt'])
            f.write("\n```\n\n")
            f.write("---\n\n")
            
    return output_file

if __name__ == "__main__":
    default_path = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\03_Production\01_Email_Drafts\March\20260302_Spring_Cleaning_Routine.md"
    
    if len(sys.argv) < 2:
        print(f"No arguments provided. Defaulting to: {default_path}")
        input_path = default_path
    else:
        input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    print(f"Extracting prompts from {input_path}...")
    prompts, name = extract_prompts(input_path)
    
    if prompts:
        out_path = save_prompts(prompts, name)
        print(f"Success! Prompts saved to: {out_path}")
    else:
        print("No Visual References found in this draft.")
