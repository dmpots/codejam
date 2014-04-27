#!/usr/bin/env python3
import sys
import pprint
import argparse
from operator import attrgetter, methodcaller, itemgetter

debug = False
def log(msg, *args):
  global debug
  if debug:
    print(msg.format(*args))

def parse_args():
  parser = argparse.ArgumentParser(description='Google CodeJam Template')
  parser.add_argument('-d', '--debug', action='store_true',
                    help='print debugging messages')
  parser.add_argument('-c', '--case', metavar='N', type=int,
                    help='only run case N (default: run them all)')

  args = parser.parse_args()
  if args.debug:
    global debug
    debug = True
  return args

class Case:
  def __init__(self, i):
    self.i = i

  def solve(self):
    log("Solving: {}", self)
    sol = ""
    return self.case() + sol

  def case(self):
    return "Case #{}: ".format(self.i)

  def __repr__(self):
    return self.case()

def parse_input(stream):
  cases = []
  T = int(stream.readline())
  for i in range(1, T+1):
    # parse case input
    cases.append(Case(i))
  return cases

def main():
  options = parse_args()
  cases = parse_input(sys.stdin)
  for case in cases:
    if not options.case or options.case == case.i:
      print(case.solve())
      sys.stdout.flush()


main()
  
