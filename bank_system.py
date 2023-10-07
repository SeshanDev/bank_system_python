#loan details
def loan_details():
    print("\n LOAN DETAILS'")
    print("******************************************\n\n")
    print(" Months             Rate\n")
    print(" 0-36                15%\n")
    print(" 36-60               20%\n")
    print(" 60-84               25%\n")
    print("  <84                30%\n")

    
    main_menu()       #return to main menu


    
#customer new profile
def customer_new_profile():
    print("******************************************\n")
    customer_file = open("customer_details.txt","a")
    transaction_file = open("transaction_details.txt","a")
    new_customer_id = input("--> Enter new customer ID: ")
    new_customer_name = input("--> Enter new customer NAME: ")
    new_customer_branch = input("--> Enter the branch of BANK: ")
    new_customer_phone = input("--> Enter new customer PHONE NUMBER: ")
    new_customer_pass = input("--> Enter new customer PASSWORD: ")
    new_customer_balance = input("--> Enter BALANCE for new customer: ")
    customer_file.write(new_customer_id+","+new_customer_name+","+new_customer_branch+","
                        +new_customer_phone+","+new_customer_pass+","+new_customer_balance+"\n")
    customer_file.close()
    transaction_file.write(new_customer_id+","+new_customer_balance+",Deposit\n")
    transaction_file.close()
    print("***** NEW ACCOUNT CREATED! *****")
    
    main_menu()       #return to main menu
    

#Customer login menu
def customer_login():
    print("\n\n------------- Customer Login -------------\n")
    customer_id = input("--> Enter your ID: ")
    customer_pass = input("--> Enter your Password: ")
    customer_file = open("customer_details.txt","r")
    for line in customer_file:
        login_customer = line.strip().split(",")
        if (customer_id == login_customer[0] and customer_pass == login_customer[4]):
            print("\n\n===** WELCOME, ",login_customer[1]," **===\n\n")
            customer_menu()
            return True
        else:
            print("**!!!! Your Password or ID is wrong !!!!**")
    
    customer_login()      #return to customer login
    return False



#Customer menu after login function
def customer_menu():
    print("------------- Customer MENU -------------:\n")
    print("1. Cash Deposit\n2. Cash Withdraw\n3. Account balance\n4. The monthly repayment for a loan  \n5. Interest calculated on the deposits of the account   \n6. Logout \n")
    customer_menu=int(input("--> Please select your options [1] [2] [3] [4] [5] [6] : "))
    while(customer_menu !='4'):
        if (customer_menu==1):
            customer_deposit()
        elif(customer_menu==2):
            customer_withdraw()
        elif(customer_menu==3):
            customer_Account_balance()
        elif(customer_menu==4):
            monthly_repayment_loan()
        elif(customer_menu==5):
            interest_deposits()
        elif(customer_menu==6):
            print("*** Good bye! Have a nice day! ***\n\n")
            main_menu()
        else:
            print("**!!! Invalid Option! Please read the option carefully! !!!**\n")
        customer_menu=int(input("--> Please select your options [1] [2] [3] [4] [5] [6] : "))
        

#Customer Cash deposit 
def customer_deposit():
    print("******************************************\n")
    deposit_id = input("--> Enter your ID: ")
    deposit_pass = input("--> Enter your Password: ")
    deposit_balance = int(input("--> Enter the BALANCE to be deposit: "))
    if (deposit_balance>0):
        customer_file = open("customer_details.txt","r")
        transaction_file = open("transaction_details.txt","a")
        for line in customer_file:
            cust_deposit = line.strip().split(",")
            if (deposit_id == cust_deposit[0] and deposit_pass == cust_deposit[4]):
                transaction_file.write(deposit_id+","+str(deposit_balance)+",Deposit\n")
                transaction_file.close()
                print("*** BALANCE SUCSSESFULLY DEPOSIT! ***")
                print("--- Return to Customer Menu ---\n")
                customer_menu()
            else:   
                print ("!!! You enter wrong ID or Password !!!")
        
        customer_menu()     #return to customer menu
    else:
        print("!!!you entered invalied deposit amount please try again!!!")
        customer_deposit()
    return False
    
#Customer Cash withdraw 
def customer_withdraw():
    current_balance=0
    view_id = input("--> Enter your ID: ")
    withdrawal_pass = input("--> Enter your Password: ")
    transaction_file = open("transaction_details.txt","r")
    print("\n-------- Transaction History --------\n")
    for line in transaction_file:
        view_transaction_file = line.strip().split(",")
        if (view_id == view_transaction_file[0]):
            current_balance=int(view_transaction_file[1])+current_balance
    print("Current Balance : {0:.2f}".format(current_balance))
    print("******************************************\n")
    withdrawal_id = view_id
    withdrawal_balance = int(input("--> Enter the BALANCE to be withdraw: "))
    if (withdrawal_balance>0):
        if (current_balance>withdrawal_balance):
            customer_file = open("customer_details.txt","r")
            transaction_file = open("transaction_details.txt","a")
            for line in customer_file:
                cust_withdrawal = line.strip().split(",")
                if (withdrawal_id == cust_withdrawal[0] and withdrawal_pass == cust_withdrawal[4]):
                    transaction_file.write(withdrawal_id+",-"+str(withdrawal_balance)+",Withdrawal\n")
                    transaction_file.close()
                    print("*** WITHDRAWAL SUCCESS! ***")
                    print("--- Return to Customer Menu ---\n")
                    customer_menu()
                    return True
                else:
                    print("!!! You enter wrong ID or Password !!!")
                    customer_menu()  #return to customer menu
        else:
            print("!!! You Account balance is not enough to withdraw money try again !!!")
            customer_withdraw()
    else:
        print("!!!you entered invalied withdraw amount please try again!!!")
        customer_withdraw()
    
    customer_menu()  #return to customer menu
    return False

