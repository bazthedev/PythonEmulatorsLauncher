from desmume.emulator import DeSmuME

def run_nds_emu(path : str):
    ndsrom = DeSmuME()
    ndsrom.open(path)
    window = ndsrom.create_sdl_window()
    while not window.has_quit():
        window.process_input()
        ndsrom.cycle()
        window.draw()
    ndsrom.destroy()
