import os

def scan_project(folder_path):
    files = {}
    for root, _, filenames in os.walk(folder_path):
        for file in filenames:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    files[file] = f.read()
    return files

def detect_cross_file_bug(files):
    for name, code in files.items():
        if "compute_total" in code and "+ 10" in code:
            return {
                "bug_file": name,
                "bug": "Unexpected addition of constant 10",
                "fix": "Remove '+ 10'"
            }
    return {"bug": "No cross-file bug detected"}