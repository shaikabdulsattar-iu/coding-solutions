# Single Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **non-empty**  array of integers `nums`, every element appears  *twice*  except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

 **Example 1:** 

 **Input:**  nums = [2,2,1]

 **Output:**  1

 **Example 2:** 

 **Input:**  nums = [4,1,2,1,2]

 **Output:**  4

 **Example 3:** 

 **Input:**  nums = [1]

 **Output:**  1

 

 **Constraints:** 

- 1 <= nums.length <= 3 * 104
- -3  *104 <= nums[i] <= 3*  104
- Each element in the array appears twice except for one element which appears only once.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 64.97%)  
**Memory:** 21.9 MB (beats 10.84%)  
**Submitted:** 2026-09-18T05:52:49.546Z  

```py
from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = Counter(nums)
        for key,values in s.items():
            if values == 1:
                return key
        
```

---

[View on LeetCode](https://leetcode.com/problems/single-number/)