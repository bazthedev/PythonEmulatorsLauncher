import requests
import zipfile
import json
import os

with open("./config.json", "r") as f:
    config = json.load(f)

cver = config["version"]

new_ver = requests.get("https://api.github.com/repos/bazthedev/PythonEmulatorsLauncher/releases/latest")
new_ver_str = new_ver.json()["name"]

def check_update():
    cver = config["version"]
    new_ver = requests.get("https://api.github.com/repos/bazthedev/PythonEmulatorsLauncher/releases/latest")
    new_ver_str = new_ver.json()["name"]

    if cver < new_ver_str:
        return True
    else:
        return False

def update(version : str):
    files = ["./main.py", "./emulators/runnes.py", "./emulators/rungb.py", "./emulators/runnds.py", "./requirements.txt"]
    if check_update():
        print(f"New update found\nDownloading new version {version}")
        toupd = requests.get(f"https://github.com/bazthedev/PythonEmulatorsLauncher/releases/download/{version}/PEL_{version}.zip")
        with open(f"PEL_{version}.zip", "wb") as p:
            p.write(toupd.content)
            p.close()
        print("Downloaded version\nInstalling...")
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        print("Deleted old versions of files")
        with zipfile.ZipFile(f"./PEL_{version}.zip", "r") as newverzip:
            newverzip.extractall("./")
        config["version"] = version
        with open("./config.json", "w") as f:
            json.dump(config, f, indent=4)
        print("Cleaning up...")
        os.remove(f"./PEL_{version}.zip")
        print("Successfully updated!")
    else:
        return False
    
update(new_ver_str)