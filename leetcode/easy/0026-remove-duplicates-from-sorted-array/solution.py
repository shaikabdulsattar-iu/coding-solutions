class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = set(nums)
        return len(sorted(n))