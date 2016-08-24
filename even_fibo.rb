#!/usr/bin/env ruby

=begin

Problem 2 Even Fibonacci numbers:

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

=end

# return the next fibonacci number
def fib(n)
  if n < 2 then return n end
  return fib(n-2) + fib(n-1)
end

sum = 0  # sum variable
i = 1    # iterator variable

while sum < 4000000 do 
  n = i  # don't disturb the iterator...
  n = fib(n)
  if n % 2 == 0 then sum += n end
  i += 1
end

# show the answer
puts sum


