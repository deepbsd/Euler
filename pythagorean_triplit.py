#!/usr/bin/env python3

'''
Problem 9 Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

import math

MIN = 500
MAX = 1000

def pytrue(a,b,c):
  if (b>a>0) and (int(math.sqrt(c))**2==c):
    if (c == (a**2)+(b**2)):
      return True
  return False

def eq1000(a,b,c):
  if a+b+c == 1000:
    return True
  else:
    return False


def checklst(lst1, lst2):
  for a in lst1:
    for b in lst2:
      c = (a**2)+(b**2)
      if pytrue(a,b,c):
        if eq1000(a,b,math.sqrt(c)):
          return "{}  {}  {}".format(a,b,math.sqrt(c))


if __name__ == "__main__":

    # start with a is even...
    a = [ n for n in range(MIN) if n % 2 == 0 ]
    b = [ n for n in range(MAX) if n % 2 != 0 ]

    if checklst(a,b): print(checklst(a, b))

    # now if a is odd...
    a = [ n for n in range(MIN) if n % 2 != 0 ]
    b = [ n for n in range(MAX) if n % 2 == 0 ]

    if checklst(a,b): print(checklst(a,b))



