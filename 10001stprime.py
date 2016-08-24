#!/usr/bin/env python3

'''
Problem 7 10001st prime:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
'''
import math


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    sqrt_n = int(math.floor(math.sqrt(n)))
 
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


def genprimes(lim):
    """ This function generates a list of primes from 0 to 'lim'.  """
    int(lim)   # not sure if I need this...
    prime_list = []
    for n in range(2, lim):
        if is_prime(n):
            prime_list.append(n)
        else:
            next
    return prime_list  

if __name__ == "__main__":

  maxnum = 115000
  all_primes = genprimes(maxnum)
  
  for n, p in enumerate(all_primes, start=1):
    #print("{}  {}".format(n, p))
    if n == 10001:
      answer = "INDEX {}: ANSWER: {}".format(n,p)

  print(answer)


