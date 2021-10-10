# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
## Linked  List
## functions and classes
class Node:
    def __init__(self,data=None,next=None):
        self.data=data;
        self.next=next;
class Linkedlist:
    def __init__(self):
        self.head=None

    def add_begin(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        new_node.next=next
    def print(self):
        if self.head is None:
            print("The Linked  List is Empty");

        n = self.head
        str1=' '
        while n is not None:
            str1 += 'str(n.data) ' + '-->'
            n = n.next;
            print(str1)

    ##def add_ending(self, data):
        ##new_node = Node(data)
        ##new_node.next = None
        ##new_node = self.head



if __name__ == '__main__':
    ll1=Linkedlist()
    ll1.add_begin(14)
    ll1.add_begin(41)