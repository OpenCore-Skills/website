import os
import yaml
from jinja2 import Environment, FileSystemLoader

# --- Configuration ---
# All paths are relative to the repository root
SKILLS_DIR = "skills"
TEMPLATE_FILE = "templates/skill_template.html"
INDEX_SOURCE_PATH = "docs/index.html"
OUTPUT_DIR = "dist"  # This is the folder GitHub Pages will deploy

# --- Setup ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
env = Environment(loader=FileSystemLoader('.')) # Look for templates from root
template = env.get_template(TEMPLATE_FILE)

print(f"Loading skills from: {SKILLS_DIR}")
print(f"Using template: {TEMPLATE_FILE}")
print(f"Outputting to: {OUTPUT_DIR}")

# --- Generation Loop (Generates skill pages) ---
skill_files = [f for f in os.listdir(SKILLS_DIR) if f.endswith('.yaml')]

for filename in skill_files:
    skill_name = filename.split('.')[0]
    input_path = os.path.join(SKILLS_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, f"{skill_name}.html")
    
    print(f"  -> Generating {output_path} from {input_path}")
    
    with open(input_path, 'r') as f:
        raw_yaml_content = f.read()
        f.seek(0)
        skill_data = yaml.safe_load(f)
        
    html_content = template.render(
        skill=skill_data, 
        raw_yaml=raw_yaml_content
    )
    
    with open(output_path, 'w') as f:
        f.write(html_content)

# --- Final Step (Copies your main index.html) ---
print(f"Copying {INDEX_SOURCE_PATH} to {OUTPUT_DIR}/index.html")
try:
    with open(INDEX_SOURCE_PATH, "r") as f:
        index_content = f.read()
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(index_content)
except FileNotFoundError:
    print(f"ERROR: Cannot find index file at '{INDEX_SOURCE_PATH}'.")
    print("Build failed.")
    exit(1)

print("\nBuild complete! Site generated in /dist")
