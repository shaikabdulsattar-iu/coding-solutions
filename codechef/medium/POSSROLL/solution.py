# cook your dish here
a,b,c = map(int,input().split())
if c % b == 0 and 1 <= c//b <= a:
    print("yes")
else:
    print("no")
