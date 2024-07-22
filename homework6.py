'''-------Словари------'''
my_dict = {'Павел': 1991,
           'Антон': 1992,
           'Светлана': 2000,
           'Игорь': 1998}
print(my_dict)
print(my_dict.get('Павел'))
print(my_dict.get('Петр'))
my_dict.update({'Стас': 2022,
                'Лена': 1980})
del_item = my_dict.pop('Игорь')
print("Игорь: ", del_item)
print(my_dict)

'''-------Множества------'''
my_set = {1, 'f', True, 1, 'a', False, (1, 2), 'f', 2}
print(my_set)
my_set.add(3)
my_set.add('b')
print(my_set)
my_set.discard('f')
print(my_set)
