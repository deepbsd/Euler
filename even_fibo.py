#!/usr/bin/env python3
'''
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''

evens = []

def fib(n):
  if n < 2:
    return n
  return fib(n-2) + fib(n-1)

for n in range(34):
  f = fib(n)
  if (f % 2 == 0):
    evens.append(f)

print("Evens: ", evens)
print("Sum = ", sum(evens))
