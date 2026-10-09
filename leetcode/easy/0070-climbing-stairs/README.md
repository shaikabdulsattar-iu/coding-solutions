# Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

 **Example 1:** 

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

 **Example 2:** 

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

 

 **Constraints:** 

- 1 <= n <= 45

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19 MB  
**Submitted:** 2026-10-09T06:24:10.197Z  

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        prev1, prev2 = 3, 2
        for _ in range(4, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1
```

---

[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)