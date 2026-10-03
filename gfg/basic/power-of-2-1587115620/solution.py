class Solution:
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        # code here
        while n % 2 == 0:
            n //= 2
        return n == 1        