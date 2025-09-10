class Maxstack:
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self,x):
        self.stack.append(x)

        if self.max:
            if x >= self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)

    def pop(self):
        if self.stack[-1]==self.max[-1]:
            self.stack.pop()
            self.max.append()
        else:
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getmax(self):
        return self.max[-1]
        
        
obj = Maxstack()
obj.push(2)
obj.push(7)
obj.push(1)
obj.pop()
obj.push(6)
result_top = obj.top()
print("the top value is",result_top)

result_max = obj.getmax()
print("the maximam value is",result_max)