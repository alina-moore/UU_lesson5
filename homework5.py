immutable_var = (1, 2, "hello", False)
print("Immutable tuple: ", immutable_var)
# immutable_var[1] = 5
# print(immutable_var)
# ошибка. кортеж - неизменяемая коллекция, изменить элементы объект, который относится к типу tuple нельзя
mutable_list = [1, 2, "hello", False]
mutable_list[1] = 5
print("Mutable list: " , mutable_list)
