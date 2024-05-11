import math
import os

# Read credentials from file
with open('authorized_users.txt', 'r') as f:
    credentials_line = f.readline().strip()

# Parse credentials into dictionary
credentials = {
    'user': credentials_line.split(',')[0],
    'pass': credentials_line.split(',')[1],
    'level': int(credentials_line.split(',')[2])
}

# Prompt user for login credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if user credentials match authorized credentials
authorized = username == credentials['user'] and password == credentials['pass']

if authorized:
     # Print welcome message and access level
    print(f"Welcome, {username}! Your access level is {credentials['level']}.")
    print('--------------------------------------------------------------------------')
    # Landscaping program code goes here
    print('Welcome to to the Fertilizer Calculator!')
    print('I will ask if you have a specific section of the lawn.')
    print('Then I will ask you for the length and width of those (rectangular) sections.')
    print('--------------------------------------------------------------------------')
    #Ask if each lawn exists
    front_lawn = int(input("Does the front lawn exist? (1 for yes, 0 for no): "))
    back_lawn = int(input("Does the back lawn exist? (1 for yes, 0 for no): "))
    side1_lawn = int(input("Does side 1 lawn exist? (1 for yes, 0 for no): "))
    side2_lawn = int(input("Does side 2 lawn exist? (1 for yes, 0 for no): "))
    print('--------------------------------------------------------------------------')
    #Ask for the lenght and width of each lawn to calculate total area
    if front_lawn == 1:
        front_lawn_length = int(input("What is the length of the front lawn? "))
        front_lawn_width = int(input("What is the width of the front lawn? "))
        front_lawn_area = front_lawn_length*front_lawn_width
    if back_lawn == 1:
        back_lawn_length = int(input("What is the length of the back lawn? "))
        back_lawn_width = int(input("What is the width of the back lawn? "))
        back_lawn_area = back_lawn_length*back_lawn_width
    if side1_lawn == 1:
        side1_lawn_length = int(input("What is the length of side 1 lawn? "))
        side1_lawn_width = int(input("What is the width of side 1 lawn? "))
        side1_lawn_area = side1_lawn_length*side1_lawn_width
    if side2_lawn == 1:
        side2_lawn_length = int(input("What is the length of side 2 lawn? "))
        side2_lawn_width = int(input("What is the width of side 2 lawn? "))
        side2_lawn_area = side2_lawn_length*side2_lawn_width
    print('--------------------------------------------------------------------------')
    #If the lawn does not exist, set the area to 0
    if front_lawn == 0:
        front_lawn_area = 0
    if back_lawn == 0:
        back_lawn_area = 0
    if side1_lawn == 0:
        side1_lawn_area = 0
    if side2_lawn == 0:
        side2_lawn_area = 0

    #Calculate the total area of the lawn
    total_area = front_lawn_area + back_lawn_area + side1_lawn_area + side2_lawn_area

    # Constants Values
    fertilizer_coverage_per_bag = 2000  # square feet
    fertilizer_cost_per_bag = 27  # dollars
    nitrogen_per_bag = 1  # pounds
    potassium_per_bag = 0.125  # pounds
    technician_coverage_per_hour = 2500  # square feet
    technician_wage_per_hour = 20  # dollars

    #Number of bags needed
    bags_needed = math.ceil(total_area / fertilizer_coverage_per_bag)
    #Calculate the total cost of the fertilizer
    fertilizer_needed_cost = fertilizer_coverage_per_bag * bags_needed

    #Hours of labor needed
    hours_needed = math.ceil(total_area / technician_coverage_per_hour)
    #Total cost of the labor
    technician_needed_cost = technician_wage_per_hour * hours_needed

    #Number of technicians needed
    workers_needed = total_area / technician_coverage_per_hour

    #total cost of the technicians
    technician_needed_cost = technician_coverage_per_hour * workers_needed

    #Total cost of the fertilizer and technicians
    total_cost = fertilizer_needed_cost + technician_needed_cost

    #Environmental Impact
    total_nitrogen = bags_needed * nitrogen_per_bag
    total_potassium = bags_needed * potassium_per_bag
    print('--------------------------------------------------------------------------')
    #RESULTS
    print(f'Your application has a total area of {total_area} sq. feet.')
    print(f'That will require {bags_needed} bags of fertilizer.')
    print(f'The cost of the fertilizer will be ${fertilizer_needed_cost}.')
    print(f'Our technicians will require {hours_needed} hours to finish the job and the labor cost will be ${technician_needed_cost}.')
    print(f'The total cost to the company will be ${total_cost}.')
    print(f'The application will add {total_nitrogen} pounds of nitrogen and {total_potassium} pounds of potassium to the soil.')
else:
    print("Invalid credentials. Please try again.")