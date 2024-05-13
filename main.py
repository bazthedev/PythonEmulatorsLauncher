from emulators.runnes import run_nes_emu as rne
from emulators.rungb import run_gb_emu as rge
from emulators.runnds import run_nds_emu as rndse



import requests
import os
import json


config_options = ["version", "romdir", "autoupd", "bypass_config_check", "foundroms", "foundnesroms", "foundgbroms", "foundgbcroms", "foundndsroms", "foundn64roms"]

def clear_scr():
    os.system("cls")

def reset_config():
    autoupd = input("Would you like to enable automatic updates? (y/n) ")
    if autoupd[0].lower() == "y":
        aupd = True
    else:
        aupd = False
    with open("config.json", "w") as f:
        conf = {}
        conf["version"] = "0.0.5"
        conf["romdir"] = "./roms"
        conf["autoupd"] = aupd
        conf["bypass_config_check"] = False
        conf["foundroms"] = []
        conf["foundnesroms"] = []
        conf["foundgbroms"] = []
        conf["foundgbcroms"] = []
        conf["foundndsroms"] = []
        conf["foundn64roms"] = []
        json.dump(conf, f, indent=4)



if not os.path.exists("./config.json"):
    reset_config()

from updater import check_update

with open("config.json", "r") as f:
        config = json.load(f)
        loaded_config = True


if not os.path.exists("./roms") and config["romdir"] == "./roms":
    os.mkdir("./roms")

if not os.path.exists("./updater.py"):
            updater = requests.get("https://raw.githubusercontent.com/bazthedev/PythonEmulatorsLauncher/main/updater.py")
            with open("./updater.py", "wb") as f:
                f.write(updater.content)
                f.close()


if config["autoupd"] and check_update():
        print("Update found, please run updater.py")
else:
    print(f"You are already running the latest version!\nVersion: {config['version']}")

def config_check(config : dict):
    corrupt = False
    for option in config_options:
        if (option not in config_options) or (option in config_options and (option not in config)):
            corrupt = True
    if corrupt:
        reset_conf_chk = input("Config seems to be corrupt, would you like to reset?\nMake sure you make a backup of your config incase you forget your settings.\n\ny/n: ")
        if reset_conf_chk.lower() == "y":
            reset_config()
            print("Config has been reset")
        else:
            print("Config has not been reset")

romdir = config["romdir"]

update_config = False

