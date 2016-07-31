def multiply_0 (n, a):
    if (n == 1): return a;
    return multiply_01(n - 1, a) + a;

def odd(n):
    return n & 0x1;

def half(n):
    return n >> 1;

def multiply_01 (n, a):
    if (n == 1): return a;
    result = multiply_01(half(n), a + a)
    if (odd(n)): result = result + a;
    return result;


