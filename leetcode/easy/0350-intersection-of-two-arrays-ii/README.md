# Intersection of Two Arrays II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer arrays `nums1` and `nums2`, return  *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in  **any order**.

 

 **Example 1:** 

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

 **Example 2:** 

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

 

 **Follow up:** 

- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 5.28%)  
**Memory:** 19.3 MB (beats 85.51%)  
**Submitted:** 2026-10-03T05:05:06.555Z  

```py
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = []
        nums2_copy = list(nums2)
        
        for i in nums1:
            for j in nums2_copy:
                if i == j:
                    l.append(i)
                    nums2_copy.remove(j)  
                    break                 
                    
        return l
```

---

[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)