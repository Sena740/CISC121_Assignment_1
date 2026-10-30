def solution(A):
    box = set() # create an empty set
    for i in A: # iterate through each element in the list
        if i in box: # if the element is already in the set, remove it
            box.remove(i)
        else:
            box.add(i)
    return box.pop() # return the only element left in the set
