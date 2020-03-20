from unittest import TestCase

# local import
from src.tictactoe.tictactoe import TicTacToe


class Test_AI(TestCase):

    """tictactoe.tictactoe.TicTacToe unit tests class"""

    def __init__(self, *args, **kwargs):
        super(Test_AI, self).__init__(*args, **kwargs)
        self.ai = TicTacToe(1)

    def test_01_fullboard(self):
        """Full board case"""
        res = self.ai.ai([["X" for i in range(3)] for i in range(3)], "O")
        assert res == ()

    def test_02_engine1_valid_random_position(self):
        self.ai.engine = 1
        """valid random position with engine level 1"""
        b = [["X" for i in range(3)] for i in range(3)]
        b[1][0] = ""
        res = self.ai.ai(b, "O")
        assert res == (1, 0)

    def test_03_engine2_defence(self):
        """Block enemy line"""
        self.ai.engine = 2
        b = [["X", "", "O"], ["O", "", "X"], ["X", "O", "X"]]
        res = self.ai.ai(b, "O")
        assert res == (1, 1)

    def test_04_engine2_attack(self):
        """Attack on winning position event there's an defence position"""
        self.ai.engine = 2
        b = [["X", "", "X"], ["O", "", "O"], ["", "", ""]]
        res = self.ai.ai(b, "O")
        assert res == (1, 1)

    def test_05_engine3_firstmove_all_except_center(self):
        """first play (any random place except the center avoiding some tricks)"""
        self.ai.engine = 3
        b = [["" for i in range(3)] for i2 in range(3)]
        res = self.ai.ai(b, "X")
        assert res != (1, 1)

    def test_06_engine3_secondmove_center_target(self):
        """center target on second move"""
        self.ai.engine = 3
        b = [["" for i in range(3)] for i2 in range(3)]
        b[0][0] = "X"
        res = self.ai.ai(b, "O")
        assert res == (1, 1)

    def test_07_engine3_secondmove_unempty_center_corner_target(self):
        """second target on second move 'corners'"""
        self.ai.engine = 3
        b = [["" for i in range(3)] for i2 in range(3)]
        b[1][1] = "X"
        res = self.ai.ai(b, "O")
        assert res in [(0, 0), (0, 2), (2, 0), (2, 2)]

    def test_08_engine4_fourthmove_plus_positions_target(self):
        """Plus positions target on fourth move"""
        self.ai.engine = 4
        b = [["X", "", ""], ["", "O", ""], ["", "", "X"]]
        res = self.ai.ai(b, "O")
        assert res in [(1, 0), (0, 1), (1, 2), (2, 1)]

    def test_09_engine4_fifthmove_center_target(self):
        """Center target on fifth move"""
        self.ai.engine = 4
        b = [["X", "", ""], ["", "", "O"], ["O", "X", ""]]
        res = self.ai.ai(b, "X")
        assert res == (1, 1)
