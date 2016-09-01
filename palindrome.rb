#!/usr/bin/env ruby

=begin
Project Euler: Problem 4.

Largest Palindrome Product:

A palindromic number reads the same both ways.  The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.  

Find the largest palindrome made from the product of two 3-digit numbers.
=end

start_time = Time.now


def is_pal(n)
  n.to_s == n.to_s.reverse
end

maxval = 0  # starting point...

100.upto(999) { |fac1|         #only 3-digit factors...
  fac1.upto(999) { |fac2|
    product = fac1 * fac2

    if is_pal(product) && product > maxval   #only need to save the maxval, toss the rest
      maxval = product 
      $mfac1, $mfac2  = fac1, fac2           #good use for global vars????  Not sure
    end
  }
}

puts "#{maxval} = #{$mfac1} * #{$mfac2}   Elapsed time: %.4f  milliseconds" % ((Time.now-start_time)*1000)






