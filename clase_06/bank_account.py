class BankAccount:
    def __init__(self, balance = 0) -> None:
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("El monto a depositar debe ser positivo")

    def withdraw(self, amount):
        """
        Retirar dinero
        """
        if self.__balance > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("El monto a retirar es invalido o no tienes fondos suficientes")

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("El balance no puede ser negativo")

account = BankAccount()
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(50)
print(account.balance)
account.balance = 40
print(account.balance)

