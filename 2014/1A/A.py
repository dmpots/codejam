#!/usr/bin/env python3
import sys
import pprint

def pp(d):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(d)

def flipv(s):
  if s == "0":
    return "1"
  return "0"

def flip(col):
  return [flipv(i) for i in col]

def numify(row):
  return int("".join(map(str,row)),2)

def normalize(sockets):
  return sorted(map(numify, sockets))

def apply_flips(flips, sockets):
  results = []
  for s in sockets:
    res = []
    for (i,v) in enumerate(s):
      if i in flips:
        res.append(flipv(v))
      else:
        res.append(v)
    results.append("".join(res))
  return results

class Case:
  def __init__(self, i, start, goal):
    self.i = i
    self.start = start
    self.goal = goal
    self.sorted_goal = normalize(goal)
    self.cached_flips = set()

  def is_sol(self,config):
    return normalize(config) == self.sorted_goal

  def findbest(self):
    start = self.start
    if self.is_sol(start):
      return 0

    num_flips = []
    for g_row in self.goal:
      for s_row in self.start:
        flips = []
        for (i,s) in enumerate(s_row):
          if g_row[i] != s:
            flips.append(i)
        #print("{}: f:{} s:{} fd:{}".format(self.i,flips, start,flipped))
        flips = tuple(flips)
        if len(flips) == 0 or flips in self.cached_flips:
          continue
        flipped = apply_flips(flips, start)
        if self.is_sol(apply_flips(flips, start)):
          num_flips.append(len(flips))
        self.cached_flips.add(flips)

    if len(num_flips) == 0:
      return -1
    return min(num_flips)

  def solve(self):
    s = self.findbest()
    if s == -1:
      sol="NOT POSSIBLE"
    else:
      sol = str(s)
    return "Case #{}: {}".format(self.i, sol)

  def __repr__(self):
    return "Case #{}: {} to {}".format(self.i, self.start, self.goal)

def parse_input(stream):
  cases = []
  N = int(stream.readline())
  for i in range(1, N+1):
    stream.readline()
    start = stream.readline().split()
    goal  = stream.readline().split()
    cases.append(Case(i, start, goal))
  return cases

def main():
  cases = parse_input(sys.stdin)
  #pp(cases)
  for case in cases:
    print(case.solve())


main()
  
