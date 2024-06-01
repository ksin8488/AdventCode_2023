"""Main File for 1_trebuchet problem solving

This file takes an input file and reads each line for the first and last numerical value to form a 2 digit number.
All digits for each line is then added together to create a final total that is returned when there are no more
lines left in the file to be calculated.
"""

import fileinput
import argparse
import sys

parser = argparse.ArgumentParser(
    description="May take a file to read each line for calibration numbers."
)

parser.add_argument(
    "-f", "--file", "--filepath", metavar="file",
    required=False, help="Filepath for a file containing lines with at least two numbers on each line for calibration code calculating."
)

args = parser.parse_args()
print("Input file:", args.file)

#--File section--

#TODO: start reading the file line by line and use another function to start adding values to a final total
def get_file():
    total_num = 0
    
    try:
        file = open(args.file, 'r')
        for line in file:
            total_num += calculate_num(line)
        
        print("Calibration value is:", total_num)
        file.close()
    except FileNotFoundError:
        print("File not found error. Please check the filepath again")
        sys.exit(1) #Exit with code 1 to indicate error
        
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
    first_num = 0
    last_num = 0
    num_list = []
    
    for char in line:
        if(char.isdigit()):
            num_list.append(char)
    
    first_num = num_list[0]
    last_num = num_list[-1] #-1 goes backwards from the starting value so it will be the last element in the list
    
    #concatonate first and last digit to form 2 digit num
    line_value = str(first_num) + str(last_num)
    return int(line_value)

if args.file is not None:
    get_file()
else:
    user_line = input("Please enter a string with at least two numbers contained anywhere in it.\n")
    total_num = 0
    total_num = calculate_num(user_line)
    
    print("Calibration value is:", total_num)
    
#--Error checking section--
    #TODO: extra section added for practicing error handling. What if there's only one digit? No digits? No lines in file? etc.