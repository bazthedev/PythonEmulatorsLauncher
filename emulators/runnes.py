from nes.pycore.system import NES as pyNES

def run_nes_emu(path : str):

    rom = pyNES(path)

    rom.run()