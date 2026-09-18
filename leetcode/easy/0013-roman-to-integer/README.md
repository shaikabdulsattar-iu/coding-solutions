# Roman to Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

 **Example 1:** 

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

 **Example 2:** 

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

 **Example 3:** 

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

 

 **Constraints:** 

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 41.21%)  
**Memory:** 19 MB (beats 99.73%)  
**Submitted:** 2026-09-18T05:12:41.667Z  

```py
class Solution:
    def romanToInt(self, s: str) -> int:
        s = (
            s.replace("IV", "a")
            .replace("IX", "b")
            .replace("XL", "c")
            .replace("XC", "d")
            .replace("CD", "e")
            .replace("CM", "f")
        )

        sum_ = 0
        for i in s:
            if i == "a":
                sum_ += 4
            elif i == "b":
                sum_ += 9
            elif i == "c":
                sum_ += 40
            elif i == "d":
                sum_ += 90
            elif i == "e":
                sum_ += 400
            elif i == "f":
                sum_ += 900
            elif i == "I":
                sum_ += 1
            elif i == "V":
                sum_ += 5
            elif i == "X":
                sum_ += 10
            elif i == "L":
                sum_ += 50
            elif i == "C":
                sum_ += 100
            elif i == "D":
                sum_ += 500
            elif i == "M":
                sum_ += 1000

        return sum_
```

---

[View on LeetCode](https://leetcode.com/problems/roman-to-integer/)