try:
    a,b=eval(input("enter the no's: "))
    print(a,b)
except SyntaxError:
    print("check syntaxes")