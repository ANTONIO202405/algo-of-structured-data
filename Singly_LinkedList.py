# Singly LinkedList
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
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
    def Append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        temp=self.head
        self.head=new_node
        self.head.next=temp
        self.length+=1
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
    def get(self,index):
        if index<0 or index>self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.Append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    def remove(self,index):
        if index<=0 or index>self.length:
            return False
        if index==0:
            return self.pop_first()
        if index==self.length:
            return self.pop()
        prev=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
    def reverse_between(self,start_index,end_index):
        start=self.head
        end=self.head
        pre=self.head
        if self.head==None or self.length==1:
            return None
        else:
            for _ in range(start_index):
                start=start.next
            for _ in range(end_index):
                end=end.next
            if start_index==0:
                self.head=end
            else:
                for _ in range(start_index-1):
                    pre=pre.next
            before=start
            temp=before.next
            before.next=None
            for _ in range(start_index,end_index):
                after=temp.next
                temp.next=before
                before=temp
                temp=after
            pre.next=end
            start.next=temp
my_linked_list=LinkedList(2)
#my_linked_list.pop()
my_linked_list.Append(3)
my_linked_list.Append(4)
my_linked_list.Append(5)
#print(my_linked_list.pop())
my_linked_list.prepend(1)
#print(my_linked_list.get(0))
#my_linked_list.set_value(1,3)
#my_linked_list.pop_first()
#my_linked_list.insert(0,1)
#print(my_linked_list.remove(2))
#my_linked_list.reverse()
#print(f"Head:{my_linked_list.head.value}")
#print(f"Tail:{my_linked_list.tail.value}")
#print(f"Length:{my_linked_list.length}")
my_linked_list.reverse_between(2,4)
my_linked_list.pop_first()
my_linked_list.print_list()


import sys
# ...existing code...

def linked_list_memory_usage(ll):
    total = sys.getsizeof(ll)
    node = ll.head
    while node:
        total += sys.getsizeof(node)
        total += sys.getsizeof(node.value)
        node = node.next
    return total

# Example usage:
print("Approximate memory usage (bytes):", linked_list_memory_usage(my_linked_list))
# ...existing code...
