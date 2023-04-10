import os
import re
import sys

if sys.argv[1] is None:
    raise ValueError(
        "Please provide a path to the directory containing the files to rename."
    )

# Define the path to the directory containing the files
target_dir = sys.argv[1]
suffix = "_ref"

# Compile a regular expression to match file extensions
ext_pattern = re.compile(r"\.[^.]+$")

for root, dirs, files in os.walk(target_dir):
    for filename in files:
        if ext_pattern.search(filename) and not filename.endswith(suffix):
            old_path = os.path.join(root, filename)
            ext = ext_pattern.search(old_path).group()
            new_path = (
                os.path.join(root, ext_pattern.sub(rf"{suffix}\g<0>", filename)) + ext
            )
            print(f"Renaming {old_path} to {new_path}...")
            os.rename(old_path, new_path)
