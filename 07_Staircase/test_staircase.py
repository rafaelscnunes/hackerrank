"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_staircase.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import staircase


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_0(self):
        self.assertEqual(['    #', '   ##', '  ###', ' ####', '#####'], staircase.staircase(5))

    def test_1(self):
        staircase.staircase_optimized(7)
        self.assertEqual(['  #', ' ##', '###'], staircase.staircase(3))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
