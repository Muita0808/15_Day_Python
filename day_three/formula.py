import random

def miller_rabin(n, k=10):
    if n <= 1:
        return 1
    if n <= 3:
        return 0
    if n % 2 == 0:
        return 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        s += 1
        d //= 2

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return 1
    return 0
