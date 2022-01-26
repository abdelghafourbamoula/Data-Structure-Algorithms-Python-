class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
       
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        ''' insert data at the head of the linked list.'''
        
        self.head = Node(data, self.head)
        
    def add_at_end(self, data):
        ''' insert data at the last item of the linked list.'''
        
        if not self.head:
            self.head = Node(data, self.head)
            return
            
        c = self.head
        while c.next != None:
            c = c.next
        c.next = Node(data, None)
        
    def add_at(self, index, data):
        '''add data at the given index.'''
        
        if index > self.length() or index < 0:
            raise Exception("Invalid Index !")
        
        i,curr = 0, self.head
        while curr.next:
            if i == index-1:
                node = Node(data, curr.next)
                curr.next = node
                break
            
            curr = curr.next
            i += 1
        
    def remove_at(self, index):
        '''remove data from the given index.'''
        
        if index > self.length() or index < 0:
            raise Exception("Invalid Index !")
        
        if index == 0:
            self.head = self.head.next
            return
            
        i,curr = 0, self.head
        while curr.next:
            if i == index-1 :
                curr.next = curr.next.next
                break
                
            curr = curr.next
            i += 1
        
    def print(self):
        '''print the linked list items.'''
        
        if self.head is None:
            print("Linked List is empty ..")
            return
        
        n = self.head
        while n != None:
            print(n.data, end=" --> ")
            n = n.next
        print('(',None,')')
        
    def length(self):
        '''get the lenth ofthe linked list'''
        
        c = 0
        n = self.head
        while n:
            c +=1
            n = n.next
            
        return c
    
    def insert_after_value(self, data_after, data_inert):
        '''insert data after the given value node.'''
        
        if self.head is None:
            print("Linked List is empty ..")
            return
        
        curr = self.head
        while curr:
            if curr.data == data_after:
                node = Node(data_inert, curr.next)
                curr.next = node
                return
            
            curr = curr.next
            
        print("Invalid data .. ")
        
    def remove_by_value(self, value):
        '''remove first node that contain given data'''
        
        if self.head is None:
            print("Linked List is empty ..")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
            
        curr = self.head
        while curr.next:
            if curr.next.data == value:
                curr.next = curr.next.next
                return
            curr = curr.next
            
        print("Invalid data .. ")