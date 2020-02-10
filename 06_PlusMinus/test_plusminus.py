"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_plusminus.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import plusminus


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_something(self):
        precision = '{:.6f}'
        self.assertEqual([precision.format(0.500000),
                          precision.format(0.333333),
                          precision.format(0.166667)],
                         plusminus.plusMinus([-4, 3, -9, 0, 4, 1], precision))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
