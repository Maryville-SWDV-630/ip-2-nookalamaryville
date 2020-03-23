#importing CheckingAccount class
from CheckingAccount import CheckingAccount
#create an object of CheckingAccount
useraccount = CheckingAccount("Malli Nookala","Natoma Street, San Diego, CA 95324",5646362616,0.00)

# print a menu
print("1-Debit")
print("2-Credit")
print("3-View Balance")
print("q-Quit")
while True:
    # read user choice and execute corresponding method
    choice = input("Enter Choice : ")
    if choice == "1":
        amount = float(input("Enter Amount : "))
        useraccount.debitAccount(amount)
    elif choice == "2":
        amount = float(input("Enter Amount : "))
        useraccount.creditAccount(amount)
    elif choice == "3":
        useraccount.getBalance()
    else:
        break