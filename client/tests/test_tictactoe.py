from unittest import TestCase

# local import
from src.tictactoe.tictactoe import TicTacToe


class Test_TicTacToe(TestCase):

    """tictactoe.tictactoe.TicTacToe unit tests class (whoWinner function)"""

    def __init__(self, *args, **kwargs):
        super(Test_TicTacToe, self).__init__(*args, **kwargs)

    def test_01_horizontal_line_winning(self):
        """Fist winning case horizontal"""
        r1 = TicTacToe.whoWinner([["X", "X", "X"], ["", "", ""], ["", "", ""]])
        r2 = TicTacToe.whoWinner([["", "", ""], ["X", "X", "X"], ["", "", ""]])
        r3 = TicTacToe.whoWinner(
            [
                ["", "", ""],
                ["", "", ""],
                ["X", "X", "X"],
            ]
        )
        assert r1 == ("X", (0, 0))
        assert r2 == ("X", (1, 0))
        assert r3 == ("X", (2, 0))

    def test_02_vertical_line_winning(self):
        """Second winning case vertical"""
        r1 = TicTacToe.whoWinner([["O", "X", "O"], ["O", "X", ""], ["O", "", "X"]])
        r2 = TicTacToe.whoWinner([["X", "O", "O"], ["X", "O", ""], ["", "O", "X"]])
        r3 = TicTacToe.whoWinner([["O", "X", "O"], ["", "X", "O"], ["X", "", "O"]])
        assert r1 == ("O", (0, 1))
        assert r2 == ("O", (1, 1))
        assert r3 == ("O", (2, 1))

    def test_03_diagonal_line_winning(self):
        """Thired winning case diagonal"""
        r1 = TicTacToe.whoWinner([["X", "", ""], ["O", "X", ""], ["O", "", "X"]])
        r2 = TicTacToe.whoWinner([["O", "", "X"], ["O", "X", ""], ["X", "", ""]])
        assert r1 == ("X", (0, 2))
        assert r2 == ("X", (1, 2))

    def test_04_full_board(self):
        """Full board case"""
        r = TicTacToe.whoWinner([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]])
        assert r == ("F", ())

    def test_05_none_of_above_cases(self):
        """None of above cases"""
        r = TicTacToe.whoWinner([["X", "O", "X"], ["X", "O", ""], ["O", "X", "X"]])
        assert r == ()
