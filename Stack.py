class Stack:
    
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
        
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def clear(self):
        self.items.clear()