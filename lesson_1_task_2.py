seconds = int(input("Введите время в секундах: "))
h = seconds // 3600
m = seconds % 3600 // 60
s = seconds % 3600 % 60
print(f'{h:02}:{m:02}:{s:02}')

