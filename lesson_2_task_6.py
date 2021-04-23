q = int(input("Введите количество позиций товара: "))
l = 1
ch_list = []
ch_dict = []
an_dict = []
while q >= l:
    ch_dict = {'название': input("Введите название товара: "),
               'цена': input("Введите цену товара: "),
               'количество': input("Введите количество товара: "),
               'ед': input("Введите единицы измерения товара: ")}
    ch_list.append((l, ch_dict))
    l += 1
    an_dict = {'название': ch_dict.get('название'),
               'цена': ch_dict.get('цена'),
               'количество': ch_dict.get('количество'),
               'ед': ch_dict.get('ед')}
    print(ch_list)
    print(an_dict)

