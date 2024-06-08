""" Main file for 2_cube problem

This file takes an input file or given line and calculates if the number of cubes in each
round of a game is actually possible based on how many actual cubes there are in the "bag".
Returns a sum of all the possible games.
"""

import argparse
import sys
import fileinput
import re

#---LAUNCHER ARGUMENTS---

#Allows user to add a file representing game information
parser = argparse.ArgumentParser(
    description="May take a file to read each line for Game and results in the game"
)

parser.add_argument(
    "-f", "--file", "--filepath", metavar="file",
    required=False, help="Filepath for a file containing game ID and different results."
)

args = parser.parse_args()
print("Input file:", args.file)

#---METHODS---
def read_file(filepath):
    '''
    Takes a user give file for the cube games and starts calculating the sum of the game
    IDs that have valid results. i.e the # of cubes taken out don't exceed the actual # of cubes
    
    Args:
        filepath: filepath to the cube games that's checked line by line
        
    Return: 
        total_gameID: the sum of the game IDs for each game that is possible
    '''
    try:
        file = open(filepath, 'r')
        total_gameID = 0
        
        for line in file:
            total_gameID += parse_games(line)
        file.close()
        
        print("Added value of Game IDs:", total_gameID)
        return total_gameID
        
    except FileNotFoundError:
        print("File not found error. Please check the filepath again")
        raise


def parse_games(line):
    '''
        takes a string and uses regex to split them into sections in order to check if the game cubes
    exceed the true number of cubes in the bag.

    Args:
        line: a line containing the game ID and rounds where red, green, & blue cubes are moved 

    Return: 
        sucessful_ID: 
    '''
    gameID_list = [] #List of all valid games and the game ID info at index 0
    gameID_list = re.split(r"\:|;", line)
    
    for game in gameID_list[1:]: #[:1] lets you skip the first element (our game ID)
        single_pull_list = re.split(",", game) #splits each game into the cubes pulled
        
       #Checks that each color DOES NOT exceed the limits in the bag. If so, automatically returns 0 (representing no game)  
        for cubes in single_pull_list: 
            if "red" in cubes:
                if int(re.sub("\D+", "", cubes)) > max_rgbCubes[0]:
                    return 0
            elif "green" in cubes:
                if int(re.sub("\D+", "", cubes)) > max_rgbCubes[1]:
                    return 0
            elif "blue" in cubes:
                if int(re.sub("\D+", "", cubes)) > max_rgbCubes[2]:
                    return 0
            else:
                print("ERROR! There's a cube color/text that shouldn't be there")
                return 0
            
    #If all pulls in the game are valid, return the game ID as an integer
    sucessful_ID = int(re.sub("\D+", "", gameID_list[0]))
    return sucessful_ID
    
#--MAIN CODE---
#default numbers in "bag" is Red=12, Green=13, Blue=14
max_rgbCubes = [12, 13, 14] #red, green, blue in order

if args.file is not None:
    read_file(args.file)
else:
    parse_games("Game 1: 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue")