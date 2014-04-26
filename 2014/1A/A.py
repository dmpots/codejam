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

def numify(socket):
  return int(socket, 2)

def normalize(sockets):
  return sorted(map(numify, sockets))

def apply_flips(flips, sockets):
  results = []
  for s in sockets:
    results.append(s ^ flips)
  return results

class Case:
  def __init__(self, i, start, goal):
    self.i = i
    self.start = normalize(start)
    self.goal = normalize(goal)
    self.sorted_goal = normalize(goal)
    self.cached_flips = set()

  def is_sol(self,config):
    return sorted(config) == self.sorted_goal

  def findbest(self):
    start = self.start
    if self.is_sol(start):
      return 0

    num_flips = []
    for g_row in self.goal:
      for s_row in self.start:
        flips = []
        flips = g_row ^ s_row

        if flips in self.cached_flips:
          continue
        
        flipped = apply_flips(flips, start)
        #print("s: {}, f: {}, fd:{} = {}".format(list(map(bin,start)), flips, list(map(bin,flipped)), sorted(flipped)))
        if self.is_sol(flipped):
          num_flips.append(bin(flips).count("1"))
        self.cached_flips.add(flips)

    if len(num_flips) == 0:
      return -1
    return min(num_flips)

  def solve(self):
    print(self.i)
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
  
