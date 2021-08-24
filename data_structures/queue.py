from collections import deque


class Queue:
    def __init__(self):
        self.nodes = deque()
        
    def is_empty(self, nodes):
        return len(nodes) == 0
    
    def enqueue(self, node):
        self.nodes.append(node) # FIFO, so it'll be added to the end of the queue
        
    def dequeue(self):
        if not self.is_empty(self.nodes): # So in here the added item from enqueue method will be removed acc to FIFO rule
            return self.nodes.popleft()  # popleft() removes an element from the left side of the deque and returns the value.
        
    def peek(self):
        if not self.is_empty(self.nodes):
            return self.nodes[0]
    
    def get_len(self):
        return len(self.nodes)
    
    def print_queue(self):
        print(self.nodes)
        
        
    
# https://www.youtube.com/watch?v=lgpsde-1GNs&list=PL7g1jYj15RUMeIY778b8lvgUzdRFnEniI&index=2
