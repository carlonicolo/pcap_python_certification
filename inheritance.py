class Super:
    def __init__(self):
    # Add your code here
      self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        # Add your code here
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
