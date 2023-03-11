from dataclasses import dataclass

@dataclass
class Node:
    val : int 
    next : int = None

@dataclass
class LinkedList:
    head : int = None

    def display(self):
        if self.head is None:
            return "String is empty"
        itr = self.head
        l = []
        while itr:
            l.append(itr.val)
            itr = itr.next
        print(l)
    
    def add_node(self, ele):
        node = Node(ele)
        node.next = self.head
        self.head = node


ll = LinkedList()
ll.add_node(8)
ll.add_node(19)
ll.display()
