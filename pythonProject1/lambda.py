# def rev(num):
#     return num[-1]

my_list = [1, 2, 3, 4, 5]
print(list(map(lambda num: num ** 2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# print(a[0][1])
a.sort(key= lambda num: num[1])
print(a)

print(list(map(lambda num: sorted(num), a)))