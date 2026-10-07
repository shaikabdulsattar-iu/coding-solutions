# cook your dish here
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    s = input()
    l = input()
    left = set(l)
    count = 1
    ans = 1
    pre = s[0] in left
    for i in s[1:]:
        now = i in left
        if now == pre:
            count += 1
        else:
            count = 1
        ans = max(ans,count)
        pre = now
    print(ans)        
            
    
    
    