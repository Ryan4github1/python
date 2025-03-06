Height=float(input("Enter you height in Cm: "))
Weight=float(input("Enter your weight in Kg: "))
BMI= Weight/(Height/100)**2
print("your BMI is", BMI)

if BMI<= 18.4:
    print("you are underweight. ")
elif BMI<= 24.9:
    print("you are Healthy. ")
elif BMI<= 29.9:
    print("you are overweight. ")
elif BMI<= 34.9:
    print("you are severely over weight. ")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are severely obese")