def findroms(romdir : str, update_config : bool):
    
    found_roms = []
    found_nes_roms = []
    found_gb_roms = []
    found_gbc_roms = []
    found_nds_roms = []
    found_n64_roms = []

    if loaded_config != True:

        for rom in os.listdir(romdir):

            if rom.endswith(".nes") or rom.endswith(".gb") or rom.endswith(".gbc") or rom.endswith(".nds") or rom.endswith(".z64"):
                found_roms.append(str(rom))
            elif rom.endswith(".ram"):
                pass
            else:
                print("Invalid filetype found")
                
            if rom.endswith(".nes"):
                found_nes_roms.append(rom)
            elif rom.endswith(".gb"):
                found_gb_roms.append(rom)
            elif rom.endswith(".gbc"):
                found_gbc_roms.append(rom)
            elif rom.endswith(".nds"):
                found_nds_roms.append(rom)
            elif rom.endswith(".z64"):
                found_n64_roms.append(rom)

    elif update_config == True:
        for rom in os.listdir(romdir):

                if rom.endswith(".nes") or rom.endswith(".gb") or rom.endswith(".gbc") or rom.endswith(".nds") or rom.endswith(".z64"):
                    found_roms.append(str(rom))
                elif rom.endswith(".ram"):
                    pass
                else:
                    print("Invalid filetype found")

                if rom.endswith(".nes"):
                    found_nes_roms.append(rom)
                elif rom.endswith(".gb"):
                    found_gb_roms.append(rom)
                elif rom.endswith(".gbc"):
                    found_gbc_roms.append(rom)
                elif rom.endswith(".nds"):
                    found_nds_roms.append(rom)
                elif rom.endswith(".z64"):
                    found_n64_roms.append(rom)
        config["foundroms"] = found_roms
        config["foundnesroms"] = found_nes_roms
        config["foundgbroms"] = found_gb_roms
        config["foundgbcroms"] = found_gbc_roms
        config["foundndsroms"] = found_nds_roms
        config["foundn64roms"] = found_n64_roms
            
        with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
        update_config = False

    elif config["foundroms"] == [] and loaded_config:
            for rom in os.listdir(romdir):

                if rom.endswith(".nes") or rom.endswith(".gb") or rom.endswith(".gbc") or rom.endswith(".nds") or rom.endswith(".z64"):
                    found_roms.append(str(rom))
                elif rom.endswith(".ram"):
                    pass
                else:
                    print("Invalid filetype found")

                if rom.endswith(".nes"):
                    found_nes_roms.append(rom)
                elif rom.endswith(".gb"):
                    found_gb_roms.append(rom)
                elif rom.endswith(".gbc"):
                    found_gbc_roms.append(rom)
                elif rom.endswith(".nds"):
                    found_nds_roms.append(rom)
                elif rom.endswith(".z64"):
                    found_n64_roms.append(rom)
            config["foundroms"] = found_roms
            config["foundnesroms"] = found_nes_roms
            config["foundgbroms"] = found_gb_roms
            config["foundgbcroms"] = found_gbc_roms
            config["foundndsroms"] = found_nds_roms
            config["foundn64roms"] = found_n64_roms
            
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
    
    

    elif loaded_config and config["foundroms"] != []:
        found_roms = config["foundroms"]
        found_nes_roms = config["foundnesroms"]
        found_gb_roms = config["foundgbroms"]
        found_gbc_roms = config["foundgbcroms"]
        found_nds_roms = config["foundndsroms"]
        found_n64_roms = config["foundn64roms"]

    return found_roms, found_nes_roms, found_gb_roms, found_gbc_roms, found_nds_roms, found_n64_roms


menu = """
                                    Python Emulators Launcher
                            A CLI launcher for emulators made with python
"""

optn = """
Options:
    [!] Press the number key and then enter to select a system

    [1] Nintendo Entertainment System (*.nes)
    [2] Gameboy (*.gb)
    [3] Gameboy Colour (*.gbc)
    [4] Nintendo DS (*.nds)
    [5] Nintendo 64 (*.z64)

    
Other options:
    [R] Rescan Rom Directory
    [V] View Detected Roms
    [C] Change Rom Directory
    [D] Reset Config File to Default Options
    [I] View Information about this Program
    [S] View Current Config
    [BCC] Bypass Config Check
    [B] Backup Config
    [IB] Import Config Backup
    [U] Update the App
    [X] Exit
"""
try:
    if not config["bypass_config_check"]:
        config_check(config)
except Exception:
    config_check(config)

foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms(romdir, update_config)
print(menu)
running = True
print("Detected roms:")
for rm in foundroms:
        print("     - " + rm)
