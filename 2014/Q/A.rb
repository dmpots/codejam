#!/usr/bin/env ruby
#
require 'pp'
require 'set'

class Case
  def initialize(i, row1, board1, row2, board2)
    @i = i
    @row1 = Set.new board1[row1-1]
    @row2 = Set.new board2[row2-1]
  end

  def solve
    res = @row1 & @row2
    "Case ##{@i}: " +
      case res.size
      when 0 then "Volunteer cheated!" 
      when 1 then res.first
      else "Bad magician!"
      end
  end
end

def read_input(f)
  boards = []
  n = f.readline.to_i
  (1..n).each do |i|
    row1 = f.readline.to_i
    board1 = []
    board1 << f.readline.chomp.split
    board1 << f.readline.chomp.split
    board1 << f.readline.chomp.split
    board1 << f.readline.chomp.split

    row2 = f.readline.to_i
    board2 = []
    board2 << f.readline.chomp.split
    board2 << f.readline.chomp.split
    board2 << f.readline.chomp.split
    board2 << f.readline.chomp.split

    boards << Case.new(i, row1, board1, row2, board2)
  end
  boards
end

if __FILE__ == $0
  read_input($stdin).each do |c|
    #pp c
    puts c.solve
  end

end
