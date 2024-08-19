class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amoun = amount
        
class ExpenseTracker:
    def __init__(self):
       self.expenses = [] 
    
    #Main actions
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
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}, Date: {expense.date}, Description:  {expense.description}, Amount: {expense.amount:.2f}}")   
                
    def totalExpenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}")


#Main point of entry for the program.        
def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Add Expenses")
        print("5. Exit")
        
        choice = input("Select your choice (1-5): -->> ")
        if choice == "1" :
            print("You selected '1. Add Expense', lets get to it!")
            date = input("First inform the date of the Expense (DD/MM/YYYY) -->> ")
            description = input("Now inform description of the Expense (DD/MM/YYYY) -->> ")
            amount = input("Lastly, inform the amount ($) of the expense -->>")
            expense = Expense(date, description, amount)      
            tracker.addExpense(expense)
            print("Expense added succesfully!")
        
        if choice == "2" :  
            print("You selected '2. Remove Expense', lets get to it!")