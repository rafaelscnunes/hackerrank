"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_theprimegame.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import theprimegame


class WinnerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_winner0(self):
        self.assertEqual('Manasa', theprimegame.winner([84, 87, 78, 16, 94, 36, 87, 93, 50, 22]))

    def test_winner1(self):
        self.assertEqual('Manasa', theprimegame.winner([63, 28, 91, 60, 64, 27, 41, 27, 73, 37]))

    def test_winner2(self):
        self.assertEqual('Manasa', theprimegame.winner([12, 69, 68, 30, 83, 31, 63, 24, 68, 36]))

    def test_winner3(self):
        self.assertEqual('Sandy', theprimegame.winner([30, 3, 23, 59, 70, 68, 94, 57, 12, 43]))

    def test_winner4(self):
        self.assertEqual('Manasa', theprimegame.winner([30, 74, 22, 20, 85, 38, 99, 25, 16, 71]))

    def tearDown(self) -> None:
        pass


class ExchangeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_exchange0(self):
        self.assertEqual('Sandy', theprimegame.exchange('Manasa'))

    def test_exchange1(self):
        self.assertEqual('Manasa', theprimegame.exchange('Sandy'))

    def tearDown(self) -> None:
        pass


class TurnTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_turn0_0(self):
        self.assertEqual((True, [3, 10]), theprimegame.turn([10, 10]))

    def test_turn0_1(self):
        self.assertEqual((True, [0, 10]), theprimegame.turn([3, 10]))

    def test_turn0_2(self):
        self.assertEqual((True, [0, 3]), theprimegame.turn([3, 3]))

    def test_turn0_3(self):
        self.assertEqual((True, [0, 0]), theprimegame.turn([0, 3]))

    def test_turn0_4(self):
        self.assertEqual((False, [0, 0]), theprimegame.turn([0, 0]))

    def test_turn1_0(self):
        self.assertEqual((True, [0, 2, 3]), theprimegame.turn([2, 2, 3]))

    def test_turn1_1(self):
        self.assertEqual((True, [0, 2, 0]), theprimegame.turn([2, 2, 0]))

    def test_turn1_2(self):
        self.assertEqual((True, [0, 0, 0]), theprimegame.turn([0, 2, 0]))

    def test_turn1_3(self):
        self.assertEqual((False, [0, 0, 0]), theprimegame.turn([0, 0, 0]))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
