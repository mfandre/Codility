def solution(A):
    
    totalRight = sum(A[1:])
    accumLeft = A[0]
    accumRight = totalRight
    
    minimalDiff = abs(accumLeft - accumRight)
    
    for i in range(1,len(A)-1):
        
        #print("A[i]", A[i])
        accumLeft = accumLeft + A[i]
        accumRight = accumRight - A[i]
        #print("accumLeft",accumLeft)
        #print("accumRight",accumRight)
        result = abs(accumLeft  - accumRight)
        #print("result",result)
        if minimalDiff > result:
            minimalDiff = result
            
    
    return minimalDiff
