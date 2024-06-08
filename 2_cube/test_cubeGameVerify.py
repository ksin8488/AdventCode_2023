import unittest
import os
import cubeGameVerify

class TestCubeGameVerify(unittest.TestCase):
    
    #Setup testing materials
    def setUp(self):
        fp = open('cubeTesting.txt', 'w')
        fp.write("Game 1: 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue\n")
        fp.close()
        
        
    #TESTING
    #TODO: test file inputs, combining colors, random games, error checking
    
    #teardown
    def tearDown(self):
        os.remove("cubeTesting.txt")
        
if __name__ == '__main__':
    unittest.main()
