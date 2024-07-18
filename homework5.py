immutable_var = True, 1, 5.2, 'string'
print(immutable_var)
#immutable_var[0] = 4 - - ошибка, так как элементы кортежа неизменяемые
mutable_list = [1, 5.2, True, 'string']
mutable_list[1] = 6
print(mutable_list)
