"""Main File for 1_trebuchet problem solving

This file takes an input file and reads each line for the first and last numerical value to form a 2 digit number.
All digits for each line is then added together to create a final total that is returned when there are no more
lines left in the file to be calculated.
"""

import fileinput

#--File section--

#opens the "generatedCodes.txt" file to begin processing lines
#calibration_file = open('generatedCodes', 'r', encoding="utf-8")
total_num = 0

#TODO: start reading the file line by line and use another function to start adding values to a final total

#--Functions--
def calculate_num(line):
    """
    Takes a line and calculates a two digit number from first and last digits and returns it.
    
    Args:
        line: A string containing at least two digits. 
        
    Returns:
        line_value: The two digit number formed from first and last digits found in the line.
    """
    #TODO: Take a string and return a two digit number from the first and last digit found. 
    line_value = 0 #TODO: Actually code this
    return line_value

#--Error checking section--
    #TODO: extra section added for practicing error handling. What if there's only one digit? No digits? No lines in file? etc.