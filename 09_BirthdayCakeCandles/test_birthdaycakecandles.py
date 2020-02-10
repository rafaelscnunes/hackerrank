"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_birthdaycakecandles.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import birthdaycakecandles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_0(self):
        self.assertEqual(2, birthdaycakecandles.birthdayCakeCandles([3, 2, 1, 3]))

    def test_1(self):
        self.assertEqual(1, birthdaycakecandles.birthdayCakeCandles([6, 3, 2, 5, 1, 4, 3, 5, 5, 2]))

    def test_2(self):
        self.assertEqual(3, birthdaycakecandles.birthdayCakeCandles([3, 2, 5, 1, 4, 3, 5, 5, 2]))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
