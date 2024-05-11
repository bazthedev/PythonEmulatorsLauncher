from desmume.emulator import DeSmuME

def run_nds_emu(path : str):
    ndsrom = DeSmuME()
    ndsrom.open(path)

    # Create the window for the emulator
    window = ndsrom.create_sdl_window()

    # Run the emulation as fast as possible until quit
    while not window.has_quit():
        window.process_input()   # Controls are the default DeSmuME controls, see below.
        ndsrom.cycle()
        window.draw()