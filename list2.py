my_list = [1, 2, 3, 3, 2, 5, 1]
unique_list = []

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print("List without duplicates:", unique_list)