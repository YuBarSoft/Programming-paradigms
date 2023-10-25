# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def reverse_sort(lst):
    nums = len(lst)
    for i in range(nums):
        for j in range(nums - 1 - i):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


init_list = [1, 2, 6, 3, 8, 4, 2, 1]
print(reverse_sort(init_list))
