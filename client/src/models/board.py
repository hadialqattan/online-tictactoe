from time import sleep
import pygame

# local import
from base.base import GUIBase
from tictactoe.tictactoe import TicTacToe


class Board(GUIBase):

    """TicTacToe board

    :param screen: pygame screen
    :type screen: pygame.Surface
    """

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        # init game board
        self.__board = [["" for i in range(3)] for j in range(3)]
        # create squares list
        self.__squares = [
            [Square((r, c), self.screen) for r in range(3)] for c in range(3)
        ]
        self.__selected = None
        self.__end = False

    @property
    def board(self) -> list:
        """board property (getter)"""
        return self.__board

    @property
    def selected(self) -> tuple:
        """selected property (getter)"""
        return self.__selected

    @selected.setter
    def selected(self, pos: tuple):
        """selected property (setter) & refresh squares

        :param pos: selected square position (row, column)
        :type pos: tuple
        """
        # clear previous selection
        if self.__selected != None:
            self.__squares[self.__selected[0]][self.__selected[1]].selected = False
        if pos and not self.__end:
            # select new square
            self.__selected = pos
            self.__squares[self.__selected[0]][self.__selected[1]].selected = True
        else:
            # set selected to None if pos out of board
            self.__selected = None

    @property
    def end(self) -> bool:
        """end property (getter)"""
        return self.__end

    @end.setter
    def end(self, v: bool):
        """end property (setter)

        :param v: end value
        :type v: bool
        """
        self.__end = v

    def board_reset(self, r: str):
        """Reset the board

        :param r: game result
        :type r: str
        """
        # sleep before show
        sleep(0.5)
        # start end show
        # set show text
        if r == "w":
            txt = ["YOU", "WON", ["Tic", "Tac", "Toe"]]
        elif r == "l":
            txt = ["YOU", "LOS", "T!!"]
        else:
            txt = ["TIC", "TAC", "TOE"]
        # show text with delay
        for r in range(3):
            for c in range(3):
                self.__squares[r][c].value = txt[r][c]
                sleep(0.20)
        # delay before hide the text
        sleep(1)
        # reset board
        self.__board = [["" for i in range(3)] for j in range(3)]
        # reset squares
        for i in self.__squares:
            for s in i:
                s.reset()
        # enable playing events
        self.__end = False

    def set_value(self, v: str) -> str:
        """set square value

        :param v: value to set (X | O)
        :type v: str
        :returns: winner (x, o) || full (f) || False
        :rtype: str
        """
        # handle none selected value
        if self.__selected:
            # get selected square
            r, c = self.__selected
            # check if the square empty
            if not self.__squares[r][c].value and not self.__end:
                self.__squares[r][c].value = v
                self.__board[r][c] = v
                # get winner
                w = TicTacToe.whoWinner(self.__board)
                # check if there's a winner
                if w and w != ("F", ()):
                    self.__set_win_squares(w)
                elif w == ("F", ()):
                    self.__end = True
                return w
        return ()

    def __set_win_squares(self, w: list):
        """Set win squares

        :param w: win line
        :param w: list
        """
        # end the game
        self.__end = True
        # rows
        if w[1][1] == 0:
            for i in range(3):
                self.__squares[w[1][0]][i].win = True
        # columns
        elif w[1][1] == 1:
            for i in range(3):
                self.__squares[i][w[1][0]].win = True
        # diagonal
        elif w[1][1] == 2:
            if w[1][0] == 0:
                # (0,0), (1,1), (2,2) line
                for i in range(3):
                    self.__squares[i][i].win = True
            else:
                # (0,2), (1,1), (2,0) line
                for i in range(3):
                    self.__squares[i][abs(i - 2)].win = True

    def draw(self):
        """Draw board"""
        # Draw squares
        # iterate over all rows
        for r in range(3):
            # iterate over all columns
            for c in range(3):
                # draw square value
                self.__squares[c][r].draw()
        # Draw lines
        # set space between squares
        space = 166
        # drow 2 lines HvV
        for r in range(1, 3):
            # draw horizontal line (screen, (color), (start_pos), (end_pos), width)
            pygame.draw.line(
                self.screen,
                (72, 234, 54),
                (260, r * space),
                (740, r * space),
                3,
            )
            # draw vertical line (screen, (color), (start_pos), (end_pos), width)
            pygame.draw.line(
                self.screen,
                (72, 234, 54),
                (r * space + 250, 15),
                (r * space + 250, 485),
                3,
            )
        # frame
        pygame.draw.rect(self.screen, (72, 234, 54), ((250, 0), (500, 500)), 3)


class Square(GUIBase):

    """TicTacToe board square

    :param pos: square position (row, column)
    :type pos: tuple
    :param screen: pygame screen
    :type screen: pygame.Surface
    """

    def __init__(self, pos: tuple, screen: pygame.Surface):
        super().__init__(screen)
        self.__pos = pos
        self.__selected = False
        self.__win = False
        self.__value = ""

    @property
    def selected(self) -> tuple:
        """selected property (getter)"""
        return self.__selected

    @selected.setter
    def selected(self, v: bool):
        """selected property (setter)

        :param v: selected value
        :type v: bool
        """
        self.__selected = v

    @property
    def win(self) -> tuple:
        """win property (getter)"""
        return self.__win

    @win.setter
    def win(self, v: bool):
        """win property (setter)

        :param v: win value
        :type v: bool
        """
        self.__win = v

    @property
    def value(self) -> str:
        """value property (getter)"""
        return self.__value

    @value.setter
    def value(self, v: str):
        """selected property (setter)
        :param v: value (X | O)
        :type v: str
        """
        self.__value = v

    def reset(self):
        """Reset square"""
        self.__value = ""
        self.__win = False
        self.__selected = False

    def draw(self):
        """Draw square value"""
        # set space between squares
        space = 166
        # set actuall square potition on the screen
        pos = self.__pos[0] * space + 250, self.__pos[1] * space
        # draw bold outline around selected square
        if self.__selected:
            # draw rectangle (fill)
            pygame.draw.rect(self.screen, (10, 30, 0), (pos, (space, space)))
        if self.__win:
            # draw win rectangle (fill)
            pygame.draw.rect(self.screen, (60, 80, 50), (pos, (space, space)))
        # check for unempty squares
        if self.__value != "":
            # draw square value
            self._type(self.__value, (72, 234, 54), pos, 60, space)

    def _type(self, txt: str, rgb: tuple, pos: tuple, fsize: int, space: int):
        """Draw string on the surface screen (override)

        :param txt: text to draw
        :type txt: str
        :param rgb: text color
        :type rgb: tuple
        :param pos: postition to draw
        :type pos: tuple
        :param fsize: font size
        :type fsize: int
        :param space: space between squares
        :type space: int
        """
        # create font object
        font = pygame.font.Font("assets/comfortaa-font/Comfortaa-Regular.ttf", fsize)
        # render font object with text
        v = font.render(txt, 1, rgb)
        # draw font obj on the surface
        self.screen.blit(
            v,
            (
                int(pos[0] + ((space / 2) - (v.get_width() / 2))),
                int(pos[1] + ((space / 2) - (v.get_height() / 2))),
            ),
        )
