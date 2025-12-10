import sys

income_list = []
expense_list = {}
income = 0

def add_income():
    global int_income
    while True:
        income = input("Add your income here: ")
        try:
            int_income = int(income)
            print("Your income has been added!")
            break
        except ValueError:
            print("Income must be an integer, please try again!")
    main()
    return 

def add_expenses():
    
    expense_item = input("Add your expense here: ")
    expense_amount = int(input("Add the expense amount here: "))
    expense_list[expense_item] = expense_amount
    print("Your expense was added!")  
    
    while True:
        choice = input("Do you need to add another expense: ")
        try:
            if choice != "yes" and choice != "no":
                print("Input either yes or no, please try again!")
                continue
            if choice == "no":
                main()
            if choice == "yes":
                expense_item = input("Add your expense here: ")
                expense_amount = int(input("Add the expense amount here: "))
                expense_list[expense_item] = expense_amount
                print("Your expense was added!")
            choice = input("Do you need to add another expense: ")
            continue
        except ValueError:
            print("Either yes or no must be entered, please try again")
          
            
    return

def view_balance():
    global int_income, expense_list
    if int_income == 0:
        print("You have not yet entered your income")
        add_income()
        return
    total_expenses = sum(expense_list.values())
    balance = int_income - total_expenses
    print(f"Your balance is: {balance}")
    main()

    return 

def view_spending_summary():
    print("This is your spending summary: ")
    for c, values in expense_list.items():
        print(f"{c} : {values}")
        if c == "" and values == 0:
            print("You have no expenses")
            
    main()
    return
    
def exit_program():
    print("You are exiting the program. Come again soon :)")
    return sys.exit(0)

def main():
    print("Welcome to your personal budget tracker")

    commands = ["Add Income", "Add Expenses", "View Balance", "View Spending Summary", "Quit"]

    for num, option in enumerate(commands, start = 1):
        print(f"{num}. {option}")


    while True:
        choose = input("Choose an option:")
        try:
            int_choose = int(choose)
            if int_choose > 5:
                print("Option must be an integer from 1-5, please try again!")
                continue
            break
        except ValueError:
            print("Option must be an integer, please try again!")

    if int_choose == 1:
        add_income()

    if int_choose == 2:
        add_expenses()

    if int_choose == 3:
        view_balance()
    
    if int_choose == 4:
        view_spending_summary()
    
    if int_choose == 5:
        exit_program()

main()