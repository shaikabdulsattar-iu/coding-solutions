# Intersection of Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer arrays `nums1` and `nums2`, return  *an array of their intersection*. Each element in the result must be  **unique**  and you may return the result in  **any order**.

 

 **Example 1:** 

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

 **Example 2:** 

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 31 ms (beats 5.35%)  
**Memory:** 19.5 MB (beats 12.38%)  
**Submitted:** 2026-10-07T12:54:27.958Z  

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = set(nums1)
        l1 = set(nums2)
        l2 = []
        for i in l:
            for j in l1:
                if i == j:
                    l2.append(i)
        return l2            
        
```

---

[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)