"""Reconstruct an already extracted MSI's files without running its actions."""
import argparse
import json
import shutil
from pathlib import Path
import msilib

parser = argparse.ArgumentParser()
parser.add_argument("msi", type=Path)
parser.add_argument("extracted", type=Path)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
db = msilib.OpenDatabase(str(args.msi.resolve()), msilib.MSIDBOPEN_READONLY)

def rows(query):
    view = db.OpenView(query)
    view.Execute(None)
    while (record := view.Fetch()) is not None:
        yield [record.GetString(i) for i in range(1, record.GetFieldCount() + 1)]

directories = {key: (parent, name) for key, parent, name in rows(
    "SELECT `Directory`,`Directory_Parent`,`DefaultDir` FROM `Directory`")}
components = dict(rows("SELECT `Component`,`Directory_` FROM `Component`"))
root = args.destination.resolve()
source_root = args.extracted.resolve()
root.mkdir(parents=True, exist_ok=True)
resolved = {"TARGETDIR": root}

def directory(key):
    if key in resolved:
        return resolved[key]
    parent, name = directories[key]
    target_name = name.split(":", 1)[0].split("|")[-1]
    base = directory(parent) if parent else root
    result = base if target_name == "." else base / target_name
    result = result.resolve()
    if not result.is_relative_to(root):
        raise ValueError(f"Directory escapes destination: {key}")
    resolved[key] = result
    return result

copied = 0
missing = []
for file_id, component, filename in rows(
        "SELECT `File`,`Component_`,`FileName` FROM `File`"):
    source = (source_root / file_id).resolve()
    if not source.is_relative_to(source_root):
        raise ValueError("Source escapes extraction directory")
    target = (directory(components[component]) / filename.split("|")[-1]).resolve()
    if not target.is_relative_to(root):
        raise ValueError("File escapes destination")
    if not source.is_file():
        missing.append(file_id)
        continue
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    copied += 1
print(json.dumps({"copied": copied, "missing_count": len(missing), "missing": missing[:10]}))
if missing:
    raise SystemExit(1)
