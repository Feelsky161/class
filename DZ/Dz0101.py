import random
#1. написать функцию генерирующую список заданного размера из случайных значений заданного диапазона
def generate_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]
print(generate_list(5, 0, 10))
#2. написать функцию, возвращающую максимальное значение из списка
def find_max(lst):
    return max(lst)
print(find_max(generate_list(5, 0, 10)))
#3. написать функцию, определяющую количество повторяющихся значений списка
def count_duplicates(lst):
    unique_elements = set(lst)
    return len(lst) - len(unique_elements)
print(count_duplicates(generate_list(5, 0, 10)))
'''4. написать функцию, принимающую в качестве параметра список и
возвращающую новый список, включающий только положительные числа из
первого списка'''
def get_positive_numbers(lst):
    return [num for num in lst if num > 0]
print(get_positive_numbers(generate_list(5, 0, 10)))
#5. написать функцию, удаляющую из списка все четные значения
def remove_even(lst):
    return [num for num in lst if num % 2 != 0]
print(remove_even(generate_list(5, 0, 10)))
#6.написать функцию, принимающую два списка и возвращающую список содержащий все уникальные элементы из этих двух
# списков
def get_unique_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.symmetric_difference(set2))
print(get_unique_elements(generate_list(5, 0, 10), generate_list(5, 0, 10)))
