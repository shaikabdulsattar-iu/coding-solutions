T = int(input())
for _ in range(T):
    X = int(input())
    if X > 5000:
        X -= 500
    elif X > 1000:
        X -= 100
    elif X > 100:
        X -= 25
    print(X)
