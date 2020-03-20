from abc import abstractmethod
import pygame


class GUIBase:

    """Base GUI class
    
    :param screen: pygame screen
    :type screen: pygame.Surface 
    """

    def __init__(self, screen: pygame.Surface):
        self.__screen = screen

    @property
    def screen(self):
        """screen property (getter)"""
        return self.__screen

    @abstractmethod
    def draw(self):
        """Draw function (must override)"""
        pass

    def _type(self, txt: str, rgb: tuple, pos: tuple, fsize: int, b: bool = False):
        """Draw string on the surface screen
        
        :param txt: text to draw
        :type txt: str
        :param rgb: text color
        :type rgb: tuple
        :param pos: postition to draw
        :type pos: tuple
        :param fsize: font size
        :type fsize: int
        :param b: bold font
        :type b: bool
        """
        # create font object
        t = "Bold" if b else "Regular"
        font = pygame.font.Font(f"assets/comfortaa-font/Comfortaa-{t}.ttf", fsize)
        # render font object with text
        v = font.render(txt, 1, rgb)
        # draw font obj on the surface
        self.__screen.blit(v, pos)
