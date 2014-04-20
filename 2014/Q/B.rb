#!/usr/bin/env ruby
#
require 'pp'

class Case
  def initialize(i, c, f, x)
    @i = i
    @c = c
    @f = f
    @x = x
  end

  def cook_time(rate, needed)
    needed / rate
  end

  def farm_time(rate)
    @c / rate
  end

  def cookies(rate, elapsed_time)
    rate * elapsed_time
  end

  def greedy
    times = []
    cookies = 0
    rate = 2.0

    while cookies < @x
      remaining = @x - cookies 
      next_cook_time = cook_time(rate, remaining)
      next_farm_time = farm_time(rate) + cook_time(rate+@f, remaining+@c-(cookies(rate, farm_time(rate))))
      if next_cook_time < next_farm_time
        #puts "cook"
        cookies += remaining
        times << next_cook_time
      else
        #puts "farm"
        cookies += -@c + (farm_time(rate) * rate)
        times << farm_time(rate)
        rate += @f
      end
    end
    #puts times
    times.reduce(:+)
  end

  def solve
    sprintf "Case ##{@i}: %.7f", greedy
  end
end

def read_input(f)
  n = f.readline.to_i
  (1..n).map do |i|
    c,ff,x = f.readline.split
    Case.new(i, c.to_f, ff.to_f, x.to_f)
  end
end

if __FILE__ == $0
  read_input($stdin).each_with_index do |c,i|
    #pp c
    puts c.solve 
  end

end
