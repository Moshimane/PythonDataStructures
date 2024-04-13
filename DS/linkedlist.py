class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_first(self, data):
        if self.head is not None:
            curr = Node(data)
            curr.next = self.head
            self.head = curr
        else:
            self.head = Node(data)
    
    def add_last(self, data):
        if self.head is not None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
        else:
            self.head = Node(data)
    
    def add_at_index(self, data, index):
        if self.head is not None:
            i = 0
            curr = self.head
            while i < index-1 and curr.next is not None:
                curr = curr.next
                i += 1
            new_node = Node(data, curr.next)
            curr.next = new_node
        else:
            self.head = Node(data)
            
    def print_list(self):
        if self.head is not None:
            curr = self.head
            while curr is not None:
                print(curr.data, end=' ')
                curr = curr.next
            print('\n')
        else:
            print('List is empty')
            
    def remove_first(self):
        if self.head is not None:
            curr = self.head
            self.head = self.head.next
            curr.next = None
            del curr
        else:
            print('List is empty')
            
    def remove_last(self):
        if self.head is not None:
            curr = self.head
            if curr.next is not None:
                temp = curr.next
                while temp.next is not None:
                    curr = curr.next
                    temp = temp.next
                curr.next = None
                del temp
            else:
                self.head = None
        else:
            print('List is empty')
            
    def check_exist(self,data):
        if self.head is not None:
            curr = self.head
            while curr is not None:
                if curr.data == data:
                    return True
                curr = curr.next
            return False
        else:
            print('List is empty')
            return False
        
    def reverse_list(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                curr = temp.next
                temp.next = curr.next
                curr.next = self.head
                self.head = curr
                curr = temp
        else:
            print('List is empty')
            