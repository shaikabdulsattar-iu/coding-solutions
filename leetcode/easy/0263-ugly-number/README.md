# Ugly Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

An  **ugly number**  is a  *positive*  integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true`  *if*  `n`  *is an  **ugly number***.

 

 **Example 1:** 

```
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

```

 **Example 2:** 

```
Input: n = 1
Output: true
Explanation: 1 has no prime factors.

```

 **Example 3:** 

```
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

```

 

 **Constraints:** 

- -231 <= n <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 7.52%)  
**Submitted:** 2026-09-22T12:04:23.154Z  

```py
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=  0:
            return False    
        for i in (2,3,5):
            while n%i == 0:
                n //= i
        return n == 1   


        
```

---

[View on LeetCode](https://leetcode.com/problems/ugly-number/)