# x = input().split(',')
# y = int(input())
# for i in range(len(x)):
#     for j in range(len(x)):
#         if int(x[i]) + int(x[j]) == y and i != j:
#             print(f"[{i}, {j}]")
#             exit()


#--------------------2-------------------

s = input().split()
res = [len(s[-1]) if len(s) > 1 else 0]
print(*res)