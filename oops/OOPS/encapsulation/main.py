class Transaction:

    def __init__(self,amount):
        self.__amount=amount
        self._receipt="TA-2625-GHUS-2025"

    def getBalance(self):
        return self.__amount
    
    def addBalance(self,amt):
        if amt<=0:
            return "Invalid Amount!! Please check again"
        else:
            self.__amount+=amt
            return f"Amount added successfully!!"
        
obj = Transaction(1000)

while(True):
    amt = int(input("Enter amt: "))
    print(obj.getBalance())
    print(obj.addBalance(amt))
    print(obj.getBalance())


