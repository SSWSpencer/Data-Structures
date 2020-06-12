"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if(self.storage):
#             output = self.storage[0]
#             self.storage.pop(0)
#             return output
#         else:
#             return None
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class Queue: 
    def __init__(self): 
        self.front = self.rear = None

    def isEmpty(self): 
        return self.front == None

    def __len__(self):
        temp = self.front
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count


    def enqueue(self, item): 
        temp = Node(item) 

        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    def dequeue(self): 
          
        if self.isEmpty(): 
            return None
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
        return temp.data