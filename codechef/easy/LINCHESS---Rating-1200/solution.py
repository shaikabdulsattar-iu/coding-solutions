
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        p_list = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        best_p = -1
        max_p = -1
        
        for p in p_list:
            if k % p == 0:
                if p > max_p:
                    max_p = p
                    best_p = p
        
        results.append(str(best_p))
        
    print("\n".join(results))

if __name__ == "__main__":
    solve()