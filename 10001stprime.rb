#!/usr/bin/env ruby

=begin
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
=end


# About 10 seconds of googling and I discovered the 'prime' class!

require 'prime'

primes = Prime.take(10001)

puts "The 10,001st prime is: "+primes.last.to_s

