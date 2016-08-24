#!/usr/bin/env python3

'''
Problem 4 Largest palindrome product:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math

biggest_num = 999*999

def getpals(num):
  '''
  Find palyndromic numbers in ranges for num
  '''
  try:
    int(num)
  except ValueError as e:
    print("Please enter an integer only.")

  palindromes = []
  for n in range(num):
    s = list(str(n))
    if (len(s) > 2) and ( s == list(reversed(s)) ):
      palindromes.append(n)

  return palindromes


def getfactors(num):
  '''
  Find all the 3-digit factor pairs for num
  '''
  length = 3  # We're looking for 3-digit pairs
  pairs = []
  biggest = int(math.sqrt(num))
  smallest = int(num*0.25)
  for n in range(biggest, smallest):
    if num % n == 0:
      fac1 = n
      fac2 = num/fac1
      pair = [int(fac1), int(fac2)]

      if (len(str(pair[0])) == length) and (len(str(pair[1])) == length):
        pairs.append(pair)

  return pairs
  
def getbigpairs():
  '''
  Take the 3-dig pairs returned from getfactors and find the largest pair
  '''
  bigpairs = []
  for pal in getpals(biggest_num):
    for pair in getfactors(pal):
      if (len(str(pair[0])) == 3) and (len(str(pair[1])) == 3):
        bigpairs.append(pair)

  return bigpairs


if __name__ == "__main__":

  bigpairs = getbigpairs()

  for pair in bigpairs:
    print("{} = {} * {}".format(pair[0]*pair[1], pair[0], pair[1]))
    



