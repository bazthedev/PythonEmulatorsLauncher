from pyboy import PyBoy

def run_gb_emu(path : str):
    gbrom = PyBoy(path)
    while gbrom.tick():
        pass
    gbrom.stop()