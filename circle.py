
import math

#Ask the user for the radius (variable) and store that input
radius = float(input(print("What is the radius? ")))

#Calculate the diameter (d = 2 * r)
diameter = 2*radius

#Calculate the Circumference (C = 2 * Pi * r)
circumference = 2*radius*math.pi

#Calculate the area (A = Pi * r)
area = math.pi*(radius**2)

#Print the results
print("The diameter is " + str(diameter))
print("The circumference is " + str(circumference))
print("The area is " + str(area))

#Ask the user if they would like to continue
#continue_program = input(print("Would you like to continue? "))