while running == True:
    print(optn)
    choice = input("\n\nEnter Selection: ")
    clear_scr()
    if choice == "1":
        print("Found NES Roms:")
        for r in foundnesroms:
            print("     - " + r)    
        romtorun = input("Enter rom name as shown in the list above (including .nes): ")
        if romtorun not in foundnesroms:
            print("Rom does not exist")
            continue
        rne(romdir + "/" + romtorun)
    elif choice == "2":
        print("Found GB Roms:")
        for r in foundgbroms:
            print("     - " + r)    
        romtorun = input("Enter rom name as shown in the list above (including .gb): ")
        if romtorun not in foundgbroms:
            print("Rom does not exist")
            continue
        rge(romdir + "/" + romtorun)
    elif choice == "3":
        print("Found GBC Roms:")
        for r in foundgbcroms:
            print("     - " + r)    
        romtorun = input("Enter rom name as shown in the list above (including .gbc): ")
        if romtorun not in foundgbcroms:
            print("Rom does not exist")
            continue
        rge(romdir + "/" + romtorun)
    elif choice == "4":
        print("Found NDS Roms:")
        for r in foundndsroms:
            print("     - " + r)    
        romtorun = input("Enter rom name as shown in the list above (including .nds): ")
        if romtorun not in foundndsroms:
            print("Rom does not exist")
            continue
        rndse(romdir + "/" + romtorun)
    elif choice == "5":
        pass #m64py
    elif choice.lower() == "r":
        print("Rescanning rom directory...")
        foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms(romdir, update_config)
        print(f"Found {str(len(foundroms))} roms!")
    elif choice.lower() == "v":
        if update_config:
            print("You are using the already scanned roms from an old directory, please select [R] to refresh the rom list.")
        print("Detected roms:")
        for rm in foundroms:
            print("     - " + rm)
        print(f"Found {str(len(foundroms))} roms!")
    elif choice.lower() == "c":
        newromdir = input("Input new rom directory: ")
        if newromdir == romdir:
            continue
        if os.path.exists(newromdir):
            config["romdir"] = newromdir
            config["foundroms"] = []
            config["foundnesroms"] = []
            config["foundgbroms"] = []
            config["foundgbcroms"] = []
            config["foundndsroms"] = []
            config["foundn64roms"] = []
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            romdir = newromdir
            print("Refreshing rom directory...")
            foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms(romdir, True)
            print("Done.")
    elif choice.lower() == "d":
        reset_config()
        with open("config.json", "r") as f:
            config = json.load(f)
        loaded_config = True
        print("Reset config, now refreshing rom directory.")
        foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms(romdir, True)
    elif choice.lower() == "i":
        print(menu)
        print(f"Version: {config['version']}")
    elif choice.lower() == "s":
        print("Current settings:")
        print(f"Rom directory: {config['romdir']}")
        print(f"Automatic updates: {config['autoupd']}")
    elif choice.lower() == "b":
        if os.path.exists("config.json.bak"):
            print("Backup already exists, proceeding will overwrite the old backup.")
        c = input("Type y to continue: ")
        if c.lower() == "y":
            with open("config.json.bak", "w") as cb:
                json.dump(config, cb, indent=4)
        else:
            continue
    elif choice.lower() == "ib":
        if not os.path.exists("config.json.bak"):
            print("Backup not found")
            continue
        c = input("Type y to import backup: ")
        if c.lower() == "y":
            with open("config.json.bak", "r") as bc:
                backup_conf = json.load(bc)
            with open("config.json", "w") as f:
                json.dump(backup_conf, f, indent=4)
    elif choice.lower() == "bcc":
        if config["bypass_config_check"] == True:
            bccchk = input("Would you like to turn on config check bypassing?\ny/n: ")
            if bccchk.lower() == "y":
                config["bypass_config_check"] = True
                with open("config.json", "w") as f:
                    json.dump(config, f, indent=4)
                print("Bypassing enabled!")
        else:
            bccchk = input("Would you like to turn off config check bypassing?\ny/n: ")
            if bccchk.lower() == "y":
                config["bypass_config_check"] = False
                with open("config.json", "w") as f:
                    json.dump(config, f, indent=4)
                print("Bypassing disabled!")
    elif choice.lower() == "u":
            updater = requests.get("https://raw.githubusercontent.com/bazthedev/PythonEmulatorsLauncher/main/updater.py")
            with open("./updater.py", "wb") as f:
                f.write(updater.content)
                f.close()
            print("Please run the updater.py file to update the app.")
            print("If you are having trouble with the updater, delete updater.py, choose the U option in the menu and it will download the latest updater.")
    elif choice.lower() == "x":
        print("Exitting...")
        break

    print("\n")
