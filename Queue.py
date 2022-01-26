class Queue:
    
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None
    
    def get_size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()