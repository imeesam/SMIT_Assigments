from datetime import datetime

account = None 

def open_acc():
    global account
    try:
        name = input("Enter your Name to create an Account:")
        balance = float(input("Enter your balance to open account:"))
    
        if name.isalpha() and balance>=0:
            print(f"Account For {name} created with balance ${balance}")
            account = { "Name" : name ,
                        "Balance" : balance ,
                        "transacation": [] }
            new_balance = account["Balance"]
            record_transcations("deposit",balance,new_balance)
            return account
        else:
            print("Please Enter a Name with Alphabets and a valid balance!")
    except ValueError:
         print("Please Enter a valid Amount!")

def depoist_money():
    global account
    try:
        money = float(input("Enter amount for deposit:"))
        if money <= 0:
            return "Please enter valid postive amount !!"
        else:
            account["Balance"] += money
            new_balance = account["Balance"]
            record_transcations("deposit",money,new_balance)
            return account
    except ValueError :
        return "Amount must be a positive number!"

def withdraw_money():
    global account
    try:
        money = float(input("Enter amount for withdrawl:"))
        if money <= 0 or money > account["Balance"]:
            return "Please enter valid amount !!"
        else:
            account["Balance"] -= money
            new_balance = account["Balance"]
            record_transcations("withdraw",money,new_balance)
            return account
    except ValueError:
        return "Amount must be a positive number!"

def check_balance():
    global account
    money =  account["Balance"]   
    return f"The amount in your Bank is ${money}."


def record_transcations(transacation_type,amount,new_balance):
    global account
    transacation = {
        "type": transacation_type,
        "amount": amount,
        "new balance" : new_balance,
        "time": datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    account["transacation"].append(transacation)
    with open("transacation.txt" , 'a') as file:
        file.write(f"- {transacation["type"]}: ${transacation["amount"]}. New Balance: ${transacation["new balance"]}\n")


def print_statement():
    print(f"Account statement for {account['Name']}:")
    with open("transacation.txt", 'r') as file:
        print(file.read())

def Banking_system(): 
    global account 
    while True:
        try:
            print("\n\tWelcome To Banking System:\t")
            print("1. Create Account.")
            print("2. Deposit Money.")
            print("3. Withdraw Money.")
            print("4. Check Balance.")
            print("5. Print Statement.")
            print("6. Exit.")
            try:
                opt = int(input("Choose any of the following Options:"))
                if opt == 1:
                    account = open_acc()
                elif opt == 2: 
                    if account:
                        print(depoist_money())
                    else:
                        print("Create Account First!")
                elif opt == 3:
                    if account:
                        print(withdraw_money())
                    else:
                        print("Create Account First!")                
                elif opt == 4:
                    if account:
                        print(check_balance())
                    else:
                        print("Create Account First!")
                elif opt == 5:
                    if account:
                        print_statement()
                    else:
                        print("Create Account First!")
                elif opt == 6:
                    print("Exiting")
                    break
                else:
                    print("Please Select from following options!!")
            except ValueError:
                 print("Please enter a valid number.")
        except ValueError:
            print("\nPlease provide valid information. Try Again!!")