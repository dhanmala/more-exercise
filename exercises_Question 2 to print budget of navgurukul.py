expense = 0.0
budget = 0.0
difference = 0.0
expenseTotal = 0.0

total_expense = 0
keep_going = 'y'


#Input Module
budget = float(input("What is your budget for the month?"))
print("Please begin entering the amounts of each of your monthly expenses:")

while keep_going == 'y':
    expense = float(input("Monthly expense amount? $"))
#*Having an issue keeping the expense running total at the end of the program?*
    total_expense = total_expense + expense
    keep_going = input("Do you have any other expenses? (Enter y for yes.)")

#Calculations Module
if expense < budget:
    difference = budget - expense
    print(difference,"under budget.")

elif expense > budget:
    difference = expense - budget
    print(difference, " over budget.")

else:
    print("You were right on budget")


