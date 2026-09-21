# cook your dish here
n  = int(input())
l1 = list(map(int,input().split()))
c = 0
for i in l1:
    if i % 2 == 0:
        c += 1
if c == n :
    print("ready for battle")
else:
    print("not ready")