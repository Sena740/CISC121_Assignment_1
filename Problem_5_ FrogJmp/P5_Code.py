def solution(X, Y, D): 
    if D <= 0: # check for invalid jump distance
        return 0
    if Y < X: # check for invalid target position
        return 0
    distance = Y - X # calculate the distance to cover
    jumps = distance // D # calculate the number of jumps needed
    if distance % D != 0: # check for any remaining distance that requires an additional jump
        jumps += 1
    return jumps
