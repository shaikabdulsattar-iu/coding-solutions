# cook your dish here
x,y,a,b = map(int,input().split())
if x < a or (x == a and y < b):
    print("Bob")
else:
    print("Alice")
