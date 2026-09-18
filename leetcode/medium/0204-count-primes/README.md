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
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-18T12:21:01.607Z  

```py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        def is_prime(x: int) -> bool:
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        count = 0
        for x in range(2, n):
            if is_prime(x):
                count += 1

        return count


        
```

---

[View on LeetCode](https://leetcode.com/problems/count-primes/)