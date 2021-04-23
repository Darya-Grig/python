my_list = [7, 5, 3, 3, 2]
n = int(input("ВВедите натуральное число: "))
a = my_list.count(n)
for el in my_list:
    if a > 0:
        i = my_list.index(n)
        my_list.insert(i + a, n)
        break
    else:
        if n > el:
            b = my_list.index(el)
            my_list.insert(b, n)
            break
        elif n < my_list[len(my_list) - 1]:
            c = my_list.index(el)
            my_list.append(n)
print(my_list)