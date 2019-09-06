# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

#brute force
def solution(A):
    min_diff = sys.maxsize
    for i in range(1, len(A)):
        part1 = A[:i]
        part2 = A[i:]
        
        diff = abs(sum(part1) - sum(part2))
        if min_diff > diff:
            min_diff = diff
        #print("===>part1",part1)
        #print("===>part2",part2)
    return min_diff
