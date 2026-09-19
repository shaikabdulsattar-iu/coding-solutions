# Add Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two non-negative integers, `num1` and `num2` represented as string, return  *the sum of*  `num1`  *and*  `num2`  *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

 

 **Example 1:** 

```
Input: num1 = "11", num2 = "123"
Output: "134"

```

 **Example 2:** 

```
Input: num1 = "456", num2 = "77"
Output: "533"

```

 **Example 3:** 

```
Input: num1 = "0", num2 = "0"
Output: "0"

```

 

 **Constraints:** 

- 1 <= num1.length, num2.length <= 104
- num1 and num2 consist of only digits.
- num1 and num2 don't have any leading zeros except for the zero itself.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 94.41%)  
**Memory:** 19.5 MB (beats 58.37%)  
**Submitted:** 2026-09-19T04:48:20.691Z  

```py
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n=int(num1)
        n1=int(num2)
        n2=n+n1
        return str(n2)
```

---

[View on LeetCode](https://leetcode.com/problems/add-strings/)