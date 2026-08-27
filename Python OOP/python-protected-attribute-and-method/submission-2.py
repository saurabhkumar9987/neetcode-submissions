class Account:
    def __init__(self,title,balance):
        self.title = title 
        self._balance = balance  ## protected attribute 
    
    def display_balance(self) -> None:   # public method 
        print(f"Balance: ${self._balance}") # protected attribute 


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
