class Solution:
    def findMaximumPairs(self, students: str) -> int:
        count = 0
        i = 0

        while i < len(students) - 1:
            if students[i] != students[i + 1]:
                count += 1
                i += 2
            else:
                i += 1

        return count