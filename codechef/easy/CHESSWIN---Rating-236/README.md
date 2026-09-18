# CHESSWIN - Rating 236

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chess Win

You are playing many chess matches against Magnus. Every match is either a win or loss.

Unsurprisingly, you are currently losing. The current score is $A:B$, where $A$ is the number of matches you have won, and $B$ is the number of matches Magnus has won.

You want to beat Magnus, i.e. win more matches than Magnus at the end. What is the minimum number of matches you still need to play to have any chance of being able to beat him?

### Input Format
- The only line contains $2$ integers - $A$ and $B$, the current score.
### Output Format

For each test case, output the number of matches you still need to play.

### Constraints
- $0 \le A \lt B \le 5$
### Sample 1:
Input
Output

```
0 1

```

```
2

```

### Explanation:

If you play $2$ more matches, it is possible that you win both and end up with a score of $2:1$, and beat Magnus.

### Sample 2:
Input
Output

```
2 4

```

```
3

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T17:05:49.431Z  

```c_cpp
#include <stdio.h>

int main() {
    int A, B;
    // Read the current scores
    if (scanf("%d %d", &A, &B) == 2) {
        // Calculate the minimum number of matches to play
        int ans = B - A + 1;
        // Print the result
        printf("%d\n", ans);
    }
    
    return 0;
}


```

---

[View on CodeChef](https://www.codechef.com/problems/CHESSWIN)