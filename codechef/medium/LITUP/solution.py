import heapq

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    heap = []
    ans = float('inf')

    for j in range(1, N + 1):

        # Add possible position for the first light
        i = j - 1

        if 1 <= i <= K + 1:
            heapq.heappush(heap, (C[i - 1], i))

        # Remove lights that are too far from j
        while heap and heap[0][1] < j - 2 * K - 1:
            heapq.heappop(heap)

        # Second light must illuminate stall N
        if j >= N - K and heap:
            ans = min(ans, C[j - 1] + heap[0][0])

    print(ans if ans != float('inf') else -1)