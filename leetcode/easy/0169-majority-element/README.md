# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 35.37%)  
**Memory:** 21.7 MB (beats 5.23%)  
**Submitted:** 2026-09-19T08:10:53.620Z  

```py
from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s = Counter(nums)
        for i,j in s.items():
            if j > len(nums)//2:
                return i

        
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)