# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

#brute force dont will pass 100%
'''def solution(A):
    min_diff = sys.maxsize
    for i in range(1, len(A)):
        part1 = A[:i]
        part2 = A[i:]
        
        diff = abs(sum(part1) - sum(part2))
        if min_diff > diff:
            min_diff = diff
        #print("===>part1",part1)
        #print("===>part2",part2)
    return min_diff'''

#######################################
#The next solution will pass 100%, the trick will not calculate the entire sum for each iteration... we needed to accumulate the sum...
#######################################

def solution(A):
    part1 = A[:1]
    part2 = A[1:]
    
    start_sum_lower = sum(part1)
    start_sum_upper = sum(part2)
    min_diff = abs(start_sum_lower - start_sum_upper)
    #print("start_sum_lower", start_sum_lower)
    #print("start_sum_upper", start_sum_upper)
    #print("diff", min_diff)
    
    if len(A) == 2:
        return min_diff
   
    for i in range(1, len(A)):
        if i == len(A)-1:
            continue
        start_sum_lower = start_sum_lower + A[i]
        start_sum_upper = start_sum_upper - A[i]
        #print("start_sum_lower", start_sum_lower)
        #print("start_sum_upper", start_sum_upper)
        diff = abs((start_sum_lower) - (start_sum_upper))
        #print("diff", diff)
        if min_diff > diff:
            min_diff = diff
    return min_diff
