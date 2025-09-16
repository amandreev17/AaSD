 class Node:
     def __init__(self, key):
         self.key = key
         self.next = None


 class LinkedList:
     def __init__(self):
         self.head = None

     def insert_at_begin(self, key):
         new_node = Node(key)
         new_node.next = self.head
         self.head = new_node

     def reverse_list(self):
         if self.head is None or self.head.next is None:
             return
         first = self.head
         second = self.head.next
         third = self.head.next.next
         if third is None:
             first.next = None
             second.next = first
             self.head = second
             return
         first.next = None
         while second.next:
             third_node = third.next
             second.next = first
             first = second
             second = third
             third = third_node
             self.head = first
         second.next = first
         self.head = second

     def printL(self):
         if self.head is None:
             print("Not elements")
             return
         current_node = self.head
         while current_node:
             print(current_node.key)
             current_node = current_node.next


 llist = LinkedList()

 llist.insert_at_begin(2)
 llist.insert_at_begin(1)
 llist.printL()
 print()
 llist.reverse_list()
 llist.printL()
 print()
 llist.insert_at_begin(3)
 llist.printL()
 print()
 llist.reverse_list()
 llist.printL()
