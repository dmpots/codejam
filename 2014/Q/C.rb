#!/usr/bin/env ruby
#
require 'pp'
require 'set'
class Integer
  def fact
    (1..self).reduce(:*) || 1
  end
end

class Board
  def initialize(rows, cols, mines)
    @rows = rows
    @cols = cols
    @mines = mines

    @board = []
    @rows.times {@board << []}
    fill_empty
    place_mines
    #puts "BOARD"
    #puts self
    #puts "BOARD"
  end
  def fill_empty
    @rows.times {|r| @cols.times {|c| @board[r][c] = 'x'}}
  end

  def place_mines
    mines = @mines
    ul = [0,0]
    ur = [0,@cols-1]
    br = [@rows-1, @cols-1]
    bl = [@rows-1, 0]
    while mines > 0
      #puts "BOARD:"
      #puts self
      cells = optimial_order(outer_box(ul, ur, bl, br), mines)
      take = [mines, cells.size].min
      allocate = cells[0...take]
      allocate.each do |cell|
        r,c = cell
        @board[r][c] = "*"
      end

      mines -= take

      ul = ul[0]+1,ul[1]+1
      ur = ur[0]+1,ur[1]-1
      br = br[0]-1,br[1]-1
      bl = bl[0]-1,bl[1]+1
    end
  end

  def optimial_order(cells, mines)
    return cells.to_a if mines > cells.size

    return_order = []
    order = cells.to_a.reverse
    saved_board = clone_board
    last = nil
    needed_mines = mines
    while needed_mines > 0 and not order.empty?
      last = order.pop
      return_order << last
      @board[last[0]][last[1]] = "*"
      needed_mines -= 1
    end

    ordered_board = clone_board
    #puts "BB"
    #puts self
    solved = solve
    if not solved and last
      return_order.pop
      @board = ordered_board
      @board[last[0]][last[1]] = "x"
      last_board = clone_board
      choices = []
      (0...@rows).each {|r| (0...@cols).each {|c| choices << [r,c] if @board[r][c] == "x"}}
      #choices = (order - return_order)
      #puts "CHOICES: #{choices}"
      choices.each do |cell|
        #puts "CHOOSE: #{cell}"
        @board = last_board.map {|r| r.clone}
        r,c = cell
        @board[r][c] = "*"
        #puts "B"
        #puts self
        if solve
          #puts "SOLVED"
          return_order << cell
          break
        end
        #puts "S"
        #puts self
      end
    end
    #puts "DONE"
    @board = saved_board
    if return_order.size < mines
      return cells.to_a
    end
    return return_order
  end

  def optimial_order2(cells, mines)
    return cells.to_a if mines > cells.size
    saved_board = clone_board
    order = try_cells(cells.to_a, mines)
    @board = saved_board
    if not order or order.size < mines
      #puts "FAILED TO FIND OPTIMIAL ORDER"
      return cells.to_a
    end
    return order
  end

  def try_cells(cells, mines)
    #puts "TRY CELLS"
    #puts self
    if cells.empty? or mines == 0
      return cells if solved?
      return nil
    end
      
    #puts "TRYING: #{cells}"
    initial_board = clone_board


    cells = cells.reject do |cell|
      r,c = cell
      @board[r][c] = "*"
      #puts "B: #{cell}"
      #puts self
      solved = solve
      @board = initial_board.map {|r| r.clone}
      #puts "B: #{cell} -- #{solved}"
      #puts self
      not solved
    end
    #puts "PRUNED: #{cells}"
    return nil if cells.size < mines


    cells.each_with_index do |cell,i|
      #puts "CELL: #{cell}"
      #puts self

      r,c = cell
      @board[r][c] = "*"
      solved = solve
      @board = initial_board.map {|r| r.clone}
      @board[r][c] = "*"
      if solved
        #puts "SOLVED: #{cell}"
        #puts self
        sub_order = try_cells(cells[0...i] + cells[i+1...cells.size], mines - 1)
        if sub_order
          #puts "SUB_SOLVED: #{sub_order}"
          #puts self
          return [cell] + sub_order if sub_order
        end
      end
      #puts "NO LUCK"
      @board[r][c] = "x"
      #puts self
    end
    @board = initial_board
    #puts "FAILED"
    return nil
  end

  def optimial_order1(cells, mines)
    return cells.to_a if mines > cells.size
    order = []

    orig_board = clone_board
    remaining_cells = cells.to_a
    solved = true
    #puts "Remaining: #{cells.to_a}"
    backtracks, bt_limit = 0,100
    while remaining_cells.size > 0 and mines > 0 and solved
      solved = false
      max_cell = remaining_cells.first
      remaining_cells.each do |cell|
        r,c = cell
        @board[r][c] = "*"
        before_solve = clone_board
        #puts "Before Solve: "
        #puts self
        if solve
          max_cell = cell
          #puts "Solved:"
          solved = true
          #puts self
          @board = before_solve
          break
        end
        @board = before_solve
        #puts "Restored: "
        #puts self
        @board[r][c] = "x"
      end

      if not solved and backtracks < bt_limit and not order.empty?
        backtracks += 1
        solved = true
        bt = order.sample
        order.delete(bt)
        #puts "BT: #{bt}"
        #puts self
        @board[bt[0]][bt[1]] = "x"
        remaining_cells << bt
        mines += 1
      else
        order << max_cell
        #puts "BS: #{solved}"
        #puts self
        @board[max_cell[0]][max_cell[1]] = "*"
        mines -= 1
        remaining_cells.delete(max_cell)
      end
      #puts self
    end
    order += remaining_cells.to_a
    @board = orig_board
    #puts order
    order
  end

  def zeros
    (0...@rows).map {|r| (0...@cols).map{|c| zero([r,c])}.count(true)}.reduce(:+)
    #@board.map{|r| r.map{|cell| zero(cell)}.count(true)}.reduce(:+)
  end

  def outer_box(ul, ur, bl, br)
    cells = Set.new([ul, ur, bl, br])
    cell = ul
    while cell != ur
      cells << cell
      cell = cell[0],cell[1]+1
    end
    while cell != br
      cells << cell
      cell = cell[0]+1,cell[1]
    end
    while cell != bl
      cells << cell
      cell = cell[0],cell[1]-1
    end
    while cell != ul
      cells << cell
      cell = cell[0]-1,cell[1]
    end
    cells
  end

  def place_mines_1
    mines = @mines
    r,c = 0,0
    r_n,c_n = 0,1
    r_ur,c_ur = 0, @cols-1
    r_br,c_br = @rows-1, @cols-1
    r_bl,c_bl = @rows-1, 0
    r_ul,c_ul = 0,0

    while mines > 0
      #puts self
      #puts ""
      @board[r][c] = "*"
      mines -= 1
      if r == r_ur and c == c_ur
        #puts "A"
        r = r+1
        r_n = 1
        c_n = 0
      elsif r == r_br and c == c_br
        #puts "B"
        c = c-1
        r_n = 0
        c_n = -1
      elsif r == r_bl and c == c_bl
        #puts "C"
        r = r-1
        r_n = -1
        c_n = 0
      else
        #puts "D"
        r += r_n
        c += c_n
      end

      if r == r_ul and c == c_ul
        #puts "E", r, c
        r = r + 1
        c = c + 1
        r_n, c_n = 0,1
        r_ul,c_ul = r_ul+1, c_ul+1
        r_ur,c_ur = r_ur+1, c_ur-1
        r_br,c_br = r_br-1, c_br-1
        r_bl,c_bl = r_bl-1, c_bl+1
      end
    end
  end
  def to_s
    s = ""
    @rows.times do |r|
      @cols.times do |c|
        s << @board[r][c]
      end
      s << "\n"
    end
    s
  end

  def solve
    starting_clicks = []
    @board.each_with_index do |row,r|
      row.each_with_index do |v,c|
        starting_clicks << [r,c] if v == "x"
      end
    end

    solved = false
    while starting_clicks.size > 0 and not solved?
      orig_board = clone_board
      play_click(starting_clicks.pop)
      #puts "CLICK:"
      #puts self
      @board = orig_board unless solved?
    end
    return solved?
  end

  def solved?
    @board.map{|r| not r.include?("x")}.reduce(:&)
  end

  def clone_board
    @board.map {|r| r.clone}
  end

  def play_click(start_click)
    visited = Set.new(start_click)
    worklist = [start_click]
    while not worklist.empty?
      #puts "#{worklist}"
      cell = worklist.pop
      visited.add(cell)
      r,c = cell
      #puts "#{cell}"
      #puts "#{neighbors(cell)}"
      if cell == start_click
        @board[r][c] = "c"
      else
        @board[r][c] = "."
      end
      if zero(cell)
        neighbors(cell).each do |n|
          nr,nc = n
          if @board[nr][nc] != "*" and not visited.include?(n)
            worklist.push(n)
          end
        end
      end
    end
  end

  def zero(cell)
    neighbors(cell).map {|r,c| @board[r][c] != "*"}.reduce(:&)
  end

  def neighbors(cell)
    r,c = cell
    [    
     [r-1,c-1],[r-1,c],[r-1,c+1],
     [r,c-1]  ,        [r,c+1],
     [r+1,c-1],[r+1,c],[r+1,c+1]
    ].reject{|r,c| r < 0 or c < 0 or r > @rows-1 or c > @cols-1}
  end

end


class Case
  attr_reader :board
  def initialize(i, rows, cols, mines)
    @i = i
    @rows = rows
    @cols = cols
    @mines = mines
    @board = Board.new(rows,cols,mines)
  end
  def solve
    #puts @board
    @board.solve

    result = "Case ##{@i}:\n"
    if @board.solved?
      result << @board.to_s
    else
      result << "Impossible"
    end
  end
end

def read_input(f)
  n = f.readline.to_i
  (1..n).map do |i|
    rows,cols,mines = f.readline.split

    Case.new(i, rows.to_i, cols.to_i, mines.to_i)
  end
end

if __FILE__ == $0
  read_input($stdin).each_with_index do |c,i|
    
    #pp c
    puts c.solve
    #puts c.board
  end

end
