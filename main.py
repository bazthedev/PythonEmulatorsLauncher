from emulators.runnes import run_nes_emu as rne
from emulators.rungb import run_gb_emu as rge
from emulators.runnds import run_nds_emu as rndse

import os
import json

def clear_scr():
    os.system("cls")

def reset_config():
    autoupd = input("Would you like to enable automatic updates? (y/n)")
    if autoupd[0].lower() == "y":
        aupd = True
    else:
        aupd = False
    with open("config.json", "w") as f:
        conf = {}
        conf["version"] = "0.0.1"
        conf["romdir"] = "./roms"
        conf["autoupd"] = aupd
        conf["foundroms"] = []
        conf["foundnesroms"] = []
        conf["foundgbroms"] = []
        conf["foundgbcroms"] = []
        conf["foundndsroms"] = []
        conf["foundn64roms"] = []
        json.dump(conf, f, indent=4)

if not os.path.exists("./config.json"):
    reset_config()


with open("config.json", "r") as f:
        config = json.load(f)
        loaded_config = True
    

romdir = config["romdir"]

def findroms():
    
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

    if config["foundroms"] == [] and loaded_config:
            for rom in os.listdir(romdir):

                if rom.endswith(".nes") or rom.endswith(".gb") or rom.endswith(".gbc") or rom.endswith(".nds") or rom.endswith(".z64"):
                    found_roms.append(str(rom))
                
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
    
    if loaded_config and config["foundroms"] != []:
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
    [U] Update the App
    [X] Exit
"""

nesemu = False
gbemu = False
gbcemu = False
ndsemu = False
n64emu = False

foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms()
print(menu)
running = True
print("Detected roms:")
for rm in foundroms:
        print("     - " + rm)
while running == True:
    #print(foundn64roms, foundndsroms, foundnesroms, foundgbcroms, foundgbroms, foundroms)
    print(optn)
    choice = input("\n\nEnter Selection: ")
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
        foundroms, foundnesroms, foundgbroms, foundgbcroms, foundndsroms, foundn64roms = findroms()
        print(f"Found {str(len(foundroms))} roms!")
    elif choice.lower() == "v":
        print("Detected roms:")
        for rm in foundroms:
            print("     - " + rm)
        print(f"Found {str(len(foundroms))} roms!")
    elif choice.lower() == "c":
        pass # change romdir
    elif choice.lower() == "d":
        reset_config()
        with open("config.json", "r") as f:
            config = json.load(f)
            loaded_config = True
    elif choice.lower() == "i":
        print("PythonEmulatorsLauncher")
        print(f"Version: {config['version']}")
    elif choice.lower() == "s":
        print("Current settings:")
    elif choice.lower() == "u":
        pass #update app
    elif choice.lower() == "x":
        print("Exitting...")
        break