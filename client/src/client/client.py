from _thread import start_new_thread
from time import sleep
import pygame

# local import
from models.board import Board
from network.network import Network
from models.left_panel import LeftPanel


class Client:

    """GUI interface for online-TicTacToe game

    :param server_address: running server address (host, port)
    :type server_address: tuple
    """

    def __init__(self, server_address: tuple):
        # set main pygame screen size
        self.__screen_size = (750, 500)
        self.__screen = pygame.display.set_mode(self.__screen_size)
        # set screen title
        pygame.display.set_caption("TicTacToe")
        # change display icon
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))
        # create network object
        self.__network = Network(*server_address)
        # create board object
        self.__board = Board((500, 500, 250), self.__screen)
        # create leftpanel object
        self.__left_panel = LeftPanel((250, 500), self.__screen)
        # playing turn constrain
        self.__turn = False
        # sounds init
        self.__sounds = {
            'X': pygame.mixer.Sound('assets/sounds/x.wav'), 
            'O': pygame.mixer.Sound('assets/sounds/o.wav'), 
            'win': pygame.mixer.Sound('assets/sounds/win.wav'), 
            'lose': pygame.mixer.Sound('assets/sounds/lose.wav'), 
        }

    @property
    def v(self) -> str: 
        """v property (getter)"""
        return self.__left_panel.v

    @v.setter
    def v(self, value: str): 
        """v property (setter)

        :param value: playing character (X | O)
        :type value: str
        """
        if value in ('X', 'O'):
            self.__left_panel.v = value
            self.__turn = value == 'X'
        else: 
            raise ValueError('Playing value must be either X or O')

    def __turn_reverser(self): 
        """self.__turn reverser"""
        self.__turn = not self.__turn

    def __refresh(self):
        """Redraw the screen and update it"""
        # set background color to black
        self.__screen.fill((0, 0, 0))
        # redraw the board
        self.__board.draw()
        # redraw the left panel
        self.__left_panel.draw()
        # update the screen
        pygame.display.update()

    def loop(self):
        """Pygame main loop"""
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
                        and self.__turn
                    ):
                        # play
                        self.__play()
                    # change selected square by arrows
                    self.__select_by_arrows(e, self.__board.selected)
                    # quite shortcut
                    if e.key == pygame.K_q:
                        return
            # update the screen
            self.__refresh()        

    def __synchronization(self):
        """Create connection and synchronize the board with enemy board"""
        try:
            while True:
                # receive data
                d = self.__network.recv()
                # check if the server still running
                if not d:
                    raise ConnectionRefusedError('')
                # play
                self.__play(d)
        except:
            self.__left_panel.connected = False
            self.__board.board_reset('d')
            # reconnect to the server 
            while True:
                sleep(1)
                # try to connect
                self.__left_panel.connected = self.__network.connect()
                # set playing vlaue
                if self.__left_panel.connected:
                    self.v = self.__network.recv()
                    # start boards state synchronization
                    start_new_thread(self.__synchronization, ())
                # if connection success exist from this thread
                if self.__left_panel.connected: 
                    break

    def __play(self, d: tuple = ()):
        """play event handler
        
        :param d: additional data (value, (row, column)) if from server else ()
        :type d: tuple
        """
        if not d and not self.__left_panel.connected:
            return
        if not d: 
            # send the value to the enemy
            self.__network.send((self.__left_panel.v, self.__board.selected))
            v, s = self.__left_panel.v, 'win'
        else:
            # select recv square
            self.__board.selected = d[1][0], d[1][1]
            v, s = d[0], 'lose'
        # set square value and get response
        res = self.__board.set_value(v)
        # reverse turn
        self.__turn_reverser()
        # play X or O sound
        self.__sounds[v].play()
        # check for win/lose
        if v in res: 
            # play win/lose sound
            self.__sounds[s].play()
            # start end show and restart the board
            start_new_thread(self.__board.board_reset, (s[0],))
        elif 'F' in res: 
            # start end show and restart the board
            start_new_thread(self.__board.board_reset, ('d',))
            # change playing value (X | O)
            self.__left_panel.v = [i for i in ('X', 'O') if i != self.__left_panel.v][0]

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
