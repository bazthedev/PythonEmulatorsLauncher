import requests
import zipfile
import json

with open("../config.json", "r") as f:
    config = json.load(f)

cver = config["version"]

new_ver = requests.get("https://api.github.com/repos/bazthedev/PythonEmulatorsLauncher/releases/latest")
print(new_ver.json()["name"])