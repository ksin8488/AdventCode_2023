import unittest
import calibCalc

from calibCalc import calculate_num
#NOTE: pytest is also a popular library for testing with less repetitive coding and more advanced features.

class TestCalibrationCalculations(unittest.TestCase):
    
    def test_calculate_number(self):
        result = calibCalc.calculate_num("five6seven8")
        self.assertEquals(result, 68)

#Means if module is run directly then run code in the conditional  
if __name__ == '__main__':
    unittest.main()
#now can run python test_calibCalc.py