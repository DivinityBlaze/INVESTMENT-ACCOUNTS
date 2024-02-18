import random

# Generate 20 random account balances between 0 and 5000
investment_accounts = [random.randint(0, 5000) for _ in range(20)]

# Menu
while True:
    print("\nMenu Options:")
    print("1: Print Account Balances")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("4: Count Accounts Under $2000")
    print("5: Apply Donations")
    print("6: Simulate Hacker Attack")
    print("7: Exit")

    # User input
    option = int(input("Enter option number: "))

    # Menu Options
    if option == 1:
        print("\nAccount Balances:")
        account_num = 1
        for balance in investment_accounts:
            print("Account", account_num, ": $", balance)
            account_num += 1
    
    elif option == 2:
        index = int(input("Enter the account number to deposit into (1-20): "))
        amount = int(input("Enter the amount to deposit: $"))
        if 1 <= index <= len(investment_accounts):
            investment_accounts[index - 1] += amount
            print("Deposit confirmed: New Balance: $", investment_accounts[index - 1])
        else:
            print("Invalid account number.")
    
    elif option == 3:
        index = int(input("Enter the account number to withdraw from (1-20): "))
        amount = int(input("Enter the amount to withdraw: $"))
        if 1 <= index <= len(investment_accounts):
            if investment_accounts[index - 1] >= amount:
                investment_accounts[index - 1] -= amount
                print("Withdrawal confirmed: New Balance: $", investment_accounts[index - 1])
            else:
                print("Sorry, insufficient funds.")
    
    elif option == 4:
        count_under_2000 = 0
        for balance in investment_accounts:
            if balance < 2000:
                count_under_2000 += 1
        print("Number of Accounts Under $2000:", count_under_2000)
    
    elif option == 5:
        total_donated = 0
        account_num = 1
        for balance in investment_accounts:
            if balance < 2000:
                investment_accounts[account_num - 1] += 500
                print("Donation applied to Account", account_num, ": New Balance: $", investment_accounts[account_num - 1])
                total_donated += 500
            account_num += 1
        print("Total Amount Donated: $", total_donated)
    
    elif option == 6:
        total_stolen = 0
        account_num = 1
        for balance in investment_accounts:
            stolen_amount = balance * 0.05
            investment_accounts[account_num - 1] -= stolen_amount
            total_stolen += stolen_amount
            account_num += 1
        print("Total Amount Stolen: $", total_stolen)
    
    elif option == 7:
        exit() 