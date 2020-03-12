from _thread import start_new_thread
from tkinter import Tk, Frame, Button, Label, messagebox
from yaml import load, Loader
from re import findall

# local import
from server.server import Server


class GUI(Frame): 

    """Server GUI class

    :param parent: parent screen
    :type parent: tkinter.Tk
    """

    def __init__(self, parent: Tk = None): 
        super().__init__(parent)
        self.__parent = parent 
        self.pack()
        self.__init_widgets()
        self.__server = Server(None, None)

    def __start(self):
        """Start the server"""
        # check if the server already running
        if self.__server.run:
            messagebox.showwarning("Warning", "The server already started!")
            return
        else: 
            try:
                # load server config from server.yaml
                with open('server.yaml', 'r') as configFile: 
                    conf = load(configFile.read(), Loader)
                # set host regex pattern
                hostregex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
                # validate host and port
                if findall(hostregex, conf['host']) and 1 <= conf['port'] <= 65535:
                    # set server host and port
                    self.__server.host, self.__server.port = conf['host'], conf['port']
                    # start the server
                    start_new_thread(self.__server.start, ())
                    messagebox.showinfo("Success", f"The server is running at\nHost: {conf['host']}\nPort: {conf['port']}")
                else:
                    messagebox.showerror("Invalid address", "Host must be IPv4 0.0.0.0 - 255.255.255.255\nPort number must be between 1 and 65535")
            except Exception as confERR:
                messagebox.showerror("Config error", f'\nserver.yaml must contain:\n\thost: 0.0.0.0\n\tport: 6400\n\n{confERR}')

    def __stop(self): 
        """Stop the server"""
        if self.__server.run:
            self.__server.stop()
            messagebox.showwarning("stopped", "The server has been stopped!")
            exit(0)

    def __init_widgets(self): 
        """Init GUI widgets
        """
        # change title 
        self.winfo_toplevel().title("TicTacToe server")
        # set window size to 500x200
        self.winfo_toplevel().geometry("300x125")
        # set resizability to False
        self.winfo_toplevel().resizable(False, False)
        # space
        Label(self, text="").pack()
        # start button
        Button(self, text="Start", width=16, height=1, bg="green", command=self.__start).pack()
        # space
        Label(self, text="").pack()
        # stop button
        Button(self, text="Stop & Exit", width=16, height=1, bg="red", command=self.__stop).pack()
        # space
        Label(self, text="").pack()
