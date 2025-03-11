unitsconsumed=int(input("Enter the units:"))
if unitsconsumed<50:
    amount=unitsconsumed*2.60+25
elif unitsconsumed>=50 and unitsconsumed<100:
    amount=unitsconsumed*3.25+35
elif unitsconsumed>=100 and unitsconsumed<200:
    amount=unitsconsumed*5.26+45
else:
    amount=unitsconsumed*8.45+70
print("the electricity bill is:", amount)