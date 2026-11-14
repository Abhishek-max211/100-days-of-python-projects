print("----Welcome to the Tip Calculator!----")

total_bill = eval(input("What was the total bill? $"))
tip = int(input("How much tip percent would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip / 100)
total_amount =  total_bill + tip_amount
split_bill = total_amount / people

print(f"Each person should pay:- ${round(split_bill,2)}")