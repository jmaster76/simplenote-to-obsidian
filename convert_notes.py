import json
import os
import sys
import subprocess
from datetime import datetime

def format_obsidian_date(date_val):
    if not date_val: return ""
    if isinstance(date_val, str):
        return date_val.split('.')[0].replace('Z', '').replace(' ', 'T')
    return ""

def set_mac_system_dates(file_path, created_str, modified_str):
    try:
        def to_setfile_format(dt_str):
            dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S")
            return dt.strftime("%m/%d/%Y %H:%M:%S")
        subprocess.run(['SetFile', '-d', to_setfile_format(created_str), file_path], check=True)
        subprocess.run(['SetFile', '-m', to_setfile_format(modified_str), file_path], check=True)
    except: pass

def convert_simplenote_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    notes = data.get("activeNotes", [])
    output_dir = "Obsidian_Import"
    os.makedirs(output_dir, exist_ok=True)

    for note in notes:
        raw_content = note.get("content", "")
        tags = note.get("tags", [])
        
        # Dates
        created_time = format_obsidian_date(note.get("creationDate", ""))
        modified_time = format_obsidian_date(note.get("lastModified", note.get("modificationDate", "")))

        # Filename = First line of note (minimal cleanup only for OS safety)
        lines = raw_content.splitlines()
        first_line = lines[0].strip() if lines else "Untitled"
        filename = first_line.replace("/", "-")[:100] + ".md"
        file_path = os.path.join(output_dir, filename)

        # Handle duplicate filenames
        counter = 1
        while os.path.exists(file_path):
            file_path = os.path.join(output_dir, f"{first_line.replace('/', '-')[:90]} ({counter}).md")
            counter += 1

        # YAML
        yaml_lines = ["---", f"created: {created_time}", f"updated: {modified_time}"]
        if tags:
            yaml_lines.append("tags:")
            for tag in tags: yaml_lines.append(f"  - {tag.strip()}")
        yaml_lines.append("---")
        
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write("\n".join(yaml_lines) + "\n\n" + raw_content)

        set_mac_system_dates(file_path, created_time, modified_time)

    print(f"Success! {len(notes)} notes processed.")

if __name__ == "__main__":
    convert_simplenote_json(sys.argv[1])