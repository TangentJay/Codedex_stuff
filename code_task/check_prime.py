# code_task/check_prime.py
'''
* Author: TanB
* Created: 7/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def isPrime(n):  # Function to check if a number is prime
    for i in range(1, n + 1):  # Loop through all numbers from 1 to n
        if i != 1 and i != n and n % i == 0:  # If n is divisible by i (excluding 1 and n), it's not prime
            return False  # Return False if a divisor is found
    
    return True  # Return True if no divisors were found (number is prime)


print(isPrime(2))  # Test the function with 2