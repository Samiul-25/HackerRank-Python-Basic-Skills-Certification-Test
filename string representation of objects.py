import math
import os
import random
import re
import sys

# Define the Car class with a custom __new__ method to return a formatted string
class Car:
    def __new__(cls, max_speed, unit):
        return "Car with the maximum speed of {0} {1}".format(max_speed, unit)

# Define the Boat class with a custom __new__ method to return a formatted string
class Boat:
    def __new__(cls, max_speed):
        return "Boat with the maximum speed of {0} knots".format(max_speed)

if __name__ == '__main__':
    # Open the output file specified by the environment variable OUTPUT_PATH for writing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read the number of queries
    q = int(input())
    
    # Initialize a list to store queries
    queries = []
    
    # Read each query from the input
    for _ in range(q):
        args = input().split()  # Split the input line into arguments
        vehicle_type, params = args[0], args[1:]  # Extract the vehicle type and parameters
        
        # Create the appropriate vehicle object based on the vehicle type
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")  # Raise an error if the vehicle type is invalid
        
        # Write the vehicle description to the output file
        fptr.write("%s\n" % vehicle)
    
    # Close the output file
    fptr.close()
