# x = input().split(',')
# y = int(input())
# for i in range(len(x)):
#     for j in range(len(x)):
#         if int(x[i]) + int(x[j]) == y and i != j:
#             print(f"[{i}, {j}]")
#             exit()


#--------------------2-------------------

# s = input().split()
# res = [len(s[-1]) if len(s) > 1 else 0]
# print(*res)

#--------------------3-------------------

# import math
# print(int(math.sqrt(int(input()))))

#--------------------4-------------------

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

#--------------------5-------------------

# print(list(set(map(int, input().split(',')))))

#--------------------6-------------------

# print(input().find(input()))

#--------------------7-------------------

a = int(input())
b = int(input())
print(bin(a) + bin(b))

