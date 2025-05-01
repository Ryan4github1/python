def multiply_tuple_elements(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
my_tuple = (2, 3, 5, 7)
result = multiply_tuple_elements(my_tuple)
print("The product of the tuple elements is:", result)