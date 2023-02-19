# -------------------------------1
class MyNum:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return MyNum(self.val + other)

    def get_val(self):
        return self.val

# -------------------------------2
