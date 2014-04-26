#!/usr/bin/env python3
import sys
import pprint

def pp(d):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(d)

def flip(col):
  def f(s):
    if s == "0":
      return "1"
    return "0"
  return [f(i) for i in col]



def solve(goal, start):
  flips = 0
  for (i, col) in enumerate(goal):
    if sorted(col) == sorted(start[i]):
      continue
    if sorted(flip(col)) == sorted(start[i]):
      flips += 1
    else:
      return -1
  return flips

class Case:
  def __init__(self, i, start, goal):
    self.i = i
    self.start = [list(x) for x in zip(*start)]
    self.goal = [list(x) for x in zip(*goal)]

  def solve(self):
    s = solve(self.goal, self.start)
    if s == -1:
      sol = "NOT POSSIBLE"
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
  for case in cases:
    print(case.solve())


main()
  
