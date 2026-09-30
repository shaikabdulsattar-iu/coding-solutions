# cook your dish here
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a % 2 == 0 or b % 2 == 0:
        print("yes")
    else:
        print("no")