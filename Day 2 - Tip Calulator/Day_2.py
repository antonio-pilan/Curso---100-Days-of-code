import functions

print("\nWelcome to Tip Calculator")

bill = input("What was the total Bill? ")

bill = functions.bill_formating(bill)
#print(bill, type(bill))

tip_rate = input("Now, What percentage will be your tip? ")

tip = functions.tip_calculator(bill,tip_rate)

people = input("How many people? ")

print("Each person should pay: R${:.2f}".format((bill + tip)/int(people)))

