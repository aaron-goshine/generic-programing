def multiply_0(n, a):
    if n == 1:
        return a
    return multiply_01(n - 1, a) + a


def odd(n):
    return n & 0x1


def half(n):
    return n >> 1


def multiply_01(n, a):
    if n == 1:
        return a
    result = multiply_01(half(n), a + a)
    if (odd(n)):
        result = result + a
    return result


def mult_acc_0(r, n, a):
    if n == 1:
        return r + a
    if odd(n):
        return mult_acc_0(r + a, half(n), a + a)
    else:
        return mult_acc_0(r, half(n), a + a)


def mult_acc_01(r, n, a):
    if n == 1:
        return r + a
    if odd(n):
        r = r + a
    return mult_acc_01(r, half(n), a + a)


def mult_acc_02(r, n, a):
    if odd(n):
        r = r + a
        if n == 1:
            return r
    return mult_acc_02(r, half(n), a + a)


def mult_acc3(r, n, a):
    if odd(n):
        r = r + a
        if n == 1:
            return r
    n = half(n)
    a = a + a
    return mult_acc3(r, n, a)


def mult_acc4(r, n, a):
    while True:
        if odd(n):
            r = r + a
            if n == 1:
                return r
        n = half(a)
        a = a + a


def multiply_02(n, a):
    if n == 1:
        return a
    return mult_acc4(a, n - 1, a)
