#!/usr/bin/env python3
import sys
import pprint

def pp(d):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(d)

class Case:
  def __init__(self, i, data):
    self.i = i
    self.data = data

  def solve(self):
    sol = ""
    return "Case #{}: {}".format(self.i, sol)

  def __repr__(self):
    return "Case #{}: {}".format(self.i, self.data)

def parse_input(stream):
  cases = []
  for (i, line) in enumerate(stream, 1):
    line = line.rstrip()
    cases.append(Case(i, line.split()))
  return cases

def main():
  cases = parse_input(sys.stdin)
  pp(cases)
  for case in cases:
    print(case.solve())

if __name__ == "__main__":
  main()
  
