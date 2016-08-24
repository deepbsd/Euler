#!/usr/bin/env python3

'''
Problem 5:
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
#####################

numlist = list(range(1,21))

products = []

# all the prime numbers have to go into it.
minnum = 2*3*5*7*11*13*17*19

for n in numlist:
  if minnum % n != 0:
    print("oops!  {}:  {}".format(n, minnum/n))
    next
  else:
    print("minnum={}. index: {}  factor: {}".format(minnum, n, minnum/n))
    continue
'''    

from functools import reduce

def gcd(a, b):
  '''Return greatest common divisor using Euclid's Algorithm.'''
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  '''Return lowest common multiple.'''
  return a * b // gcd(a, b)

def lcmm(*args):
  '''Return lcm of args.'''
  return reduce(lcm, args)


if __name__ == "__main__":

 print(lcmm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) )





