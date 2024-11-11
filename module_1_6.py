my_dict = {'Nick': 29, 'Pam': 35, 'Liza': 30, 'Donald': 78}
print(my_dict)
print(my_dict['Nick'])
my_dict['Misha'] = 61
print(my_dict['Misha'])
my_dict.update({'Roma': 31, 'Ivan': 27})
print(my_dict)
del my_dict ['Nick'] #для тренировки с помощью данной функции удалил элемент
print(my_dict)
print(my_dict.get('Nick', 'уже удален'))
my_dict['Nick'] = 29
a = my_dict.pop('Nick')
print(a)
print(my_dict)

my_set  = {1,1,1,2,2,3,4,5,5,True,True,(11,22,33,44,55),(11,22,33,44,55)}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove((11,22,33,44,55))
print(my_set)
my_set.discard(1)
print(my_set)
print(my_set.discard(1)) #не выдает ошибку
print(my_set.remove(1)) # выдает ошибку