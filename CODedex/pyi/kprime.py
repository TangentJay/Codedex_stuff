# CODedex/pyi/kprime.py
'''
* Author: TanB
* Created: 7/25/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def kth_prime(k):
    count = 0    # How many primes we've found
    num = 2      # Start checking from 2

    while True:
        if is_prime(num):
            count += 1
            if count == k:
                return num  # Found the k-th prime!
        num += 1

# Example
print(kth_prime(5))  # Output: 11
