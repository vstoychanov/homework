my_dict = {'Victor': 2001, 'Sergey': 1999, 'Sasha': 1998}
print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get('Alex'))
my_dict.update({'Vadim': 1897,
                'Pasha': 1974})
a = my_dict.pop('Victor')
print(a)
print(my_dict)

my_set = {1, 1, 2, 'String', True, (1, 4, 5)}
print(my_set)
my_set.add(7)
my_set.add("string2")
my_set.discard('String')
print(my_set)