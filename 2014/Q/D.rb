#!/usr/bin/env ruby
#
require 'pp'

class Case
  attr_accessor :table
  def initialize(i, naomi, ken)
    @i = i
    @naomi = naomi.sort.reverse
    @ken   = ken.sort.reverse

    @table = {}
  end

  def best_winning_move(ken, naomi, game)
  case game
  when :war then
    first_ken_win = ken.zip(naomi).find_index {|k,n| n < k}
    if first_ken_win and first_ken_win > 0
      i = first_ken_win - 1
      return 1,ken[0...-1],naomi[0...i]+naomi[i+1..-1]
    else
      return 0,ken[1..-1],naomi[1..-1]
    end
  end
  end
  
  def best_losing_move(ken, naomi, game)
  case game
  when :war then
    first_ken_win = ken.zip(naomi).find_index {|k,n| n < k}
    if first_ken_win
      i = first_ken_win
      return 0,ken[0...i]+ken[i+1..-1],naomi[0...i]+naomi[i+1..-1]
    else
      return 1,ken[1..-1],naomi[1..-1]
    end
  end
  end

  def best_naomi(ken, naomi, game)
    case game
    when :war then
      return naomi[0],naomi.clone[1..-1]
    when :decit
      if naomi[0] > ken[0] then
        return naomi[0],naomi.clone[1..-1]
      else
        return ken[0]-0.000001,naomi[0...-1]
      end
    end
  end

  def best_n(ken, n)
    return n if n > ken[0]
    return ken[0]-0.000001
  end

  def worst_n(ken, n)
    i = ken.find_index {|k| k > n}
    if i
      return ken[i]-0.000001
    else
      return n
    end
  end

  def worst_naomi(ken, naomi, game)
    if naomi[-1] < ken[0]
      return ken[0]-0.000001,naomi[0...-1]
    else
      return naomi[0],naomi.clone[1..-1]
    end
  end

  def kens_move(ken, n)
    #puts "#{ken}, #{n}"
    return ken[-1],ken[0...-1] if n > ken[0]
    i = ken.find_index {|k| k > n}
    return ken[i],ken[0...i]+ken[i+1..-1]
  end


  def best(ken, naomi, game)
    #puts "B: #{ken}, #{naomi}"
    return 0 if ken.size == 0
    #puts "R: #{ken}, #{naomi}"
    sub = ken.to_s+naomi.to_s
    #return (puts "HIT"; @table[sub]) if @table.has_key?(sub)
    return ( @table[sub]) if @table.has_key?(sub)

    n,nn = best_naomi(ken, naomi, game)
    k,kk = kens_move(ken, n)

    win = n > k ? 1 : 0
    #puts "W: #{win} N: #{n}, K: #{k}"
    val1 = win+best(kk, nn, game)

    if game == :decit
      val2 = naomi.each_with_index.map do |n,i|
        k,kk = kens_move(ken, best_n(ken, n))
        ((n > k) ? 1 : 0) + best(kk, naomi[0...i]+naomi[(i+1)..-1], game)
      end.max
      val3 = naomi.each_with_index.map do |n,i|
        k,kk = kens_move(ken, worst_n(ken, n))
        ((n > k) ? 1 : 0) + best(kk, naomi[0...i]+naomi[(i+1)..-1], game)
      end.max
      val = [val2,val3].max

      #max = 0
      #maxv = nil
      #vals.each do |n,v|
      #  if v > max
      #    maxv = n
      #    max = v
      #  end
      #end
      #puts "VALS: #{vals}"
      #puts "MAXV: #{maxv} = #{max}"
      #val = max

      #n2,nn2 = worst_naomi(ken, naomi, game)
      #k2,kk2 = kens_move(ken, n2)
      #win2 = n2 > k2 ? 1 : 0
      ##puts "W2: #{win} N2: #{n}, K2: #{k}"
      #val2 = win2+best(kk2, nn2, game)
      #val = [val1, val2].max
    else
      val = val1
    end

    #puts "V: #{val}"
    @table[sub] = val
    return val
  end

  def solve
    w = best(@ken, @naomi, :war)
    @table = {}
    #puts :decit
    d = best(@ken, @naomi, :decit)
    "Case ##{@i}: #{d} #{w}"
  end
end


def read_input(f)
  cases = []
  n = f.readline.to_i
  (1..n).each do |i|
    f.readline
    naomi = f.readline.split.map(&:to_f)
    ken = f.readline.split.map(&:to_f)

    cases << Case.new(i, naomi, ken)
  end
  cases
end

if __FILE__ == $0
  read_input($stdin).each do |c|
    #pp c
    puts c.solve
  end

end
