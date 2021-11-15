def max_in(massive, counter):
    if massive[0] == max(massive):
        return counter
    else:
        return max_in(massive[1:], counter + 1)
        
