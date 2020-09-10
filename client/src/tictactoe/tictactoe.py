from random import randint


class TicTacToe:

    """TicTacToe and win checking class

    :param engine: TicTacToe engine level (1 to 4)
    :type engine: int
    """

    def __init__(self, engine: int):
        self.__engine = engine

    @property
    def engine(self) -> int:
        """engine property (getter)"""
        return self.__engine

    @engine.setter
    def engine(self, lvl: int):
        """engine property (setter)

        :param lvl: engine level (1 to 4)
        :type lvl: int
        """
        if 1 <= self.__engine <= 4:
            self.__engine = lvl

    @staticmethod
    def whoWinner(board: list) -> tuple:
        """Game end checker (check for winner or full board)

        :param board: TicTacToe board
        :type board: list
        :returns: winner (value, (n, type)) ex: ('X', (0, 0)) || ('F', ()) || ()
        :rtype: tuple
        """
        # check horizontal lines
        # iterate over all rows
        for r in range(3):
            # check if all row elements are same
            if len(set(board[r])) == 1 and board[r][0]:
                return board[r][0], (r, 0)
        # check vertical lines
        # zip the board
        zboard = list(zip(*board))
        # iterate over all columns
        for c in range(3):
            # check if columns elements are same
            if len(set(zboard[c])) == 1 and zboard[c][0]:
                return zboard[c][0], (c, 1)
        # delete zboard
        del zboard
        # check diagonal lines
        # set (0,0), (1,1), (2,2) line
        # and (0,2), (1,1), (2,0) line
        r = [[], []]
        for i in range(3):
            r[0].append(board[i][i])
            r[1].append(board[i][abs(i - 2)])
        # check if all lines elements are same
        # iterate over r list
        for i in range(2):
            # check if all elements are same
            if len(set(r[i])) == 1 and r[i][0]:
                return r[i][0], (i, 2)
        # check if the entire board filled
        if all(all(r) for r in board):
            return ("F", ())
        # nothing
        return ()

    def ai(self, board: list, v: str) -> bool:
        """ai player

        :param board: TicTacToe board
        :type board: list
        :param v: computer playing value (X, O)
        :type v: str
        :returns: True if success else False
        :rtype: bool
        """
        # set enemy value
        ev = "O" if v == "X" else "X"
        # get empty positions list
        epos = self.__get_empty(board)
        # check if there's empty position in the board
        if not epos:
            return ()
        # TicTacToe algorithm ---
        # only engine level >=3
        if self.__engine >= 3:
            # empty board (play in random place except the center)
            if len(epos) == 9:
                while True:
                    r, c = epos[randint(0, 8)]
                    if (r, c) != (1, 1):
                        board[r][c] = v
                        return r, c
            # second turn (play on the center if it's empty else corner)
            if len(epos) == 8:
                # check if the center is empty
                if (1, 1) in epos:
                    board[1][1] = v
                    return 1, 1
                # choose corner
                for r, c in epos:
                    if (r + c) % 2 == 0:
                        board[r][c] = v
                        return r, c
        # only engine level >= 2
        if self.__engine >= 2:
            # search for win position (Attack)
            for r, c in epos:
                # test the postision
                board[r][c] = v
                # check if it win pos
                if TicTacToe.whoWinner(board):
                    board[r][c] = v
                    return r, c
                # reset the position
                board[r][c] = ""
            # block enemy win pos (defence)
            for r, c in epos:
                # test the position
                board[r][c] = ev
                if TicTacToe.whoWinner(board):
                    board[r][c] = v
                    return r, c
                # reset the position
                board[r][c] = ""
        # only engine level 4
        if self.__engine == 4:
            # fourth turn (from + positions)
            if len(epos) == 6:
                # choose from + positions
                for r, c in epos:
                    if (r + c) % 2 != 0:
                        board[r][c] = v
                        return r, c
            # fifth turn (center)
            if len(epos) == 5:
                # check if the center is empty
                if (1, 1) in epos:
                    board[1][1] = v
                    return 1, 1
        # only engine level >= 2
        if self.__engine >= 2:
            # choose corner
            for r, c in epos:
                if (r + c) % 2 == 0:
                    board[r][c] = v
                    return r, c
        # choose random
        r, c = epos[randint(0, len(epos) - 1)]
        board[r][c] = v
        return r, c

    def __get_empty(self, board: list) -> list:
        """Get empty positions list from LTR TTB

        :param board: TicTacToe board
        :type board: list
        :returns: empty position
        :rtype: list
        """
        return [(r, c) for r in range(3) for c in range(3) if not board[r][c]]
