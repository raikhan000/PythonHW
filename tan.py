from decimal import getcontext, Decimal
from math import *

def calcPi(n):
    getcontext().prec = B + 3
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return pi


def calc_tan(x,n):
    q = x
    s = 0

    cos_approx = 0

    for i in range(n+1):
        if i < n:
            coef = (-1) ** i
            num = x ** (2 * i)
            denom = factorial(2 * i)
            cos_approx += (coef) * ((num) / (denom))
        if i > 0:
            s = s + q
            q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))



    return str(s/cos_approx)

a = int(input())
B = int(input())

if B<16:
    n = f'{tan(a * pi / 200):.16f}'
    getcontext().prec = B
    A = Decimal(n)/ Decimal('1.0')
    print(A)
else:

    n_pi = ceil(B/14.18)
    pi_val = calcPi(n_pi)
    n = calc_tan(a * pi_val / 200, 400)

    getcontext().prec = B
    A = Decimal(str(n)) / Decimal('1.0')

    print(A)

