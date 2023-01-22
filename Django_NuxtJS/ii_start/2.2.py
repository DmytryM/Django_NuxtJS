# ------------------------------------------1
# print(*("какой чудесный день" for x in range(3)), sep='\n')
# ------------------------------------------2
# print(f"Как дела, {input()}?")
# ------------------------------------------3
# print(2021 - int(input()))
# ------------------------------------------4
# a, b = [int(i) for i in input().split()]
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a ** b)
# ------------------------------------------5
# a, b = int(input()), int(input())
# print((a % b) + (b//a))
# ------------------------------------------6
a, b, c = map(int, input().split())
if a + b == c:
    print(True)
else:
    print(False)