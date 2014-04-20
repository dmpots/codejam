#!/usr/bin/env ruby
#
require 'pp'

class Case
  def initialize(i)
    @i = i
  end

  def solve
    "Case ##{@i}: "
  end
end

def read_input(f)
  cases = []
  n = f.readline.to_i
  (1..n).each do |i|
  end
  cases
end

if __FILE__ == $0
  read_input($stdin).each do |c|
    puts c.solve
  end

end
