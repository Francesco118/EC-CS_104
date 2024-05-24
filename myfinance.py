#MyFinance 
#Net Pay
def netPay(hourlyWage, totalHours):
      #  hourlyWage = int(input("What is your hourly wage? "))
     #   totalHours = int(input("How many hours did you work? "))
        grossPay = hourlyWage * totalHours
        federalTax = grossPay * 0.10
        stateTax = grossPay * 0.05
        socialSecurity = grossPay * 0.062
        netPay = grossPay - (federalTax + stateTax + socialSecurity)
        print("Your gross pay is $" + str(grossPay))
        print("Your federal tax is $" + str(federalTax))
        print("Your state tax is $" + str(stateTax))
        print("Your social security tax is $" + str(socialSecurity))
        print("Your net pay is $" + str(netPay))

#Enter Revenue or Expense
def revenue_expense(revenueOrExpense):
        while True:
                transactionName = input('Enter transaction name: ')
                transactionAmount = float(input("Enter amount (use negative sign for expense): "))
                revenueOrExpense[transactionName] = transactionAmount
                another = input("Another? y/n ")
                if another != "y":
                        break

#Show discretionary income
def discretionaryIncome(revenueOrExpense):
        totalRevenue = sum(transactionAmount for transactionAmount in revenueOrExpense.values() if transactionAmount > 0)
        totalExpenses = sum(transactionAmount for transactionAmount in revenueOrExpense.values() if transactionAmount < 0)
        discretionaryIncome = totalRevenue + totalExpenses
        print(f"Revenue: ${totalRevenue} Expense: ${totalExpenses} Discretionary: ${discretionaryIncome}\n")
#The program itself
def main():
        print("Welcome to My Finance!\n")
        revenueOrExpense = {}
        while True:
                print('\n1-Calculate net pay')
                print('2-Enter revenue or expense')
                print('3-Show discretionary income')
                print('4-Exit the program')
                userChoice = input("\nPlease select an option: ")

                if userChoice == "1":
                        hourlyWage = float(input("What is your hourly wage? "))
                        totalHours = float(input("How many hours did you work? "))
                        netPay(hourlyWage, totalHours)
                elif userChoice == "2":
                        revenue_expense(revenueOrExpense)
                elif userChoice == "3":
                        discretionaryIncome(revenueOrExpense)
                elif userChoice == "4":
                        #exitApplication()
                        exit = True
                        break
                else:
                        print("Invalid option. Please try again.")

if __name__ == "__main__":
   main()
   print("Thanks for using MyFinance!")