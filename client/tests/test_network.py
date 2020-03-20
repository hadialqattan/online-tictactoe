from unittest import TestCase
from _thread import start_new_thread
from time import sleep

# local import
from src.network.network import Network
from tests.server_class import Server


class Test_Network(TestCase):

    """network.network.Network unit tests class"""

    def __init__(self, *args, **kwargs):
        super(Test_Network, self).__init__(*args, **kwargs)
        self.host, self.port = "127.0.0.1", 6400
        self.server = Server(self.host, self.port)
        # start the server
        start_new_thread(self.server.start, ())
        # create clients
        self.client1 = Network(self.host, self.port)
        self.client2 = Network(self.host, self.port)

    def test_01_create_connection(self):
        """Create client and connect it to the server"""
        res1 = self.client1.connect()
        res2 = self.client2.connect()
        assert res1 == True
        assert res2 == True

    def test_02_recv_playing_values(self):
        """recv playing value from server 'X' || 'O'"""
        self.client1.connect()
        self.client2.connect()
        res1 = self.client1.recv()
        res2 = self.client2.recv()
        assert res1 == "O"
        assert res2 == "O"

    def test_03_send_recv_data(self):
        """Send data from client1 and recv data from client2"""
        self.client1.connect()
        self.client2.connect()
        self.client1.recv()
        self.client2.recv()
        req = self.client1.send(("X", (0, 0)))
        res = self.client2.recv()
        assert req == True
        assert res == ("X", (0, 0))

    def test_04_stop_server(self):
        """Stop the server"""
        self.server.stop()
        sleep(2)
        assert self.server.run == False
