def calculate_due_amount(a, b):
    due_amount = a - b
    if due_amount < 0:
        print(f"You gave more than enough! You should get back ${abs(due_amount)}")
    else:
        print(f"You still owe ${due_amount}")
    return due_amount 
n1 = int(input("Enter the total cost: $"))
n2 = int(input("Enter the amount paid: $"))
ans = calculate_due_amount(n1, n2)