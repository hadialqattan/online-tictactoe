from _thread import start_new_thread
from tkinter import Tk, Frame, Label, Entry, Button, StringVar, messagebox
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

    def __start(self, host: StringVar, port: StringVar):
        """Start the server

        :param host: server host
        :type host: tkinter.StringVar
        :param port: server port
        :type port: tkinter.StringVar
        """
        # check if the server already running
        if self.__server.run:
            messagebox.showerror("Error", "The server already started!")
            return
        else: 
            # get str host
            host = host.get() 
            # get int port or 0 if None
            port = int(port.get()) if port.get() else 0
            # set host regex pattern
            hostregex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
            # validate host and port
            if findall(hostregex, host) and 1 <= port <= 65535:
                # set server host and port 
                self.__server.host, self.__server.port = host, port
                # start the server
                start_new_thread(self.__server.start, ())
                messagebox.showinfo("Success", f"The server is running at\nHost: {host}\nPort: {port}")
            else:
                messagebox.showerror("Invalid input", "Host must be IPv4 0.0.0.0 - 255.255.255.255\nPort number must be between 1 and 65535")

    def __stop(self): 
        """Stop the server"""
        self.__server.stop()
        messagebox.showwarning("stopped", "The server has been stopped!")
        exit(0)

    def __init_widgets(self): 
        """Init GUI widgets
        """
        # change title 
        self.winfo_toplevel().title("TicTacToe server")
        # set window size to 500x200
        self.winfo_toplevel().geometry("300x250")
        # set resizability to False
        self.winfo_toplevel().resizable(False, False)
        # set text variables
        host = StringVar()
        port = StringVar()
        # space
        Label(self, text="").pack()
        # set server host label
        host_lbl = Label(self, text="Server Host * ")
        host_lbl.pack()
        # set server host entry
        host_entry = Entry(self, textvariable=host)
        host_entry.pack()
        # set server port label
        port_lbl = Label(self, text="Server Port * ")
        port_lbl.pack()
        # set server port entry
        port_entry = Entry(self, textvariable=port)
        port_entry.pack()
        # space
        Label(self, text="").pack()
        # start button
        Button(self, text="Start", width=16, height=1, bg="green", command=lambda: self.__start(host, port)).pack()
        # space
        Label(self, text="").pack()
        # stop button
        Button(self, text="Stop & Exit", width=16, height=1, bg="red", command=self.__stop).pack()
        # space
        Label(self, text="").pack()
