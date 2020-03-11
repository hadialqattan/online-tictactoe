from socket import socket, error, AF_INET, SOCK_STREAM
from _thread import start_new_thread
from sys import argv


class Server: 

    """TicTacToe server-side

    :param host: server host IP
    :type host str
    :param port: server port
    :type port: int
    """

    def __init__(self, host: str, port: int): 
        self.__host = host
        self.__port = port
        self.__clients = []
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__run = False

    @property
    def host(self) -> str: 
        """host property (getter)"""
        return self.__host

    @host.setter
    def host(self, value: str): 
        """host property (setter)

        :param value: host value
        :type value: str
        """
        self.__host = value

    @property
    def port(self) -> int: 
        """port property (getter)"""
        return self.__port

    @port.setter 
    def port(self, value: int): 
        """port property (setter)

        :param value: port value
        :type value: int
        """
        self.__port = value

    @property
    def run(self) -> bool: 
        """run property (getter)"""
        return self.__run
        
    def start(self): 
        """Start the server"""
        with self.__socket:
            try:
                self.__run = True
                # try to run the server 
                self.__socket.bind((self.__host, self.__port))
                # listen for connections
                self.__socket.listen(2)
                # start connection loop
                self.__connection_loop()
            except error as bErr:
                print(f"Server error:\n{bErr}")
                exit(1)

    def stop(self): 
        """Stop the server"""
        self.__run = False

    def __connection_loop(self):
        """Main connection loop"""
        # start the loop
        while self.__run:
            # wait for connection
            conn, addr = self.__socket.accept()
            # add the client in clients list
            self.__clients.append(conn)
            # start new client thread
            start_new_thread(self.__client_thread, (conn,))

    def __client_thread(self, conn: socket):
        """Client thread to handle (send/recv) operations

        :param conn: client connection
        :type conn: socket.socket
        """
        with conn as c:
            # start client loop
            while self.__run:
                try: 
                    # receive data from client
                    data = c.recv(1024).decode()
                    # check if the client still connected
                    if not data:
                        break
                    # send the data to another client
                    for client in self.__clients:
                        # block data sending to this connection
                        if client != c:
                            # send the data
                            client.sendall(str.encode(data))
                except error:
                    break
        # remove the client from clients list
        try:
            self.__clients.remove(conn)
        except ValueError: 
            pass
