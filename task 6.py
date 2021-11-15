def hanoi(n, i, k):
    if n == 1:
        print(f'Moove disk 1 from pin {i} to pin {k}')
    else:
        tmp = 6 - i - k
        hanoi(n - 1, i, tmp)
        print(f'Move disk {n} from pin {i} to pin {k}')
        hanoi(n - 1, tmp, k)
