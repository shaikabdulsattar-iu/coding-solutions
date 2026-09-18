# Count Primes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return  *the number of prime numbers that are strictly less than*  `n`.

 

 **Example 1:** 

```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

```

 **Example 2:** 

```
Input: n = 0
Output: 0

```

 **Example 3:** 

```
Input: n = 1
Output: 0

```

 

 **Constraints:** 

- 0 <= n <= 5 * 106

## Solution

**Language:** Python  
**Runtime:** 2973 ms (beats 48.44%)  
**Memory:** 108.6 MB (beats 11.35%)  
**Submitted:** 2026-09-18T12:22:36.649Z  

```py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                is_prime[p * p : n : p] = [False] * len(range(p * p, n, p))
                
        return sum(is_prime)

        
```

---

[View on LeetCode](https://leetcode.com/problems/count-primes/)