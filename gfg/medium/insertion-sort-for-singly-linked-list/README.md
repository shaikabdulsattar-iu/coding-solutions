# Sort Singly Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a singly linked list, sort the list in ascending order.

 **Examples:** 

```
Input: head: 30->23->28->30->11->14->19->16->21->25 
Output: 11->14->16->19->21->23->25->28->30->30 
Explanation: The resultant linked list is sorted.

```

```
Input: head: 19->20->16->24->12->29->30 
Output: 12->16->19->20->24->29->30
Explanation: The resultant linked list is sorted.

```

 **Constraints:** 
0 ≤ number of nodes ≤ 103
0 ≤ node->data ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T05:22:45.158Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/insertion-sort-for-singly-linked-list/1)