def function (A, K):
    if not A: # returns empty list if A is empty
        return A 
    else:
        for i in range(K): # rotate the list K times
            last = A[-1] # store the last element of the list
            for j in range(len(A)-1, 0, -1): # shift all elements to the right by one position
                A[j] = A[j-1] 
            A[0] = last # place the last element at the first position
        return A # return the rotated list
