class CheckingAccount:
    # class constructor. Used to initialise data at the time of class instantiation
    def __init__(self, name, address, account_number, balance):        
        # Public attributes
        self.name = name
        self.address = address
        self.account_number = account_number
        # balance is made as private attribute by using __ before its name
        self.__balance = balance

    # all the below methods are public methods. These methods can be called from other file
    def debitAccount(self, amount):
        # amount is subtracted and printed
        if(self.__balance>= amount):
            self.__balance -= amount
            print("%.2f" % amount, "debited and balance = %.2f"% self.__balance)
        else:
            print("No sufficient balance is available.")

    def creditAccount(self, amount):
        # amount is added and printed
        self.__balance += amount
        print("%.2f" % amount, "credited and Balance = %.2f" % self.__balance)

    def getBalance(self):
        # balance is printed
        print("Cuurent Balance = %.2f" % self.__balance)