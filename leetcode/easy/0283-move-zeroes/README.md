# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 577 ms (beats 6.85%)  
**Memory:** 20.3 MB (beats 98.38%)  
**Submitted:** 2026-10-02T08:27:40.464Z  

```py
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = []
        while 0 in nums:
            nums.remove(0)
            l.append(0)
        nums.extend(l)            
        
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)