immutable_var = 1, 'ok', True
print("Immutable list: ", immutable_var)
#immutable_var[0] = 2 - неизменяемый объект кортежа
#print(immutable_var)
mutable_list = ['a', 'b', 'c', 1, 2]
mutable_list[4] = 0
print("Mutable list: ", mutable_list)