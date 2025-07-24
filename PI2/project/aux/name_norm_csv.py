import os
import re

# Replace with your directory path
directory = "/home/nicolas/Escritorio/Bootcamp D.E/PI2/project/data/CSV/"

# Regex pattern to match files like "1.filename.csv" or "23.other_name.CSV"
pattern = re.compile(r"^\d+\.(.+\.csv)$", re.IGNORECASE)

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        new_name = match.group(1).lower()
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Rename file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
