import predict
import unittest

class PredictTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(0, predict.predict_algorithm(1))
    def test_02(self):
        self.assertEqual(1, predict.predict_algorithm(2))
    def test_03(self):
        self.assertEqual(1, predict.predict_algorithm(3))
    def test_04(self):
        self.assertEqual(2, predict.predict_algorithm(4))
    def test_05(self):
        self.assertEqual(1, predict.predict_algorithm(5))
    def test_06(self):
        self.assertEqual(2, predict.predict_algorithm(6))
    def test_07(self):
        self.assertEqual(2, predict.predict_algorithm(7))
    def test_08(self):
        self.assertEqual(0, predict.predict_algorithm(8))
    def test_09(self):
        self.assertEqual(1, predict.predict_algorithm(9))
    def test_10(self):
        self.assertEqual(2, predict.predict_algorithm(10))
    def test_11(self):
        self.assertEqual(2, predict.predict_algorithm(11))
    def test_12(self):
        self.assertEqual(0, predict.predict_algorithm(12))
    def test_13(self):
        self.assertEqual(2, predict.predict_algorithm(13))
    def test_14(self):
        self.assertEqual(0, predict.predict_algorithm(14))
    def test_15(self):
        self.assertEqual(0, predict.predict_algorithm(15))
    def test_16(self):
        self.assertEqual(1, predict.predict_algorithm(16))
    def test_17(self):
        self.assertEqual(1, predict.predict_algorithm(102))
    def test_18(self):
        self.assertEqual(0, predict.predict_algorithm(25685))
        
if __name__ == '__main__':
    unittest.main()