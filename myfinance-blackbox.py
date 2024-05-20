def calculate_net_pay(hourly_wage, hours_worked):
    gross_pay = hourly_wage * hours_worked
    federal_tax = gross_pay * 0.10
    state_tax = gross_pay * 0.05
    social_security = gross_pay * 0.062
    net_pay = gross_pay - federal_tax - state_tax - social_security
    print(f"Gross Pay: ${gross_pay:.2f}({hours_worked:.0f} hours @ ${hourly_wage:.2f}/hr)")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}\n")

def enter_revenue_or_expense(revenues_and_expenses):
    while True:
        transaction_name = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expense): "))
        revenues_and_expenses[transaction_name] = amount
        another = input("Another? (Y/N): ")
        if another.lower() != 'y':
            break

def show_discretionary_income(revenues_and_expenses):
    total_revenue = sum(amount for amount in revenues_and_expenses.values() if amount > 0)
    total_expenses = sum(amount for amount in revenues_and_expenses.values() if amount < 0)
    discretionary_income = total_revenue + total_expenses
    print(f"Revenue: ${total_revenue:.2f} Expenses: ${total_expenses:.2f} Discretionary: ${discretionary_income:.2f}\n")

def main():
    revenues_and_expenses = {}
    while True:
        print("1-Calculate net pay")
        print("2-Enter revenue or expense")
        print("3-Show discretionary income")
        print("4-Exit")
        choice = int(input("Choice: "))
        if choice == 1:
            hourly_wage = float(input("What is your hourly wage? "))
            hours_worked = float(input("How many hours did you work? "))
            calculate_net_pay(hourly_wage, hours_worked)
            revenues_and_expenses["pay"] = hourly_wage * hours_worked
        elif choice == 2:
            enter_revenue_or_expense(revenues_and_expenses)
        elif choice == 3:
            show_discretionary_income(revenues_and_expenses)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()