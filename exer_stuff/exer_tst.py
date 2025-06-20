# 6/16/2025
#JUST RIGHT  IT LUL
#tst ex

#ON PY mODULES
#fibo nums

def fib(n):
    #writes fibonacci series up to n
    a,b= 0,1
    while a< n:
        print(a,end='')
        a,b = b,a+b
    print()

def fib2(n):
    #return fibonacci series up to n
    result = []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result

import fibo

fibo.fib(1000)