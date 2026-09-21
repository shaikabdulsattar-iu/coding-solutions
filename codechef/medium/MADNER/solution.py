class Solution:
    def findMaximumPairs(self, students: str) -> int:
        c = 0
        if 'xy' or 'yx' in students:
            c += 1
        return c        
        # write your code here
        