#Welcome user to My Finance
print("Welcome to My Finance!")

#Show Menu
#userChoice = 0
#userChoice = input(print("Please select an option:"))

#Functions

#Net Pay
def netPay(hourlyWage, totalHours):
        hourlyWage = input(print("What is your hourly wage? "))
        totalHours = input(print("How many hours did you work? "))
        print("Your salary is: ", netPay)
        netPay = hourlyWage * totalHours
        return netPay

#Enter Revenue or Expense
def revenueOrExpense(revenueOrExpense):
        print('Enter transaction name: ')
        print('Enter amount (use negative sign for expense): ')
#Show discretionary income
def discretionaryIncome(netPay, revenueOrExpense):

#Exit the program
def exitApplication():
    
#The program itself
def main():
        while exit == False:
                print("Please select an option:")
                print('1-Calculate net pay')
                print('2-Enter revenue or expense')
                print('3-Show discretionary income')
                print('4-Exit the program')
                userChoice = input(print("Please select an option:"))

                if userChoice == 1:
                        netPay(hourlyWage, totalHours)
                        print("Your salary is: ", netPay)
                elif userChoice == 2:
                        revenueOrExpense(revenueOrExpense)
                elif userChoice == 3:
                        discretionaryIncome(netPay, revenueOrExpense)
                elif userChoice == 4:
                        #exitApplication()
                        break
                else:
                        print("Invalid option. Please try again.")
