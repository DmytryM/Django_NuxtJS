# -------------------------------1
# def almost_double_factorial(n):
#     res = 1
#     for i in range(n + 1):
#         if i % 2 != 0:
#             res *= i
#     return res
#
#
# res = almost_double_factorial(int(input()))
# print(res)
# -------------------------------2
# count = -1
# def calls_num():
#     global count
#     count += 1
#     return count
# print(calls_num())
# print(calls_num())
# print(calls_num())
# print(calls_num())
# -------------------------------3
# nums = []
# def cmp_prev(val):
#     global nums
#     if len(nums) == 0:
#         if val != 0:
#             nums.append(val)
#             return True
#         elif val == 0:
#             nums.append(val)
#             return False
#     elif 2 > len(nums) > 0:
#         if val > nums[len(nums) - 1]:
#             nums.append(val)
#             return True
#         else:
#             nums.append(val)
#             return False
#     elif len(nums) >= 2:
#         if val > (nums[len(nums) - 2] + nums[len(nums) - 1]):
#             nums.append(val)
#             return True
#         else:
#             nums.append(val)
#             return False
#
# print(cmp_prev(2))
# print(nums)
# print(cmp_prev(0))
# print(nums)
# print(cmp_prev(3))
# print(nums)
# -------------------------------3
