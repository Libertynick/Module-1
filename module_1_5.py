immutable_var = (1,2,3,'kortezh',True)
print(immutable_var)
#immutable_var[0] = 21 # кортежи по своей природе не поддерживает обращение с элементами
mutable_list = [11,12,13,'spisok', False]
print(mutable_list)
mutable_list [0] = 111
mutable_list [3] = 14
mutable_list [4] = 'FalseSTR'
print(mutable_list)