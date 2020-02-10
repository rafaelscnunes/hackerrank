"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_diagonaldifference.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import diagonaldifference


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_row(self):
        self.assertEqual(15, diagonaldifference.diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
