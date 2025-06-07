# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(8, 8)   # count é um contador sem final  definido
r1 = range(8, 100, 8)  # range é um contador com um final definido


print('c1', hasattr(c1, '__iter__'))  # count é um iteravel, então ele tem um iterator
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))  # range não é um iteravel, então ele não tem um iterator

print('count')
for i in c1:
    if i > 10:
        break
    print(i)

print()
print('range')
print('count')
for i in r1:
    if i > 10:
        break
    print(i)