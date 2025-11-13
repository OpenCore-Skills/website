import os
import yaml
import json  # Import the JSON library
from jinja2 import Environment, FileSystemLoader

# --- Configuration ---
SKILLS_DIR = "skills"
TEMPLATE_FILE = "templates/skill_template.html"
INDEX_SOURCE_PATH = "docs/index.html"  # This is now a TEMPLATE
OUTPUT_DIR = "dist"

# --- Setup ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
env = Environment(loader=FileSystemLoader('.')) # Look for templates from root
skill_template = env.get_template(TEMPLATE_FILE)
# NEW: Load the index.html file as a template
index_template = env.get_template(INDEX_SOURCE_PATH) 

print(f"Loading skills from: {SKILLS_DIR}")
print(f"Using templates...")
print(f"Outputting to: {OUTPUT_DIR}")

# --- NEW: First Loop (Gather all skill data) ---
skills_list = []
skill_files = [f for f in os.listdir(SKILLS_DIR) if f.endswith(('.yaml', '.yml'))]

print("Gathering all skills...")
for filename in skill_files:
    input_path = os.path.join(SKILLS_DIR, filename)
    with open(input_path, 'r') as f:
        skill_data = yaml.safe_load(f)
        skills_list.append(skill_data)

print(f"Found {len(skills_list)} skills.")

# --- Second Loop (Generate individual skill pages) ---
print("Generating individual skill pages...")
for skill_data in skills_list:
    skill_name = skill_data['name']
    output_path = os.path.join(OUTPUT_DIR, f"{skill_name}.html")
    
    # We need the raw YAML content for the template
    input_path = os.path.join(SKILLS_DIR, f"{skill_name}.yaml") # Assumes .yaml, adjust if needed
    if not os.path.exists(input_path):
         input_path = os.path.join(SKILLS_DIR, f"{skill_name}.yml") # Check for .yml

    with open(input_path, 'r') as f:
        raw_yaml_content = f.read()
        
    html_content = skill_template.render(
        skill=skill_data, 
        raw_yaml=raw_yaml_content
    )
    
    with open(output_path, 'w') as f:
        f.write(html_content)
    print(f"  -> Generated {output_path}")

# --- NEW: Final Step (Generate the main index.html) ---
print(f"Generating main index.html...")
try:
    # Convert the Python list of skills to a JSON string
    # The 'safe' filter in Jinja will prevent HTML escaping
    skills_json = json.dumps(skills_list, indent=4)
    
    # Render the index template with the JSON data
    final_index_html = index_template.render(skills_json=skills_json)
    
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(final_index_html)
        
except Exception as e:
    print(f"ERROR: Failed to generate index.html: {e}")
    exit(1)

print("\nBuild complete! Site generated in /dist")
