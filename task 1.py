def print_till_zero(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n)
        n -= 1
        return print_till_zero(n)
    

print_till_zero(5)