#Customer Account balance      
def customer_Account_balance():
    current_balance=0
    print("******************************************\n")
    view_id = input("--> Enter your ID: ")
    transaction_file = open("transaction_details.txt","r")
    print("\n-------- Transaction History --------\n")
    for line in transaction_file:
        view_transaction_file = line.strip().split(",")
        if (view_id == view_transaction_file[0]):
            current_balance=int(view_transaction_file[1])+current_balance
            print(view_transaction_file[2]+"\t\t"+view_transaction_file[1])
    print("Current Balance : {0:.2f}".format(current_balance))
    
    
    customer_menu()      #return to customer menu


#calculate the monthly repayment for a loan
def  monthly_repayment_loan():
    print("******************************************\n")
    print("\n LOAN DETAILS'")
    print("******************************************\n\n")
    print(" Months             Rate\n")
    print(" 0-36                15%\n")
    print(" 36-60               20%\n")
    print(" 60-84               25%\n")
    print("  <84                30%\n")
    print("******************************************\n\n")
    loan_amount = float(input('-->Enter Loan Amount: '))
    numberOfmonths = int(input('-->Enter Loan payments in months: '))
    if(numberOfmonths<37):
        interest_rate=15
    elif(numberOfmonths<61):
        interest_rate=20
    elif(numberOfmonths<85):
        interest_rate=25
    elif(numberOfmonths>84):
        interest_rate=30
    interest_rate = float(interest_rate)/100
    monthlyPayments = (interest_rate/12) * (1/(1-(1+interest_rate/12)**(-numberOfmonths)))*loan_amount
    print("The monthly repayment for a loan : {0:.2f}".format(monthlyPayments))
    
    customer_menu()  #return to customer menu


#interest calculated on the deposits of the account
def interest_deposits():
    current_balance=0
    view_id = input("--> Enter your ID: ")
    deposit_pass = input("--> Enter your Password: ")
    transaction_file = open("transaction_details.txt","r")
    print("\n-------- Transaction History --------\n")
    for line in transaction_file:
        view_transaction_file = line.strip().split(",")
        if (view_id == view_transaction_file[0]):
            current_balance=int(view_transaction_file[1])+current_balance
    print("Current Balance : {0:.2f}".format(current_balance))
    print("******************************************\n\n")
    Deposit = current_balance
    import time
    from datetime import datetime
    if datetime.today().day == 30 or datetime.today().strftime("%m/%d") == '02/28':
        Deposit =int(Deposit)
        interest = (Deposit)*2/100
        current_balance = Deposit+interest
        deposit_id = view_id
        deposit_balance = int(interest)
        customer_file = open("customer_details.txt","r")
        transaction_file = open("transaction_details.txt","a")
        for line in customer_file:
            cust_deposit = line.strip().split(",")
            if (deposit_id == cust_deposit[0] and deposit_pass == cust_deposit[4]):
                transaction_file.write(deposit_id+","+str(deposit_balance)+",Deposit\n")
                transaction_file.close()
                
                print("The final total balance is: {0:.2f}".format(current_balance))
                print("Interest on the deposit of the account : {0:.2f}".format(interest))
                print("*** your monthly interest is SUCSSESFULLY DEPOSITED!  try again next month ***")
            else:   
                print ("!!! You enter wrong ID or Password !!!")
                interest_deposits()
        
        
    else:
        print("!!!Sorry, you have used this months interest limit, try again next  time in 30th of the month and also using only February 28th!!!")
    
    customer_menu()  #return to customer menu

#Main menu
def main_menu ():
    print("******************************************\n")
    print("**** WELCOME TO BANKING SYSTEM ****\n")
    print("******************************************\n\n")
    print("---------------MAIN  MENU-----------------\n")
    print("1. loan details\n2. Customer login  \n3. create new customer account \n4. Exit\n")
    main_menu=int(input("--> Please select your options [1] [2] [3] [4]: "))
    while(main_menu !='4'):
        if (main_menu==1):
            loan_details()
        elif(main_menu==2):
            customer_login()
        elif(main_menu==3):
            customer_new_profile()    
        elif(main_menu==4):
            quit()
        else:
            print("Invalid Option! Try again...\n")
        main_menu=int(input("--> Please select your options [1] [2] [3] [4]: "))


main_menu()


