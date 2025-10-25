#Doubly LinkedList

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        print(f"Head: {self.head.value}")
        print(f"Tail: {self.tail.value}")
    def append(self,value):
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(value)
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    def pop(self):
        if self.head==None:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return f"Removed Element--> {temp}"
    def get(self,index):
        if self.head==None:
            return None
        if index < self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        temp=self.get(index)
        pre=self.get(index-1)
        if temp and pre:
            new_node.next=temp
            temp.prev=new_node
            new_node.prev=pre
            pre.next=new_node
            self.length+=1
            return True
        
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        after=self.get(index)
        after.next.prev=after.prev
        after.prev.next=after.next
        after.prev=None
        after.next=None
        self.length-=1
        return True
    def swap_pairs(self):
        if self.head==None or self.length==1:
            return None
        
        else:
            pre=self.head.next
            temp=pre.next
            new=self.head.next
            while True:
                pre.next=None
                pre.next=pre.prev
                if temp is not None and temp.next is not None:
                    pre.prev.next=temp.next
                    pre=temp.next
                    temp=pre.next
                else:
                    pre.prev.next=temp
                    break
            self.head=new
            

my_doubly_linked_list=DoublyLinkedList(7)
my_doubly_linked_list.append(5)
#my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.prepend(10)
my_doubly_linked_list.append(1)
my_doubly_linked_list.set_value(4,3)
my_doubly_linked_list.insert(0,0)
#my_doubly_linked_list.remove(1)
#my_doubly_linked_list.remove(4)
#print(my_doubly_linked_list.get(5))
my_doubly_linked_list.print_list()


my_doubly_linked_list=DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
#my_doubly_linked_list.append(5)

my_doubly_linked_list.print_list()
my_doubly_linked_list.swap_pairs()
my_doubly_linked_list.print_list()
