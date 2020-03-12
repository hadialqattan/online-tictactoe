import pygame

# local import
from base.base import GUIBase


class LeftPanel(GUIBase): 

    """Left control panel

    :param size: screen size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    :param connected: connection status (default False)
    :type connected: bool
    :param v: playing value (X | O) (default X)
    :type v: str
    """

    def __init__(self, size: tuple, screen: pygame.Surface, connected: bool = False, v: str = 'X'):
        super().__init__(size, screen)
        self.__connection_control = ConnectionControl(self.size, self.screen, connected)
        self.__ai_control = AIControl(self.size, self.screen)
        self.__game_state = GameState(self.size, self.screen, v)

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

    def draw(self):
        """Draw the left panel on the screen"""
        # draw main frame
        # draw rectangle (frame)
        pygame.draw.rect(self.screen, (72, 234, 54), ((0, 0), self.size), 3)
        # draw tilte 
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, 5), (self.size[0]-10, (self.size[1] // 6)-10)))
        self._type("TicTacToe", (0, 0, 0), (20, 20), 38, True)
        # connection subframe
        self.__connection_control.draw()
        # ai subframe
        self.__ai_control.draw()
        # game stutas subframe
        self.__game_state.draw()


class ConnectionControl(GUIBase): 

    """Connection control class 
    
    :param size: screen size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    :param connected: connection status
    :type connected: bool
    """

    def __init__(self, size: tuple, screen: pygame.Surface, connected: bool): 
        super().__init__(size, screen)
        self.connected = connected

    def draw(self): 
        """Draw connection control subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, (self.size[1] // 6)-2), (self.size[0]-11, self.size[1] // 6)), 2)
        # draw title
        self._type('Connect to server', (72, 234, 54), (27, (self.size[1] // 6)+4), 20)
        # set color and text based on connection status
        if self.connected: 
            rgb = (72, 234, 54)
            txt = 'Connected'
            pos = (self.size[0]//6, (self.size[1] // 5)+8)
        else: 
            rgb = (234, 72, 54) 
            txt = 'Disconnected'
            pos = (self.size[0]//10, (self.size[1] // 5)+8)
        # draw connection status bar
        pygame.draw.rect(self.screen, rgb, ((10, (self.size[1] // 6)+3), (self.size[0]-20, self.size[1] // 6 - 9)))
        # type connection status text
        self._type(txt, (0, 0, 0), pos, 28)


class AIControl(GUIBase): 

    """AI control class

    :param size: screen size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    """

    def __init__(self, size: tuple, screen: pygame.Surface): 
        super().__init__(size, screen)

    @property
    def buttons(self):
        """buttons property (getter)"""
        return self.__buttons

    def draw(self):
        """Draw AI control subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, (self.size[1] // 3)+2), (self.size[0]-11, self.size[1] // 3)), 2)
        # draw tilte
        self._type('AI engine level', (72, 234, 54), (44, (self.size[1] // 3)+8), 20)


class GameState(GUIBase): 

    """Game state class 

    :param size: screen size (width, height)
    :type size: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    :param v: playing value (X | O)
    :type v: str
    """

    def __init__(self, size: tuple, screen: pygame.Surface, v: str): 
        super().__init__(size, screen)
        self.v = v

    def draw(self): 
        """Draw game state subframe"""
        # draw the frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((5, (self.size[1]-(self.size[1]//3)+4)), (self.size[0]-11, (self.size[1] // 3)-10)), 2)


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

    def __init__(self, target, _args: tuple, s: tuple, pos: tuple, innertxt: str, fontsize: int,size: tuple, screen: pygame.Surface): 
        super().__init__(size, screen)
        self.__target = target 
        self.__args = _args
        self.__pos = pos
        self.__innertxt = innertxt
        self.__fontsize = fontsize
        self.__fill = (0, 0, 0)
        self.__w = 1
        self.__s = s
        self.__click_range = (
            range(self.__pos[0], self.__pos[0] + self.size[0] + 1), 
            range(self.__pos[1], self.__pos[1] + self.size[1] + 1)
        )

    @property
    def innertxt(self):
        """innertxt property (getter)"""
        return self.__innertxt

    @property
    def click_range(self):
        """click range property"""
        return self.__click_range

    @property
    def reset(self):
        """Reset button style"""
        self.__fill = (0, 0, 0)
        self.__w = 1

    def click(self, args: tuple = ()):
        """Handle click event
        
        :param args: target function args if the args isn't constant
        :type args: tuple
        """
        # change button style
        self.__fill = (30, 50, 20)
        self.__w = 2
        # call the traget
        if self.__args:
            return self.__target(self.__args)
        elif args:
            return self.__target(*args)
        else:
            return self.__target()
    
    def draw(self):
        """Draw button rect"""
        # Draw main frame
        # draw rectangle (frame)
        pygame.draw.rect(
            self.screen, (72, 234, 54), (self.__pos, self.size), self.__w,
        )
        # set inner text
        self._type(
            self.__innertxt,
            (72, 234, 54),
            (
                self.__pos[0] + self.size[0] // 4 + self.__s[0],
                self.__pos[1] + self.size[1] // 8 + self.__s[1],
            ),
            self.__fontsize,
        )
