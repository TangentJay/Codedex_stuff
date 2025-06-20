Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # 6/16/2025
... #JUST RIGHT  IT LUL
... #tst ex
... 
... #ON PY mODULES
... #fibo nums
... 
... def fib(n):
...     #writes fibonacci series up to n
...     a,b= 0,1
...     while a< n:
...         print(a,end='')
...         a,b = b,a+b
...     print()
... 
... def fib2(n):
...     #return fibonacci series up to n
...     result = []
...     a,b=0,1
...     while a<n:
...         result.append(a)
...         a,b = b, a+b
...     return result
... 
... import fibo
... 
