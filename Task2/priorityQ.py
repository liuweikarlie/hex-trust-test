from queue import PriorityQueue



class priorityQA():
    def __init__(self):
        self.queue = PriorityQueue()
        self.max_size=5

    def push(self,price, quantity):
        self.queue.put((price,quantity))
        

    def pop(self):
        
        return self.queue.get()  # remove the smallest element

    def get_size(self):
        return self.queue.qsize()
    
    def empty(self):
        return self.queue.empty()
    
    def full(self):
        if self.queue.qsize()==self.max_size:
            return True
        else:
            return False
    
    def update(self, price, new_quantity):
        update=0
        for i in range(len(self.queue.queue)):
            if self.queue.queue[i][0] == price:
                self.queue.queue[i] = (price, new_quantity)
                # Maintain heap property after update (optional)
                # self.queue._heapify_pos(i)  # Access private method for update
                update=1
                break
        if update==0:
            self.push(price, new_quantity)
           



class priorityQB():
    def __init__(self):
        self.queue = PriorityQueue()

    def push(self,price, quantity):
        self.queue.put(((-price),quantity))

    def pop(self):
        data=self.queue.get()  # remove the largest element
        return (-data[0],data[1])

    def get_size(self):
        return self.queue.qsize()
    
    def empty(self):
        return self.queue.empty()
    
    def full(self):
        return self.queue.full()
    
    def update(self, price, new_quantity):
        update=0
        for i in range(len(self.queue.queue)):
            if self.queue.queue[i][0] == -price:
                self.queue.queue[i] = (-price, new_quantity)
                update=1
                break
        
        if update==0:
            self.push(-price, new_quantity)
    
            
        
    
    
    