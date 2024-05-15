import math

keepPlaying = True
while keepPlaying == True:
    #Ask the user for a number
    number = int(input("Please enter a whole number (i.e., an integer): "))
    print(f"The number you entered is {number}.")

    #Check if the number is even or odd
    if number % 2 == 0:                          #Check if there's no remainder from the division
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    #Check if the number have a perfect square root
    if int(math.sqrt(number)) == math.sqrt(number):         #Check if the resulting number pass the integer test
        print(f"{number} is a perfect square number.")
    else:
        print(f"{number} is not a perfect square number.")

    #Check the factors for the number
    factors = []                                       #Initialize an empty list to store the factors

    for i in range(1, number):                         #check every number until the {number}
        if number%i == 0:                              #if the remainder is equal to zero, it is a valid factor
            factors.append(i)                          #add the number to the factors list
            i += 1
        
    print(f"The factors of {number} are ", factors)
    response = input("Would you like to enter another number (y/n)?: ").lower
    if  response !=  'y': #Ask the user if they want to enter another number
        keepPlaying = False

print('Thank you for playing!')