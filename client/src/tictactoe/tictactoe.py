from random import randint


class TicTacToe:

    """AI and win checking class
    
    :param board: TicTacToe board
    :type board: list
    :param engine: AI engine level (1 to 4)
    :type engine: int
    """

    def __init__(self, board: list, engine: int):
        self.__board = board
        self.__engine = engine

    @staticmethod
    def whoWinner(board: list) -> str:
        """Game end checker (check for winner or full board)

        :param board: TicTacToe board
        :type board: list
        :returns: winner (x, o) || full (f) || False
        :rtype: str
        """
        # check if the entire board filled
        if all(all(r) for r in board):
            return ('F', ())
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
        # nothing
        return ()

    def ai(self, v) -> bool:
        """ai player

        :param v: computer playing value (X, O)
        :type v: str
        :returns: True if success else False
        :rtype: bool
        """
        # set enemy value
        ev = "O" if v == "X" else "X"
        # get empty positions list
        epos = self.__get_empty()
        # check if there's empty position in the board
        if not epos:
            return False
        # AI algorithm ---
        # only engine level >=3
        if self.__engine >= 3:
            # empty board (play in random place except the center)
            if len(epos) == 9:
                while True:
                    r, c = epos[randint(0, 8)]
                    if (r, c) != (1, 1):
                        self.__board[r][c] = v
                        return True
            # second turn (play on the center if it's empty else corner)
            if len(epos) == 8:
                # check if the center is empty
                if (1, 1) in epos:
                    self.__board[1][1] = v
                    return True
                # choose corner
                for r, c in epos:
                    if (r + c) % 2 == 0:
                        self.__board[r][c] = v
                        return True
        # only engine level >= 2
        if self.__engine >= 2:
            # search for win position (Attack)
            for r, c in epos:
                # test the postision
                self.__board[r][c] = v
                # check if it win pos
                if AI.whoWinner(self.__board):
                    self.__board[r][c] = v
                    return True
                # reset the position
                self.__board[r][c] = ""
            # block enemy win pos (defence)
            for r, c in epos:
                # test the position
                self.__board[r][c] = ev
                if AI.whoWinner(self.__board):
                    self.__board[r][c] = v
                    return True
                # reset the position
                self.__board[r][c] = ""
        # only engine level 4
        if self.__engine == 4:
            # fourth turn (from + positions)
            if len(epos) == 6:
                # choose from + positions
                for r, c in epos:
                    if (r + c) % 2 != 0:
                        self.__board[r][c] = v
                        return True
            # fifth turn (center)
            if len(epos) == 5:
                # check if the center is empty
                if (1, 1) in epos:
                    self.__board[1][1] = v
                    return True
        # only engine level >= 2
        if self.__engine >= 2:
            # choose corner
            for r, c in epos:
                if (r + c) % 2 == 0:
                    self.__board[r][c] = v
                    return True
        # choose random
        r, c = epos[randint(0, len(epos))]
        self.__board[r][c] = v
        return True

    def __get_empty(self) -> list:
        """Get empty positions list from LTR TTB

        :returns: empty position
        :rtype: list
        """
        return [(r, c) for r in range(3) for c in range(3) if not self.__board[r][c]]
        