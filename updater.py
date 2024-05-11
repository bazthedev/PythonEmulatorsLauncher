import requests
import zipfile
import json
import os

with open("config.json", "r") as f:
    config = json.load(f)

cver = config["version"]

new_ver = requests.get("https://api.github.com/repos/bazthedev/PythonEmulatorsLauncher/releases/latest")
new_ver_str = new_ver.json()["name"]

if cver < new_ver_str:
    print("New version found")
else:
    print("Up to date")