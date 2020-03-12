from yaml import load, Loader
from sys import argv

# GUI option import
if len(argv) == 1: 
    from tkinter import Tk
    # local import
    from gui.GUI import GUI

# CIL option import
elif len(argv) == 2:
    # local import
    from server.server import Server


if __name__ == "__main__":

    # GUI option
    if len(argv) == 1:
        guiw = Tk()
        gui = GUI(guiw)
        gui.mainloop()

    # CLI option
    elif len(argv) == 2:
        try:
            # load server config from server.yaml
            with open('server.yaml', 'r') as configFile: 
                conf = load(configFile.read(), Loader)
            if conf:
                # start the server
                s = Server(conf['host'], conf['port'])
                s.start()
        except Exception as confERR: 
            print(f'\nserver.yaml must contain:\n\thost: 0.0.0.0\n\tport: 6400\n\n{confERR}')
