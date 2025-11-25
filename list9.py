my_tuple = (10, 20, 30, 40, 50)

value = int(input("Enter value to find: "))

if value in my_tuple:
    print("Index of", value, "is:", my_tuple.index(value))
else:
    print("Value not found in the tuple.")