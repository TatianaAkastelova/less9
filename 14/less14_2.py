list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

result1 = list(filter(lambda x: not x % 2, list_1))
print(result1)
result2 = list(filter(lambda x: not x % 2, list_3))
print(result2)
result3 = list(filter(lambda x: x % 2, list_2))
print(result3)
a = list(zip(result1,result2,result3))
print(a)
y = list(map(sum,a))
print(y)
result4 = list(filter(lambda x: x % 2, y))
print(result4)