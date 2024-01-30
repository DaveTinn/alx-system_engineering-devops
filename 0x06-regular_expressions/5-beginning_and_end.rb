#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regex matching method
# The regex must be exactly matching a string that starts with 'h' and ends with 'n' and can have any single character in between

puts ARGV[0].scan(/^h.n$/).join
