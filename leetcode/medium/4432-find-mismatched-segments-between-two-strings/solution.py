class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        k = 0
        while k < len(s1):
            if s1[k] != s2[k]:
                j = k
                while k < len(s1) and s1[k] != s2[k]:
                    k += 1
                res.append([s1[j:k],s2[j:k]])
            else:
                k += 1
        return res       
        