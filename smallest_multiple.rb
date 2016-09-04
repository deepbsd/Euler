#!/usr/bin/env ruby

=begin
Project Euler Problem 5
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
=end

# Fortunately, Ruby has a built-in lcm method that can be called on a list.
# Easy Peasy!

puts "The least common multiple of all numbers from 1 to 20 is " + [*1..20].reduce(:lcm).to_s

