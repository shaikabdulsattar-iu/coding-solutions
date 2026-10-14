# cook your dish here
n = int(input())
for i in range(n):
    a = int(input())
    l1 = list(map(int,input().split()))
    l1.sort()
    if n <= 2:
        print(0)
    else:
        print(min(l1[a-1]-l1[1],l1[a-2]-l1[0]))