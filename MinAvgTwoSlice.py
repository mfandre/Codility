# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_2_lowers(A):
    total = 10001 + 10001
    x_pos = 0
    y_pos = 0
    for i,j in zip(range(len(A)), range(1, len(A))):
        if j == len(A):
            return x_pos, y_pos, total
        if A[i] + A[j] == total:
            continue #ignoring the more deeply index
        elif A[i] + A[j] < total:
            total = A[i] + A[j]
            x_pos = i
            y_pos = j
        

    return x_pos, y_pos, total

def find_3_lowers(A):
    total = 10001 + 10001 + 10001
    x_pos = 0
    y_pos = 0
    z_pos = 0
    for i,j,k in zip(range(len(A)), range(1, len(A)),range(2, len(A))):
        if k == len(A):
            return x_pos, y_pos, z_pos, total
        if A[i] + A[j] + A[k] == total:
            continue #ignoring the more deeply index
        elif A[i] + A[j] + A[k] < total:
            total = A[i] + A[j] + A[k]
            x_pos = i
            y_pos = j
            z_pos = k

    return x_pos, y_pos, z_pos, total

def solution(A):
    if len(A) <= 2:
        return 0
    
    x2,y2,total2 = find_2_lowers(A)
    x3,y3,z3,total3 = find_3_lowers(A)
    
    #print("x2,y2,total2 ", x2,y2,total2 )
    #print("x3,y3,z3,total3 ", x3,y3,z3,total3 )
    
    if total2/2 < total3/3:
        return x2
    elif total2/2 == total3/3:
        return min(x2, x3)
    return x3
