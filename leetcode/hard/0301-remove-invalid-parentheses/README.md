# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 491 ms (beats 33.61%)  
**Memory:** 22.1 MB (beats 5.70%)  
**Submitted:** 2026-10-07T03:18:46.673Z  

```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            i= 0
            ctr = 0
            while i<len(s):
                if s[i]== '(':
                    ctr += 1
                elif s[i] == ")":
                    if ctr == 0:
                        return False
                    ctr -= 1
                
                i +=1
            
            return ctr == 0
        
        level ={s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for i in range(len(s)) for s in level}
        
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)