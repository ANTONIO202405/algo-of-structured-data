# Stack 
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def print_stack(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next
    def push(self,value):
        new_node=Node(value)
        if self.top is None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
    def pop(self):
        if self.top is None:
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
        self.height-=1
    
    


my_stack=Stack(8)
my_stack.push(5)
my_stack.pop()
my_stack.print_stack()


# Queue
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
    def dequeue(self):
        if self.first is None:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1


my_queue=Queue(2)
my_queue.enqueue(5)
my_queue.dequeue()
my_queue.print_queue() 