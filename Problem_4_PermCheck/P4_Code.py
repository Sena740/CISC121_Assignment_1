def solution(A): 
    if not A: # if the list is empty, return 1 
        return 1  
    L = set(range(1,max(A)+1)) # create a set of all numbers from 1 to the maximum number in the list  
    for i in A: # iterate through each element in the list   
        if i in L: # if the element is already in the set, remove it   
            L.remove(i)   
        else: # if not, add it  
            L.add(i)  
    if not L: # if the set is empty, return 1 
        return 1 
    else: # if the set is not empty, return 0 
        return 0 
