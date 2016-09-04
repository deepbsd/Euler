#!/usr/bin/env ruby

=begin
Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
=end

MAX = 100
sum1, sum2 = 0, 0
sum_of_squares = [*1..MAX].collect { |n| sum1 += n**2 }.last
square_of_sum = [*1..MAX].collect { |n| sum2 += n }.last**2

  
puts "Difference is #{square_of_sum - sum_of_squares}"


