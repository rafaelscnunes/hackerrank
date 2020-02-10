"""
Created on 13/nov/2019 with PyCharm
INPI - Instituto Nacional da Propriedade Industrial
@author: Rafael Nunes - rafael.nunes@inpi.gov.br
@title: hackerrank - test_timeconversion.py
--------------------------------------------------------------------------------

    ***  Description of the module function  ***

--------------------------------------------------------------------------------
"""
import unittest
import timeconversion


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_Midnight_120000AM_000000(self):
        self.assertEqual('00:00:00', timeconversion.timeConversion('12:00:00AM'))

    def test_120052AM_000052(self):
        self.assertEqual('00:00:52', timeconversion.timeConversion('12:00:52AM'))

    def test_122752AM_002752(self):
        self.assertEqual('00:27:52', timeconversion.timeConversion('12:27:52AM'))

    def test_013500AM_013500(self):
        self.assertEqual('01:35:00', timeconversion.timeConversion('01:35:00AM'))

    def test_064722AM_064722(self):
        self.assertEqual('06:47:22', timeconversion.timeConversion('06:47:22AM'))

    def test_112752AM_112752(self):
        self.assertEqual('11:27:52', timeconversion.timeConversion('11:27:52AM'))

    def test_Noon_120000PM_120000(self):
        self.assertEqual('12:00:00', timeconversion.timeConversion('12:00:00PM'))

    def test_120052PM_120052(self):
        self.assertEqual('12:00:52', timeconversion.timeConversion('12:00:52PM'))

    def test_122752PM_122752(self):
        self.assertEqual('12:27:52', timeconversion.timeConversion('12:27:52PM'))

    def test_013500PM_133500(self):
        self.assertEqual('13:35:00', timeconversion.timeConversion('01:35:00PM'))

    def test_064722PM_184722(self):
        self.assertEqual('18:47:22', timeconversion.timeConversion('06:47:22PM'))

    def test_112752PM_232752(self):
        self.assertEqual('23:27:52', timeconversion.timeConversion('11:27:52PM'))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
