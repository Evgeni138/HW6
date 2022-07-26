# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
#
# Найти сумму чисел списка стоящих на нечетной позиции


lst = [1, 2, 3, 5, 1, 5, 3, 10]

s = sum([lst[i] for i in range(len(lst)) if i%2 != 0])
print('s =', s)

total = sum(lst[1::2])
print('total =',total)
