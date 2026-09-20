import heapq
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []
        count = 0
        for i,j in intervals:
            while heap and heap[0]<i:
                heapq.heappop(heap)
            count += len(heap)
            heapq.heappush(heap,j)
        return count    
        