#!/usr/bin/env python3

"""
Project Euler Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#number = 13195
number = 600851475143
i = 2

while i * i < number:
  while number % i == 0:
    number = number / i
  i = i + 1


print(int(number))

