import os
import re

base_dir = r"d:\infinity website"

# 1. Rename files in projects/
projects_dir = os.path.join(base_dir, "projects")
if os.path.exists(projects_dir):
    for f in os.listdir(projects_dir):
        if "emperia" in f.lower():
            old_path = os.path.join(projects_dir, f)
            new_f = f.lower().replace("emperia", "infinity")
            new_path = os.path.join(projects_dir, new_f)
            os.rename(old_path, new_path)
            print(f"Renamed: {f} -> {new_f}")

# 2. Rename files in asset/
asset_dir = os.path.join(base_dir, "asset")
if os.path.exists(asset_dir):
    for f in os.listdir(asset_dir):
        if "emperia" in f.lower():
            old_path = os.path.join(asset_dir, f)
            new_f = f.lower().replace("emperia", "infinity")
            new_path = os.path.join(asset_dir, new_f)
            os.rename(old_path, new_path)
            print(f"Renamed: {f} -> {new_f}")

# 3. Replace content in all HTML files
for root, dirs, files in os.walk(base_dir):
    if "website design" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Case-sensitive replaces for general text
            content = content.replace("Emperia", "Infinity")
            content = content.replace("emperia", "infinity")
            content = content.replace("EMPERIA", "INFINITY")

            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)

print("Replacement complete.")
