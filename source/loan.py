# This tells you how much you stil owe for your mortgage

# Gather the details about the loan
money_owed = float(input("How much money did you borrow?\n"))
apr = float(input("What is the annual percentage?\n"))
payment = float(input("How much is each monthly payment?\n"))
months  = int(input("How many months since the loan started?\n"))

# Calculate the monthly rate
monthly_rate = (apr/100.0)/12.0
print("The monthy rate is", monthly_rate)

# Compound every month
for x in range(months):
    interest_paid = money_owed * monthly_rate 
    money_owed = money_owed + interest_paid
    
    if money_owed - payment < 0:
        print("The last payment is", money_owed)
        print("You paid off the loan in", x+1, "months")
        break
    
    money_owed = money_owed - payment 
    print("You paid", payment, "of which", interest_paid, "was interest", end= ' ')
    print("Now you owe", money_owed)
