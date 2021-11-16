def max_in(massive):
    if massive[0] == max(massive):
        return 1
    else:
        return 1 + max_in(massive[1:])
