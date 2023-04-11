import os

# ignore the venv folder and .git folder and files within them, and ignore __pycache__ folders
ignore_list = ['myenv', '.git', 'venv','migrations','__pycache__','.mypy_cache']
ignore_dirs = ['__pycache__']

for root, dirs, files in os.walk("."):
    # Remove ignored directories from dirs
    dirs[:] = [d for d in dirs if d not in ignore_dirs]

    # check if any of the directories to be ignored is in the root path
    if any([ig_dir in root for ig_dir in ignore_list]):
        continue

    level = root.replace(".", "").count(os.sep)
    indent = " " * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")

    subindent = " " * 4 * (level + 1)
    for f in files:
        if not f.endswith('.exe') and not f.endswith('.pyc'):
            filepath = os.path.join(root, f)
            filesize = os.path.getsize(filepath)
            filesize_kb = filesize / 1024
            filesize_str = f"{filesize_kb:.2f} KB" if filesize_kb < 1024 else f"{filesize_kb/1024:.2f} MB"
            print(f"{subindent}{f} ({filesize_str})")
