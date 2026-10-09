''' Structure of a Linked List Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sortLL(self, head):
        #code here
        if not head:
            return head
        values = []
        curr = head
        while curr:
            values.append(curr.data)
            curr = curr.next
        values.sort()
        curr = head
        for i in values:
            curr.data = i
            curr = curr.next
        return head    