class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amoun = amount
        
class ExpenseTracker:
    def __init__(self):
       self.expenses = [] 
    
    def addExpense(self, expense):
        self.expenses.append(expense)
    
    def removeExpense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully")
        else:
            print("Index not found in expenses")

    def viewExpenses(self):
        if len(self.expenses) == 0:
            print("There are no expenses!")
        else:
            print("Expenses list:")
            