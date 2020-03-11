from _thread import start_new_thread
import socket 


class Network: 

    """TicTacToe client-side
    """

    def __init__(self, host: str, port: int): 
        self.__host = host
        self.__port = port 
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self): 
        """connect to the server"""
        try:
            # connect to the server 
            self.__socket.connect((self.__host, self.__port))
        except socket.error as cErr: 
            print(f"Cannot connect to server:\n{cErr}")
            exit(1)

    def send(self, data):
        ndata = self.strf(data)
        self.__socket.sendall(ndata.encode())
    
    def recv(self):
        d = self.__socket.recv(1024).decode()
        return self.formatter(d)
        
    def formatter(self, data):
        return (data[0], (int(data[1]), int(data[2])))

    def strf(self, data): 
        return ''.join([data[0], str(data[1][0]), str(data[1][1])])
"""
if __name__ == "__main__":
    c = Network('127.0.0.1', 6400)
    c.send()"""
