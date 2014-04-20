#!/usr/bin/env ruby
require 'pp'

def winner(row)
  if (row.count("X") == 3 and row.count("T") == 1) or
     (row.count("X") == 4)
    return "X"
  elsif (row.count("O") == 3 and row.count("T") == 1) or
        (row.count("O") == 4)
    return "O"
  else
    return "D"
  end
end

class Board
  def initialize(i, board)
    @board = board
    @N = i
  end

  def [](i)
    return @board[i]
  end

  def each
    yield @board[0]
    yield @board[1]
    yield @board[2]
    yield @board[3]

    yield @board.transpose[0]
    yield @board.transpose[1]
    yield @board.transpose[2]
    yield @board.transpose[3]

    yield [@board[0][0], @board[1][1], @board[2][2], @board[3][3]]
    yield [@board[0][3], @board[1][2], @board[2][1], @board[3][0]]
  end

  def incomplete
    @board.map{|r| r.join.include?(".")}.any?
  end

  def result
    head = "Case ##{@N}:"
    each do |row|
      w = winner(row)
      if w != "D"
        return "#{head} #{w} won"
      end
    end

    return "#{head} Game has not completed" if incomplete
    return "#{head} Draw"
  end
end

def read_input(f)
  boards = []
  n = f.readline.to_i
  (1..n).each do |i|
    board = []
    board << f.readline.chomp.chars
    board << f.readline.chomp.chars
    board << f.readline.chomp.chars
    board << f.readline.chomp.chars

    f.readline
    boards << Board.new(i, board)

    #pp i
    #boards[i-1].each do |row|
    #  pp row
    #end
  end
  boards
end

if __FILE__ == $0
  boards = read_input($stdin)

  boards.each do |b|
    puts b.result
  end
end
