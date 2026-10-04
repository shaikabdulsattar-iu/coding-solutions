# Counting Bits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return  *an array* `ans` *of length* `n + 1` *such that for each* `i` (`0 <= i <= n`) *,* `ans[i]` *is the  **number of*** `1` ***'s**  in the binary representation of *`i`.

Do not solve it with built-in functions (i.e., like `__builtin_popcount` in C++).

 

 **Example 1:** 

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

```

 **Example 2:** 

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```

 

 **Constraints:** 

- 0 <= n <= 105

 

 **Follow up:** 

- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 33.91%)  
**Memory:** 20.3 MB (beats 15.82%)  
**Submitted:** 2026-10-04T16:05:13.233Z  

```py
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ans[i >> 1] is the bit count of i // 2
            # (i & 1) checks if the least significant bit is 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/counting-bits/)