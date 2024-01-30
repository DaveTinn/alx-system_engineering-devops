#!/usr/bin/env ruby
# The regex must only match capital letters

puts ARGV[0].scan(/[A-Z]+/).join
