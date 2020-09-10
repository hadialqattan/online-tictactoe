from socket import socket, error, AF_INET, SOCK_STREAM
from _thread import start_new_thread
from pickle import loads, dumps


class Network:

    """TicTacToe client-side

    :param host: server host
    :type host: str
    :param port: server port
    :type port: int
    """

    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__socket = None

    def connect(self) -> bool:
        """connect to the server

        :returns: connection status
        :rtype: bool
        """
        try:
            self.__socket = socket(AF_INET, SOCK_STREAM)
            # connect to the server
            self.__socket.connect((self.__host, self.__port))
            return True
        except error as cErr:
            print(f"Cannot connect to server:\n{cErr}")
            self.__socket.close()
            return False

    def send(self, data: tuple):
        """Send TicTacToe movement object

        :param data: TicTacToe movement (Value, (posx, posy)) ex: (X, (0, 0))
        :type data: tuple
        """
        try:
            self.__socket.sendall(dumps(data))
            return True
        except error as sendErr:
            print(f"Cannot send data to server:\n{sendErr}")
            self.__socket.close()
            return False

    def recv(self) -> tuple:
        """Receive data from server

        :returns: TicTacToe movement obj (value, (posx, posy))
        :rtype: tuple
        """
        try:
            return loads(self.__socket.recv(64))
        except error as recvErr:
            print(f"Cannot recv data from server:\n{recvErr}")
            self.__socket.close()
            return False
