import pygame

# local import
from base.base import GUIBase


class LeftPanel(GUIBase):

    """Left control panel

    :param screen: pygame screen
    :type screen: pygame.Surface
    :param connected: connection status (default False)
    :type connected: bool
    :param v: playing value (X | O) (default X)
    :type v: str
    """

    def __init__(self, screen: pygame.Surface, connected: bool = False, v: str = "X"):
        super().__init__(screen)
        self.__connection_control = ConnectionControl(self.screen, connected)
        self.__game_state = GameState(self.screen, v)
        self.ai_control = AIControl(self.screen)

    @property
    def connected(self) -> bool:
        """connected property (getter)"""
        return self.__connection_control.connected

    @connected.setter
    def connected(self, isconnected: bool):
        """connected property (setter)
        
        :param isconnected: connection status
        :type isconnected: bool
        """
        self.__connection_control.connected = isconnected

    @property
    def v(self) -> str:
        """v property (getter)"""
        return self.__game_state.v

    @v.setter
    def v(self, value: str):
        """v property (setter)

        :param value: playing character (X | O)
        :type value: str
        """
        self.__game_state.v = value

    @property
    def lvl(self) -> str:
        """lvl property (getter)"""
        return self.ai_control.lvl

    @lvl.setter
    def lvl(self, value: str):
        """lvl property (setter)

        :param value: playing character (X | O)
        :type value: str
        """
        if 1 <= self.lvl <= 4:
            self.ai_control.lvl = value

    @property
    def isai(self):
        """isai property (getter)"""
        return self.ai_control.isai

    @isai.setter
    def isai(self, value: bool):
        """isai property (setter)

        :param value: isai value
        :type value: bool
        """
        self.ai_control.isai = value

    def draw(self):
        """Draw the left panel on the screen"""
        # draw main frame
        # draw rectangle (frame)
        pygame.draw.rect(self.screen, (72, 234, 54), ((0, 0), (250, 500)), 3)
        # draw tilte
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, 5), (240, 73)))
        self._type("TicTacToe", (0, 0, 0), (20, 20), 38, True)
        # connection subframe
        self.__connection_control.draw()
        # game stutas subframe
        self.__game_state.draw()
        # ai subframe
        self.ai_control.draw()


class ConnectionControl(GUIBase):

    """Connection control class 
    
    :param screen: pygame screen
    :type screen: pygame.Surface
    :param connected: connection status
    :type connected: bool
    """

    def __init__(self, screen: pygame.Surface, connected: bool):
        super().__init__(screen)
        self.connected = connected

    def draw(self):
        """Draw connection control subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, 81), (239, 83)), 2)
        # draw title
        self._type("Connect to server", (72, 234, 54), (27, 87), 20)
        # set color and text based on connection status
        if self.connected:
            rgb = (72, 234, 54)
            txt = "Connected"
            pos = (41, 108)
        else:
            rgb = (234, 72, 54)
            txt = "Disconnected"
            pos = (25, 108)
        # draw connection status bar
        pygame.draw.rect(self.screen, rgb, ((10, 86), (230, 74)))
        # type connection status text
        self._type(txt, (0, 0, 0), pos, 28)


class AIControl(GUIBase):

    """AI control class

    :param screen: pygame screen
    :type screen: pygame.Surface
    """

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.lvl = 1
        self.isai = False
        self.__buttons = [
            Button(
                self.__play_with_ai,
                (),
                (-5, 4),  # text space
                (24, 234),  # pos
                "Play with AI",  # innertxt
                20,  # fontsize
                (202, 40),  # size
                self.screen,
            ),
            Button(
                self.__play_online,
                (),
                (-5, 5),  # text space
                (24, 280),  # pos
                "Play online",  # innertxt
                20,  # fontsize
                (202, 40),  # size
                self.screen,
            ),
        ]

    @property
    def buttons(self):
        """buttons property (getter)"""
        return self.__buttons

    def __play_with_ai(self):
        """Set isai to True"""
        self.isai = True

    def __play_online(self):
        """Set isai to False"""
        self.isai = False

    def draw(self):
        """Draw AI control subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, 168), (239, 166)), 2)
        # draw the fill
        pygame.draw.rect(self.screen, (72, 234, 54), ((9, 172), (231, 158)))
        # draw tilte
        self._type(f"AI engine level {self.lvl}", (0, 0, 0), (20, 188), 26)
        # draw buttons
        for b in self.__buttons:
            b.draw(self.isai)


class GameState(GUIBase):

    """Game state class 

    :param screen: pygame screen
    :type screen: pygame.Surface
    :param v: playing value (X | O)
    :type v: str
    """

    def __init__(self, screen: pygame.Surface, v: str):
        super().__init__(screen)
        self.v = v

    def draw(self):
        """Draw game state subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, 338), (239, 156)), 2)
        # dreaw value in filled square
        pygame.draw.rect(self.screen, (72, 234, 54), ((10, 343), (230, 147)))
        # draw the letter (X | O)
        l = self.v.upper()
        pos = (72, 341) if l == "X" else (56, 342)
        self._type(l, (0, 0, 0), pos, 150)


class Button(GUIBase):

    """Button class 
    :param target: target function to start onclick
    :type target: function
    :param _args: target function args
    :type _args: tuple
    :param s: left, top space
    :type s: tuple
    :param pos: button start pos
    :type pos: tuple
    :param innertxt: inner text
    :type innertxt: str
    :param fontsize: innertxt font size
    :type fontsize: int
    :param size: button size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    """

    def __init__(
        self,
        target,
        _args: tuple,
        s: tuple,
        pos: tuple,
        innertxt: str,
        fontsize: int,
        size: tuple,
        screen: pygame.Surface,
    ):
        super().__init__(screen)
        self.size = size
        self.__target = target
        self.__args = _args
        self.__pos = pos
        self.__innertxt = innertxt
        self.__fontsize = fontsize
        self.__w = 1
        self.__s = s
        self.__click_range = (
            range(self.__pos[0], self.__pos[0] + self.size[0] + 1),
            range(self.__pos[1], self.__pos[1] + self.size[1] + 1),
        )

    @property
    def innertxt(self):
        """innertxt property (getter)"""
        return self.__innertxt

    @property
    def click_range(self):
        """click range property"""
        return self.__click_range

    def click(self, args: tuple = ()):
        """Handle click event
        
        :param args: target function args if the args isn't constant
        :type args: tuple
        """
        # call the traget
        if self.__args:
            return self.__target(self.__args)
        elif args:
            return self.__target(*args)
        else:
            return self.__target()

    def draw(self, ai: bool):
        """Draw button rect
        
        :param ai: play with ai or online
        :type ai: bool
        """
        # Draw main frame
        pygame.draw.rect(self.screen, (0, 0, 0), (self.__pos, self.size), 2)
        # choose color basend on ai param
        if (ai and self.__innertxt == "Play with AI") or (
            not ai and not self.__innertxt == "Play with AI"
        ):
            fill = (72, 234, 54)
        else:
            fill = (234, 72, 54)
        # draw rectangle (fill)
        pygame.draw.rect(
            self.screen,
            fill,
            (
                (self.__pos[0] + 2, self.__pos[1] + 2),
                (self.size[0] - 3, self.size[1] - 3),
            ),
        )
        # set inner text
        self._type(
            self.__innertxt,
            (0, 0, 0),
            (
                self.__pos[0] + self.size[0] // 4 + self.__s[0],
                self.__pos[1] + self.size[1] // 8 + self.__s[1],
            ),
            self.__fontsize,
        )
