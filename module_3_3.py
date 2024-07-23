def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [2, 'list', True]
values_dict = {'a': 3,
               'b': 'dict',
               'c': False
               }
values_list_2 = [4, 'list_2']
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 45)
