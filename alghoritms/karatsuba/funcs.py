import time

counter_1 = 0
counter_2 = 0
counter_3 = 0


def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper

@timing_val
def karatsuba(x, y):
    n = len(str(x))
    half_n = int(n/2)
    a = int(str(x)[:half_n])
    b = int(str(x)[half_n:])
    c = int(str(y)[:half_n])
    d = int(str(y)[half_n:])
    ac = a*c
    bd = b*d
    sum_of_ad_and_bc = (a + b) * (c + d) - ac - bd
    result = (10**n * ac) + (10**half_n * sum_of_ad_and_bc) + bd
    return result

def make_one_length_vars(x, y):
    if len(x) > len(y):
        difference = len(x) - len(y)
        zeros_needed = '0' * difference
        y = zeros_needed + y

    elif len(x) < len(y):
        difference = len(y) - len(x)
        zeros_needed = '0' * difference
        x = zeros_needed + x

    return x, y

@timing_val
def recursive_karatsuba(x:str, y:str):
    x, y = make_one_length_vars(x, y)

    if len(x) > 1 or len(y) > 1:
        if len(x)%2:
            x = '0' + x
            y = '0' + y

        n = len(x)
        half_n = int(n / 2)
        a, b = x[:half_n], x[half_n:]
        c, d = y[:half_n], y[half_n:]
        ac = recursive_karatsuba(a, c)
        bd = recursive_karatsuba(b, d)
        a_and_b = str(int(a) + int(b))
        c_and_d = str(int(c) + int(d))
        ad_and_bc = recursive_karatsuba(a_and_b, c_and_d) - ac - bd

        if ad_and_bc == 105:
            global counter_1
            counter_1 += 1
        elif ad_and_bc == 72:
            global counter_2
            counter_2 += 1
        elif ad_and_bc == 12:
            global counter_3
            counter_3 += 1

        result = (10 ** n * ac) + (10 ** half_n * ad_and_bc) + bd

    else:
        result = int(x)*int(y)

    return result


x = 1234999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999912349999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999123499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991234999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999912349999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


print(karatsuba(str(x), str(x)))

@timing_val
def multiply(a,b):
    return a*b

print(multiply(x, x))