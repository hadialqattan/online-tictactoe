from sys import argv

# GUI option import
if len(argv) == 1: 
    from tkinter import Tk
    # local import
    from gui.GUI import GUI

# CIL option import
elif len(argv) == 3: 
    from re import findall
    # local import
    from server.server import Server


if __name__ == "__main__":
    
    # GUI option
    if len(argv) == 1:
        guiw = Tk()
        gui = GUI(guiw)
        gui.mainloop()

    # CLI option
    elif len(argv) == 3:
        host = argv[1] 
        port = int(argv[2])
        hostregex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
        # validate host and port
        if findall(hostregex, host) and 1 <= port <= 65535:
            s = Server(host, port)
            s.start()
        else: 
            raise Exception("Host must be IPv4 0.0.0.0 - 255.255.255.255\nPort number must be between 1 and 65535")
    else: 
        raise Exception("Usage:\n\t$ python3 main.py host port (for CLI)\n\t$ python3 main.py (for GUI)")
