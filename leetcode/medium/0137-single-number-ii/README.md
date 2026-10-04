# Single Number II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` where every element appears  **three times**  except for one, which appears  **exactly once**.  *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

 **Example 1:** 

```
Input: nums = [2,2,3,2]
Output: 3

```

 **Example 2:** 

```
Input: nums = [0,1,0,1,0,1,99]
Output: 99

```

 

 **Constraints:** 

- 1 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each element in nums appears exactly three times except for one element which appears once.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 71.30%)  
**Memory:** 20.9 MB (beats 28.83%)  
**Submitted:** 2026-10-04T16:09:14.607Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1
        
        for key,value in freq.items():
            if value==1:
                return key
        
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-ii/)