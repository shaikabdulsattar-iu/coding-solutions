# Bitwise AND of Numbers Range

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two integers `left` and `right` that represent the range `[left, right]`, return  *the bitwise AND of all numbers in this range, inclusive*.

 

 **Example 1:** 

```
Input: left = 5, right = 7
Output: 4

```

 **Example 2:** 

```
Input: left = 0, right = 0
Output: 0

```

 **Example 3:** 

```
Input: left = 1, right = 2147483647
Output: 0

```

 

 **Constraints:** 

- 0 <= left <= right <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 44.70%)  
**Memory:** 19.3 MB (beats 55.41%)  
**Submitted:** 2026-10-04T16:06:47.394Z  

```py
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
```

---

[View on LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)