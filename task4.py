# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



n = int(input('n --> '))
lam = lambda i: 3 * i + 1
dic = dict({i: lam(i) for i in range(1, n + 1)})
print(dic)


dic2 = dict(enumerate(list(map(lambda i: 3 * i + 1, range(1, n + 1))), 1))
print(dic2)
