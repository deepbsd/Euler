#!/usr/bin/env ruby

=begin
Problem 3 Largest prime factor:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
=end



number = 600851475143
i = 2

while i * i < number do
  while number % i == 0 do
    number = number / i
  end
  i = i + 1
end

puts number.to_i
