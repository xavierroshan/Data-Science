import operator
a, b, c = 5, 6, 2
print(operator.lt(5,6))
print(operator.le(5,6))
print(operator.eq(5,6))
print(operator.gt(5,6))
print(operator.ge(5,6))
print(operator.or_(a>b,b>c))
print(operator.or_(a<b,b>c))
print(operator.not_(a<b))
lst = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}
get_item = operator.itemgetter(1)
print(get_item(lst))
get_item = operator.itemgetter('b', 'c')
print(get_item(dict1))