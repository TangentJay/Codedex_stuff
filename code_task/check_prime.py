# code_task/check_prime.py
'''
* Author: TanB
* Created: 7/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def isPrime(n):
    for i in range(1, n + 1):
        if i != 1 and i != n and n % i == 0:
            return False

    return True


print(isPrime(4))