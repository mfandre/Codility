# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def sumPa(A, an):
    a1 = 1
    n = an
    
    return (a1+an)*n/2

def solution(A):
    if len(A) == 0:
        return 1
    if len(A) == 1 and A[0] >= 2:
        return 1
    if len(A) == 1 and A[0] == 1:
        return 2
        
    an = max(A)
    elem_missing = int(sumPa(A, an) - sum(A))
        
    if elem_missing == 0:
        return an+1
        
    #print(sumPa(A) - sum(A))
    return elem_missing
