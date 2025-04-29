start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
if start > end:
    print("The start number must be less than or equal to the end number.")
else:
    squares = []
    even_squares = []
    odd_squares = []
    for number in range(start, end + 1):
        square = number * number
        squares.append(square)
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    print("\nEven square numbers:", even_squares)
    print("Odd square numbers:", odd_squares)