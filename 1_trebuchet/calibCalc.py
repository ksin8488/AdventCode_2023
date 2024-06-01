"""Main File for 1_trebuchet problem solving

This file takes an input file and reads each line for the first and last numerical value to form a 2 digit number.
All digits for each line is then added together to create a final total that is returned when there are no more
lines left in the file to be calculated.
"""

import fileinput
import argparse
import sys

#--Launch Arguments---

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

def get_file(given_filepath):
    """
    Opens a file given in user argument when program runs and calculates the calibration number.
    
    Args: 
        given_filepath: filepath given by the user through args.file.
    Returns:
        total_num: all two digit numbers per line in the file added together.
    """
    total_num = 0
    
    try:
        file = open(given_filepath, 'r')
        for line in file:
            total_num += calculate_num(line)
        
        print("Calibration value is:", total_num)
        file.close()
        return total_num
    except FileNotFoundError:
        print("File not found error. Please check the filepath again")
        raise
        
#--Functions--

def calculate_num(line):
    """
    Takes a line and calculates a two digit number from first and last digits and returns it.
    
    Args:
        line: A string containing at least two digits. 
        
    Returns:
        line_value: The two digit number formed from first and last digits found in the line.
    """
    first_num = 0
    last_num = 0
    num_list = []
    
    for char in line:
        if(char.isdigit()):
            num_list.append(char)
    
    if(len(num_list) < 2):
        raise IndexError("There is less than two numbers in the following line. Please fix or use a new line.", line)
    
    first_num = num_list[0]
    last_num = num_list[-1] #-1 goes backwards from the starting value so it will be the last element in the list
    
    #concatonate first and last digit to form 2 digit num
    line_value = str(first_num) + str(last_num)
    return int(line_value)

#--Main Code--

total_num = 0 #Total count for the calibration value

#Uses user given file if in argument else prompts user for a line to get digit from
if args.file is not None:
    total_num = get_file(args.file)
    print("Calibration value from file is:", total_num)
else:
    user_line = input("Please enter a string with at least two numbers contained anywhere in it.\n")
    total_num = calculate_num(user_line)
    
    print("Calibration value is:", total_num)