# -------------------------------1
# class MyNum:
#     def __init__(self, val):
#         self.val = val
#
#     def __add__(self, other):
#         return MyNum(self.val + other)
#
#     def get_val(self):
#         return self.val

# -------------------------------2
# class MyQueue:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val):
#         self.stack.append(val)
#
#     def front(self):
#         return self.stack[0]
#
#     def pop(self):
#         del self.stack[0]

# -------------------------------3
class Neuron:
    prev_x = list()

    def __init__(self, w, f=lambda x: x):
        self.weight = w
        self.func = f
        prev_x = None

    def forward(self, x):
        self.prev_x = x
        result = sum(map(lambda i1, i2: i1 * i2, self.weight, x))
        return self.func(result)

    def backlog(self):
        return self.prev_x

