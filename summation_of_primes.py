#!/usr/bin/env python3

'''
Problem 10 Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    sqrt_n = int(math.floor(math.sqrt(n)))
    #for i in range(3, sqrt_n + 1, 2):
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def genprimes(lim):
    """ This function generates a list of primes from 0 to 'lim'
    Please use common sense and don't exceed 100 for now...
    """
    int(lim)   # not sure if I need this...
    prime_list = []
    for n in range(2, lim):
        if is_prime(n):
            prime_list.append(n)
        else:
            next
    return prime_list  


if __name__ == "__main__":
    
    primeslist = genprimes(1999999)
    print(sum(primeslist))


