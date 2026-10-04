# Prime Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer n, return  *the smallest  **prime palindrome**  greater than or equal to* `n`.

An integer is  **prime**  if it has exactly two divisors: `1` and itself. Note that `1` is not a prime number.

- For example, 2, 3, 5, 7, 11, and 13 are all primes.

An integer is a  **palindrome**  if it reads the same from left to right as it does from right to left.

- For example, 101 and 12321 are palindromes.

The test cases are generated so that the answer always exists and is in the range `[2, 2 * 108]`.

 

 **Example 1:** 

```
Input: n = 6
Output: 7

```

 **Example 2:** 

```
Input: n = 8
Output: 11

```

 **Example 3:** 

```
Input: n = 13
Output: 101

```

 

 **Constraints:** 

- 1 <= n <= 108

## Solution

**Language:** Python  
**Runtime:** 259 ms (beats 12.90%)  
**Memory:** 19.3 MB (beats 74.19%)  
**Submitted:** 2026-10-04T16:11:04.856Z  

```py
class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_palindrome(x):
            return str(x) == str(x)[::-1]
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8

            
            
```

---

[View on LeetCode](https://leetcode.com/problems/prime-palindrome/)