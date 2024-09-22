print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
your_total = tip/100*bill+bill
my_share = round(your_total/people)
print(f"Each person split: ${my_share}")


