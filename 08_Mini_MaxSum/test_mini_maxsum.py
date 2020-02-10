"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_mini-maxsum.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import mini_maxsum


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_0(self):
        self.assertEqual([10, 14], mini_maxsum.miniMaxSum([1, 2, 3, 4, 5]))

    def test_1(self):
        self.assertEqual([15, 20], mini_maxsum.miniMaxSum([1, 2, 3, 4, 5, 6]))

    def test_2(self):
        self.assertEqual([21, 27], mini_maxsum.miniMaxSum([1, 2, 3, 4, 5, 6, 7]))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
