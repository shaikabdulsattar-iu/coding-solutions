# Three Divisors

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return `true` *if* `n` *has  **exactly three positive divisors**. Otherwise, return* `false`.

An integer `m` is a  **divisor**  of `n` if there exists an integer `k` such that `n = k * m`.

 

 **Example 1:** 

```
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

```

 **Example 2:** 

```
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

```

 

 **Constraints:** 

- 1 <= n <= 104

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 13.49%)  
**Memory:** 19.3 MB (beats 50.24%)  
**Submitted:** 2026-09-18T12:40:47.100Z  

```py
class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(1,n+1):
            if n % i == 0:
                c += 1
        return c == 3        

        
```

---

[View on LeetCode](https://leetcode.com/problems/three-divisors/)