import unittest
import comparethetriplets


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_0(self):
        self.assertEqual([1,1], comparethetriplets.compareTriplets([5, 6, 7], [3, 6, 10]))

    def test_1(self):
        self.assertEqual([2,1], comparethetriplets.compareTriplets([17, 28, 30], [99, 16, 8]))

    def test_2(self):
        self.assertEqual([1, 1], comparethetriplets.compareTriplets(['5', '6', '7'], ['3', '6', '10']))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
