from _thread import start_new_thread
import pygame

# local import
from .models.board import Board
from .models.player import Player
from .network.network import Network


class Client:

    """GUI interface for online-TicTacToe game

    :param server_address: running server address (host, port)
    :type server_address: tuple
    :param v: playing value (X | O)
    :type v: str
    """

    def __init__(self, server_address: tuple, v: str):
        # set main pygame screen size
        self.__screen_size = (1000, 500)
        self.__screen = pygame.display.set_mode(self.__screen_size)
        # set screen title
        pygame.display.set_caption("TicTacToe")
        # change display icon
        pygame.display.set_icon(pygame.image.load("src/assets/icon.png"))
        # create board object
        self.__board = Board((500, 500, 500), self.__screen)
        # create network object
        self.__network = Network(*server_address)
        # playing value
        self.__v = v

    def __refresh(self):
        """Redraw the screen and update it"""
        # set background color to black
        self.__screen.fill((0, 0, 0))
        # redraw the board
        self.__board.draw()
        # update the screen
        pygame.display.update()

    def loop(self):
        """Pygame main loop"""
        # connect to the server
        self.__network.connect()
        # start boards state synchronization
        start_new_thread(self.__synchronization, ())
        # run Pygame main loop
        while True:
            # listen to events
            for e in pygame.event.get():
                # close window button event
                if e.type == pygame.QUIT:
                    return
                # select square by mouse event
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    # select square by mouse
                    self.__select_by_mouse()
                # keyboard keydown events
                elif e.type == pygame.KEYDOWN:
                    # set value by enter key
                    if (
                        e.key in (pygame.K_RETURN, pygame.K_SPACE)
                        and self.__board.selected
                        and not self.__board.end
                    ):
                        # set value and get response
                        res = self.__board.set_value(self.__v)
                        # send the value to the enemy
                        self.__network.send((self.__v, self.__board.selected))
                    # change selected square by arrows
                    self.__select_by_arrows(e, self.__board.selected)
                    # quite shortcut
                    if e.key == pygame.K_q:
                        return
            # update the screen
            self.__refresh()

    def __synchronization(self):
        """Synchronize this board with enemy board"""
        while True:
            # receive data
            d = self.__network.recv()
            # check if the enemy connected
            if not d:
                break
            # set received value
            self.__board.selected = d[1][0], d[1][1]
            self.__board.set_value(d[0])

    def __select_by_mouse(self):
        """Select board square by MOUSEBUTTONDOWN event"""
        # get mouse click position
        p = pygame.mouse.get_pos()
        # calculate square (row, column) from mouse position
        left_space = self.__screen_size[0] - self.__screen_size[1]
        if p[0] > left_space:
            self.__board.selected = (
                p[1] // (self.__screen_size[1] // 3),
                (p[0] - left_space) // (self.__screen_size[1] // 3),
            )
        else:
            self.__board.selected = None

    def __select_by_arrows(self, e: pygame.event.Event, pos: tuple):
        """changed selected square by arrows

        :param e: pygame event
        :type e: pygame.event.Event
        :param pos: current position
        :type pos: tuple
        """
        # set row, column change value
        r, c = 0, 0
        if e.key == pygame.K_UP or e.key == pygame.K_w:
            r = -1
        elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
            r = 1
        elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
            c = 1
        elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
            c = -1
        # check if there's selected square
        if pos:
            # move to the next position
            pos = (pos[0] + r, pos[1] + c)
            if -1 < pos[0] < 3 and -1 < pos[1] < 3:
                self.__board.selected = pos
