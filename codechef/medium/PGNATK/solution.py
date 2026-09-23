T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(N + (N - 1) // (K - 1))