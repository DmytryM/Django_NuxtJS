# -------------------------------1
class MyNum:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return MyNum(self.val + other)

    def get_val(self):
        return self.val

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

    def __init__(self, w, f = lambda x: x):
        #YOUR CODE HERE

    def forward(self, x):
        #YOUR CODE HERE

    def backlog(self):
        #YOUR CODE HERE

