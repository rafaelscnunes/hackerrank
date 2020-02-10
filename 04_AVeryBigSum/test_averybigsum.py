"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_averybigsum.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import averybigsum


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_0(self):
        self.assertEqual(5000000015, averybigsum.aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
