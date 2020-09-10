from _thread import start_new_thread
from time import sleep
import pygame

# local import
from models.board import Board
from network.network import Network
from models.left_panel import LeftPanel
from tictactoe.tictactoe import TicTacToe


class Client:

    """GUI interface for online-TicTacToe game

    :param server_address: running server address (host, port)
    :type server_address: tuple
    """

    def __init__(self, server_address: tuple):
        # set main pygame screen size -init pygame.Surface-
        self.__screen = pygame.display.set_mode((750, 500))
        # set screen title
        pygame.display.set_caption("TicTacToe")
        # change display icon
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))
        # create network object
        self.__network = Network(*server_address)
        # create board object
        self.__board = Board(self.__screen)
        # create leftpanel object
        self.__left_panel = LeftPanel(self.__screen)
        # playing turn constrain
        self.__turn = False
        # tictactoe obg
        self.__ai = TicTacToe(1)
        self.__reverse = "X"
        # sounds init
        pygame.mixer.init()
        self.__sounds = {
            "X": pygame.mixer.Sound("assets/sounds/x.wav"),
            "O": pygame.mixer.Sound("assets/sounds/o.wav"),
            "w": pygame.mixer.Sound("assets/sounds/win.wav"),
            "l": pygame.mixer.Sound("assets/sounds/lose.wav"),
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
        if value in ("X", "O"):
            self.__left_panel.v = value
            self.__turn = value == "X"  # first turn to X player
            self.__reverse = "X" if value == "O" else "O"
        else:
            raise ValueError("Playing value must be either X or O")

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
                    # press ai buttons
                    self.__ai_buttons()
                # keyboard keydown events
                elif e.type == pygame.KEYDOWN:
                    # set value by enter key
                    if (
                        e.key in (pygame.K_RETURN, pygame.K_SPACE)
                        and self.__board.selected
                        and not self.__board.end
                        and self.__turn
                    ):
                        if not self.__left_panel.isai:
                            # play
                            self.__play()
                        else:
                            # set player move
                            res = self.__play_with_ai(False)
                            if res:
                                # get ai response
                                self.__play_with_ai(True)
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
                    raise ConnectionRefusedError("")
                if not self.__left_panel.isai:
                    # play
                    self.__play(d)
        except:
            self.__left_panel.connected = False
            # start end show and reset the board
            start_new_thread(self.__board.board_reset, ("d",))
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
            v, s = self.__left_panel.v, "win"
        else:
            # select recv square
            self.__board.selected = d[1][0], d[1][1]
            v, s = d[0], "lose"
        # set square value and get response
        res = self.__board.set_value(v)
        # reverse turn
        self.__turn_reverser()
        # play X or O sound
        self.__sounds[v].play()
        # check for win/lose
        if v in res:
            s = s[0]
        elif "F" in res:
            s = "d"
        # start end show and reset the board
        if s in ("l", "w"):
            # play win/lose sound
            self.__sounds[s].play()
        if res:
            start_new_thread(self.__board.board_reset, (s,))
            # change playing value (X | O)
            self.v = self.__reverse

    def __play_with_ai(self, ai: bool):
        """play with ai event handler

        :param ai: is ai turn
        :type ai: bool
        """
        if not ai:
            # send the value to the enemy
            v, s = self.__left_panel.v, "win"
        else:
            # select recv square
            aires = self.__ai.ai(self.__board.board, self.__reverse)
            if aires:
                self.__board.selected = aires
                v, s = self.__reverse, "lose"
        try:
            # set square value and get response
            res = self.__board.set_value(v)
            # reverse turn
            self.__turn_reverser()
            # play X or O sound
            self.__sounds[v].play()
            # check for win/lose
            if v in res:
                s = s[0]
            elif "F" in res:
                s = "d"
            # start end show and reset the board
            if s in ("l", "w"):
                # play win/lose sound
                self.__sounds[s].play()
            if res:
                # start end show and reset the board
                start_new_thread(self.__board.board_reset, (s[0],))
                # change playing value (X | O)
                self.v = self.__reverse
                if s == "w" and not ai:
                    # increase AI engine level
                    self.__left_panel.lvl = self.__left_panel.lvl + 1
                    self.__ai.engine = self.__ai.engine + 1
                if self.v == "O":
                    # play ai if x
                    start_new_thread(self.__x_ai, ())
                    return False
            return True
        except UnboundLocalError:
            pass

    def __x_ai(self):
        """first turn for AI"""
        sleep(3.5)
        self.__play_with_ai(True)

    def __ai_buttons(self):
        """Press ai buttons by MOUSEBUTTONDOWN event"""
        # get mouse click position
        p = pygame.mouse.get_pos()
        # iterate over ai buttons
        for b in self.__left_panel.ai_control.buttons:
            # check if the position match b click range
            if p[0] in b.click_range[0] and p[1] in b.click_range[1]:
                # call click event
                b.click()
                # reset the game
                self.v = "X"
                # start end show and reset the board
                start_new_thread(self.__board.board_reset, ("d",))

    def __select_by_mouse(self):
        """Select board square by MOUSEBUTTONDOWN event"""
        # get mouse click position
        p = pygame.mouse.get_pos()
        # calculate square (row, column) from mouse position
        left_space = 250
        if p[0] > left_space:
            self.__board.selected = (
                p[1] // (166),
                (p[0] - left_space) // (166),
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
