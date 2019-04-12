class Stack:
    def __init__(self):
        self.items = []

    
    def is_empty(self):
        return self.items == []


    def push(self, item):
        self.items.append(item)

    
    def pop(self):
        return self.items.pop()

    
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



def rev_string(my_str):
    final_string = []
    while not my_str.is_empty():
        final_string.append(my_str.pop())


mimi = Stack()
mimi.push('ulemzi')

print(rev_string(mimi))



m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    m.pop()
    m.pop()
print(m.peek())