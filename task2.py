class BankAccount:
    def __init__(self, balance=0):
        """
        Ініціалізація рахунку з початковим балансом.
        Параметри:
        balance (int, float): початковий баланс рахунку (за замовчуванням 0).
        Викидає ValueError, якщо баланс негативний.
        """
        if balance < 0: raise ValueError("Initial balance cannot be negative.")
        self.balance = balance
    
    def deposit(self, amount):
        """
        Додає кошти на рахунок.
        Параметри:
        amount (int, float): сума для внесення на рахунок.
        Викидає ValueError, якщо сума для внесення непозитивна.
        """
        if amount <= 0: raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount):
        """
        Знімає кошти з рахунку.
        Параметри:
        amount (int, float): сума для зняття з рахунку.
        Викидає ValueError, якщо сума для зняття непозитивна або перевищує баланс.
        """
        if amount <= 0: raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance: raise ValueError("Not enough funds to withdraw.")
        self.balance -= amount
    
    def get_balance(self):
        """
        Повертає поточний баланс рахунку.
        """
        return self.balance