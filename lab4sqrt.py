# Prolog
# Author: David Yurek
# Section 012
# Sept. 11, 2013
# Lab 4 

# Defines main()
def main():
    
    # Imports from the math library so we can use math.sqrt.
    import math
    
    # Defines the height variables, gravity variable, and assigns values via input from the user.
    firstS_height = float(input("Enter the height for the first sphere: "))
    secondS_height = float(input("Enter the height for the second sphere: "))
    thirdS_height = float(input("Enter the height for the third sphere: "))
    g = 9.81
    
    # Calculates the fall time using the equation given and the height variables.
    firstS_time = math.sqrt(2*firstS_height/g)
    secondS_time = math.sqrt(2*secondS_height/g)
    thirdS_time = math.sqrt(2*thirdS_height/g)
    
    # Calculates the total time by adding the three time variables.
    total_time = firstS_time + secondS_time + thirdS_time
    
    # Rounds the time variables to the appropriate decimal places.
    firstS_time = round(firstS_time, 3)
    secondS_time = round(secondS_time, 3)
    thirdS_time = round(thirdS_time, 3)
    total_time = round(total_time, 5)
    
    # Prints the final information from the rounded variables.
    print("Time for the first shpere to fall is", firstS_time, "seconds.")
    print("Time for the second shpere to fall is", secondS_time, "seconds.")
    print("Time for the third shpere to fall is", thirdS_time, "seconds.")
    print("The total time is ", total_time, "seconds.")
    
# Calls main()    
main()
            