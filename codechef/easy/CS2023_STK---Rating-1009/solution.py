def max_streak(arr):
    max_count = 0
    current_count = 0
    for x in arr:
        if x > 0:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count


t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    streak_om = max_streak(a)
    streak_addy = max_streak(b)
    
    if streak_om > streak_addy:
        print("Om")
    elif streak_addy > streak_om:
        print("Addy")
    else:
        print("Draw")
        
    t -= 1
