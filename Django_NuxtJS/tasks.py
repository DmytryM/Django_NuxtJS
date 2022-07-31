# x = input().split(',')
# y = int(input())
# for i in range(len(x)):
#     for j in range(len(x)):
#         if int(x[i]) + int(x[j]) == y and i != j:
#             print(f"[{i}, {j}]")
#             exit()


# --------------------2-------------------

# s = input().split()
# res = [len(s[-1]) if len(s) > 1 else 0]
# print(*res)

# --------------------3-------------------

# import math
# print(int(math.sqrt(int(input()))))

# --------------------4-------------------

# s = input().split(',')
# b = []
# minimal = min((word for word in s if word), key=len)
# s.remove(minimal)
# for i in range(len(s)):
#     for j in minimal:
#         index = minimal.index(j)
#         if j != s[i][index] or s[i][index] in b:
#             break
#         else:
#             b.append(j)
#             # print(j, end='')
# print(*b)

# --------------------5-------------------

# print(list(set(map(int, input().split(',')))))

# --------------------6-------------------

# print(input().find(input()))

# --------------------7-------------------

# s = input()
# print(s.count('A') <= 1 and 'LLL' not in s)

# --------------------8-------------------

# from functools import reduce
#
#
# def func(a, b):
#     return a * b
#
#
# nums = [int(i) for i in input().split(',')]
# total = reduce(func, nums, 1)
# print(total)

# --------------------9-------------------

# nums = [int(i) for i in input().split(',')]
# lst = [x for x in range(len(nums) - 1) if nums[x] > nums[x + 1]]
# print(('YES', 'NO')[len(lst) > 1])

# --------------------10-------------------

# res = 1
# try:
#     nums = [int(i) for i in input().split(',')]
#     for i in range(len(nums) - 1):
#         if nums[i] < nums[i + 1]:
#             res += 1
#         else:
#             break
#     print(res)
# except ValueError:
#     print(0)

# --------------------11-------------------

# nums = [int(i) for i in  input().split(',')]
# if len(nums) % 2 == 0:
#     print(-1)
# print(nums)

# --------------------12-------------------

# print(sorted(map(lambda x: x ** 2, [int(i) for i in  input().split(',')])))

# --------------------13-------------------

# address = input()
# print(address.replace('.', '[.]'))

# --------------------14-------------------

# a = [int(i) for i in  input().split(',')]
# lst = [i for i in a if i % 2 == 0]
# [lst.append(x) for x in a if x % 2 == 1]
# print(lst)

# --------------------15-------------------