import unittest
import calibCalc
import os
from calibCalc import calculate_num
#NOTE: pytest is also a popular library for testing with less repetitive coding and more advanced features.

class TestCalibrationCalculations(unittest.TestCase):
    
    #use setUp() to setup things used later during tests
    def setUp(self):
        #create a testing file for unit testing
        fp = open('testing.txt', 'w')
        fp.write('one1two22three333four4444five5\n')
        fp.write('01\n')
        fp.close()
     
    #TESTS   
    def test_calculate_number(self):
        result = calibCalc.calculate_num("five6seven8")
        self.assertEqual(result, 68)

    def test_two_lines(self):
        result = calibCalc.calculate_num("123456")
        result += calibCalc.calculate_num("0123four")
        self.assertEqual(result, 19)
        
    def test_zeros(self):
        result = calibCalc.calculate_num("0000000000000000000000000000000000000000000")
        result += calibCalc.calculate_num("00")
        self.assertEqual(result, 0)
        
    def test_only_one_value(self):
        with self.assertRaises(IndexError):
            calibCalc.calculate_num("onetwothree4")
        
    def test_empty_line(self):
        with self.assertRaises(IndexError):
            calibCalc.calculate_num("")
            
    def test_no_filepath(self):
        with self.assertRaises(FileNotFoundError):
            calibCalc.get_file("")
            
    def test_wrong_filepath(self):
        with self.assertRaises(FileNotFoundError):
            calibCalc.get_file("1_trebuchet/testing.txt")
            
    def test_correct_test_file(self):
        result = calibCalc.get_file("testing.txt")
        self.assertEqual(result, 16)
        
    #Removes setup files after testing
    def tearDown(self):
        os.remove("testing.txt")
        
#Means if module is run directly then run code in the conditional  
if __name__ == '__main__':
    unittest.main()
#now can run python test_calibCalc.py