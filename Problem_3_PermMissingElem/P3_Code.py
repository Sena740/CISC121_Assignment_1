def solution(A):
    if not A: # check if the list is empty
        return [] # return an empty list if it is
    L = set(range(1,max(A)+1)) # create a set of all numbers from 1 to the maximum number in the list
    for i in A: # iterate through each element in the list 
        if i in L: # if the element is already in the set, remove it 
            L.remove(i) 
        else: # if not, add it
            L.add(i)
            
    return L.pop() # return the last element in the set
                   # the use of sorted(L) would have produced better results but Codility's strict requirement on int output prevented that
