m = int(input("Введите месяц: "))
s_dict = {0: 'spring', 1: 'summer', 2: 'autumn', 3: 'winter'}
if m == 3 or m == 4 or m == 5:
    print(s_dict.get(0))
elif m == 6 or m == 7 or m == 8:
    print(s_dict.get(1))
elif m == 9 or m == 10 or m == 11:
    print(s_dict.get(2))
elif m == 12 or m == 1 or m == 2:
    print(s_dict.get(3))
else:
    print("Несуществующий месяц")

m = int(input("Введите месяц: "))
s_list = ['spring', 'summer', 'autumn', 'winter']
if m == 3 or m == 4 or m == 5:
    print(s_list[0])
elif m == 6 or m == 7 or m == 8:
    print(s_list[1])
elif m == 9 or m == 10 or m == 11:
    print(s_list[2])
elif m == 12 or m == 1 or m == 2:
    print(s_list[3])
else:
    print("Несуществующий месяц")