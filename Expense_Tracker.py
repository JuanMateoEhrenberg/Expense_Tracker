class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
        
class ExpenseTracker:
    def __init__(self):
       self.expenses = [] 
    
    #Main actions
    def addExpense(self, expense):
        self.expenses.append(expense)
    
    def removeExpense(self, index):
        index-=1 #Lowers one from the item, so it avoids typing 0 for item 1 and so on.
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully")
            
        else:
            print("Index not found in expenses")
            print(f"Available indexes are from 0 to {len(self.expenses) -1}. ")

    def viewExpenses(self):
        if len(self.expenses) == 0:
            print("There are no expenses!")
        else:
            print("Expenses list:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i} --> Date: {expense.date}, Expense Description:  {expense.description}, Amount: {expense.amount}")   
                
    def totalExpenses(self):
        total = sum(int(expense.amount) for expense in self.expenses)
        print(f"Total expenses: ${total}")


#Main point of entry for the program.        
def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")
        
        choice = input("Select your choice (1-5): -->> ")
        if choice == "1":
            print("You selected '1. Add Expense', lets get to it!")
            date = input("First inform the date of the Expense (YYYY-MM-DD) -->> ")
            description = input("Now inform description of the Expense -->> ")
            amount = input("Lastly, inform the amount ($) of the expense -->>")
            expense = Expense(date, description, amount)      
            tracker.addExpense(expense)
            print("Expense added succesfully!")
        
        if choice == "2":  
            print("You selected '2. Remove Expense', lets get to it!")
            index = input("Please inform which expense you wish to remove with the index -->> ")
            indexInt = int(index)  # Convert index to integer since it's a string
            tracker.removeExpense(indexInt)
            
        if choice == "3":
            print("You selected '3. View Expenses', lets get to it!")
            tracker.viewExpenses()
            
        if choice == "4":
            print("You selected '4. Total Expenses', lets get to it!")
            tracker.totalExpenses()
            
        if choice == "5":
            print("Thanks for trying this tracker! hope to see you soon! :) Bye")
            break
            
#Start the program.
main()