import unittest
import functions_for_testing as fft


class FunctionsTest(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(fft.suma(4, 5), 9)
        self.assertNotEqual(fft.suma(3, 4), 4)
        self.assertEqual(fft.suma(10, 15), 25)
        self.assertEqual(fft.suma(100, 150), 250)

    def test_dif(self):
        self.assertEqual(fft.dif(5, 1), 4)
        self.assertEqual(fft.dif(15, 3), 12)
        self.assertEqual(fft.dif(150, 250), -100)

    def test_multiple(self):
        self.assertEqual(fft.multiple(5, 2), 10)
        self.assertEqual(fft.multiple(25, 4), 100)

    # HW
    def test_div(self):
        try:
            fft.div(20, 0)
        except ZeroDivisionError:
            self.assertEqual(0, 0)
        self.assertEqual(fft.div(20, 10), 2)
        self.assertEqual(fft.div(100, 2), 50)
        self.assertNotEqual(fft.div(5000, 250), 6)
