#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regex matching method
# Regex should not contain square brackets

puts ARGV[0].scan(/hbt*n/).join
