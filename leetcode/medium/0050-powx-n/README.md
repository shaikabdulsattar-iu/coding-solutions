# Pow(x, n)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `xn`).

 

 **Example 1:** 

```
Input: x = 2.00000, n = 10
Output: 1024.00000

```

 **Example 2:** 

```
Input: x = 2.10000, n = 3
Output: 9.26100

```

 **Example 3:** 

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

```

 

 **Constraints:** 

- -100.0 < x < 100.0
- -231 <= n <= 231-1
- n is an integer.
- Either x is not zero or n > 0.
- -104 <= xn <= 104

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 28.59%)  
**Memory:** 19.6 MB (beats 21.29%)  
**Submitted:** 2026-09-18T12:12:22.899Z  

```py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
```

---

[View on LeetCode](https://leetcode.com/problems/powx-n/)