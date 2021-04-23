my_string = input("Введите строку: ")
string = my_string.split()
for ind, el in enumerate(string):
    print(ind + 1, el[:10])