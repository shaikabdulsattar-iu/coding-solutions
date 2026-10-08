class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 3 or n == 1:
            return n
        return (n*(n+1))//2    
        