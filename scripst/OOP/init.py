class MyNum(object):
    def __init__(self, value):
        print("calling __init__")
        self.val = value

    def increment(self):
        self.val += 1


dd = MyNum()
dd.increment()
dd.increment()
print(dd.val)
