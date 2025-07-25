class stackArray:
    def __init__(self,val):
        self.stack=[]
        self.totalsize=val
        self.size=0
    
    def push_stack(self,data):
        if self.totalsize==self.size:
            print("stack is full")
            return
        self.stack.append(data)
        self.size=self.size+1

    def pop_stack(self):
        if self.size==0:
            print("stack is empty")
            return
        self.stack.pop()
        self.size=self.size-1

    def peek_stack(self):
        if self.size==0:
            print("stack is empty")
            return
        print(self.stack[-1])

    def display(self):
        if self.size==0:
            print("stack is empty")
            return
        stack_element=self.stack[::-1]
        for x in stack_element:
            print(x)

stack=stackArray(6)

stack.push_stack(1)
stack.push_stack(2)
stack.push_stack(3)
stack.push_stack(4)
stack.push_stack(5)

stack.display()
stack.pop_stack()
stack.display()

    

