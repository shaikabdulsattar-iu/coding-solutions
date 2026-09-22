# cook your dish here
t = int(input())

for _ in range(t):
    # Read the state of the three bottles
    b1, b2, b3 = map(int, input().split())
    
    # If the sum of empty bottles (0s) is >= 2, which is equivalent to sum of values <= 1
    if b1 + b2 + b3 <= 1:
        print("Water filling time")
    else:
        print("Not now")