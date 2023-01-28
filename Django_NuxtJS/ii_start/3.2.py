# -------------------------------1
# a = int(input())
# for i in range(0, a + 1):
#     print(i * '*', end='\n')
# -------------------------------2
# print(input().replace('x', '??'))
# -------------------------------3
# a = input()
# counter = 0
# for i in range(len(a)):
#     if a[i] == 'a':
#         for j in range(i, len(a)):
#             if a[j] == 'b':
#                 counter += 1
# print(counter)
# -------------------------------4
# def iterativeFib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
#
#
# print(iterativeFib(int(input())) % 1000000007)
# -------------------------------5
n = int(input())
n1 = n**0.5
n2 = n**(1/3)
n3 = n/(n1*n2)

print(int(n1+n2-n3))
