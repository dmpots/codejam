#!/usr/bin/env ruby
require 'pp'

class Board
  def initialize(i, board)
    @board = board
    @N = i
  end

  def result
    head = "Case ##{@N}:"
  end
end

def read_input(f)
  boards = []
  tT = f.readline.to_i
  (1..tT).each do |t|
    n,m = f.readline.split.map{|i| i.to_i}
    board = []
    (1..n).each do
      board << f.readline.chomp.split
    end
    boards << Board.new(t, board)
  end
  pp boards
end

if __FILE__ == $0
  boards = read_input($stdin)

  boards.each do |b|
    puts b.result
  end
end
