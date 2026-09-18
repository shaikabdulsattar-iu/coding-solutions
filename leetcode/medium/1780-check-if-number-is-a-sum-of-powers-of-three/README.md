# Check if Number is a Sum of Powers of Three

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return `true`  *if it is possible to represent* `n` *as the sum of distinct powers of three.*  Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3x`.

 

 **Example 1:** 

```
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

```

 **Example 2:** 

```
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

```

 **Example 3:** 

```
Input: n = 21
Output: false

```

 

 **Constraints:** 

- 1 <= n <= 107

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 29.72%)  
**Submitted:** 2026-09-18T12:38:27.691Z  

```py
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True      


        
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)