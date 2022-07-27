print ("Welcome to the tip calculator")

total_bill = input("What was the total Bill? $ ")
total_people = input("How many people to split the bill? ")
tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")

#returns price of each person 
split = (float(total_bill) / int(total_people))

#returns 0.xx - the % value of tax
tip_percent = float(tip) / 100

#returns the decmial value which is the tip
bill_with_tip = split * tip_percent 

#add the tip to the individual bill amount
final_total = bill_with_tip + split 


print("Each person should pay" , round(final_total, 1))