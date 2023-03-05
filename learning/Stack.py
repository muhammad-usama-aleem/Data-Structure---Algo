# Using a list as a stack
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

# get last element and remove from stack
s.pop()

# peak at the last added element from stack
s[-1]





# using collection.deque as a stack

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def check_val(self, val):
        # check if given value exist in stack
        return self.container.count(val)
      

      
s = Stack()

s.push(34)
s.push(34)
s.push(34)
s.push(34)
s.push(78)
s.push(12)
s.check_val(34)
