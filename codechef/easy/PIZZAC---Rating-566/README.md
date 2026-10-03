# PIZZAC - Rating 566

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pizza Cutting

Chef has a circular pizza and a knife to cut that into pieces. He can only cut the pizza in a way such that the knife starts from the boundary of the pizza, passes the centre, and ends at the boundary.

Find whether Chef an divide the pizza into $N$ pieces using any (possibly zero) number of cuts.

Some valid cuts are:

Whereas, the following cuts are invalid:

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$ — denoting the desired number of cuts.
### Output Format

For each test case, output on a new line, `YES`, if Chef can divide the pizza into $N$ pieces using any (possibly zero) number of cuts, and `NO` otherwise.

Note that you may print each character in uppercase or lowercase. For example, the strings `NO`, `no`, `No`, and `nO` are considered the same.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
### Sample 1:
Input
Output

```
4
1
2
3
4

```

```
YES
YES
NO
YES

```

### Explanation:

 **Test case $1$:**  Chef can have single piece of pizza by making zero cuts.

 **Test case $2$:**  Refer the first image in valid cuts. Chef has divided the pizza into two pieces by making one cut.

 **Test case $3$:**  It is not possible for Chef to divide the pizza into $3$ pieces by using only valid cuts.

 **Test case $4$:**  Refer the second and third image in valid cuts. Chef has divided the pizza into four pieces by making two cuts.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T10:17:09.968Z  

```py
# cook your dish here
n = int(input())
for i in range(n):
    a = int(input())
    if a == 1:
        print("yes")
    elif a % 2 == 0:
        print("yes")
    else:
        print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/PIZZAC)