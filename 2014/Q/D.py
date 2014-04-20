#!/usr/bin/env python3
import sys
import pprint

def log(msg):
  #print(msg)
  pass

def pp(d):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(d)


def kens_move(kens_blocks, naomi_choice):
  if naomi_choice > kens_blocks[0]:
    return kens_blocks[-1]
  
  kbr = kens_blocks[:]
  kbr.reverse()
  for block in kbr:
    if block > naomi_choice:
      return block

def points_scored(ken, naomi):
  if naomi > ken:
    return 1
  return 0

def naomi_war(naomi_blocks, ignored):
  return naomi_blocks[0],naomi_blocks[0]

def naomi_dwar(naomi_blocks, ken_blocks):
  if naomi_blocks[-1] < ken_blocks[-1]:
    return naomi_blocks[-1],ken_blocks[0]-0.000001
  else:
    return naomi_blocks[-1],ken_blocks[0]+0.000001

def trace(k, n, p, score):
  log("K={} N={} P={} S={}".format(k, n, p, score))

class Case:
  def __init__(self, i, naomi, ken):
    self.i = i
    self.naomi = naomi
    self.ken = ken

  def run_game(self, naomi_strategy):
    score = 0
    naomi_blocks = self.naomi[:]
    ken_blocks   = self.ken[:]
    for i in range(1, len(self.ken)+1):
      naomi_chosen,naomi_told = naomi_strategy(naomi_blocks, ken_blocks)
      ken_chosen   = kens_move(ken_blocks, naomi_told)

      point = points_scored(ken_chosen, naomi_chosen)
      score += point
      trace(ken_chosen, naomi_chosen, point, score)

      naomi_blocks.remove(naomi_chosen)
      ken_blocks.remove(ken_chosen)
    return score

  def solve(self):
    dwar_points = 0
    war_points = self.run_game(naomi_war)
    log("WAR: {}".format(war_points))
    dwar_points = self.run_game(naomi_dwar)

    sol = "{} {}".format(dwar_points, war_points)
    return "Case #{}: {}".format(self.i, sol)

  def __repr__(self):
    return "Case #{}: n={}, k={}".format(self.i, self.naomi, self.ken)

def parse_blocks(line):
  return sorted(list(map(float, line.split())), reverse=True)

def parse_input(stream):
  cases = []
  N = int(stream.readline())
  for i in range(1, N+1):
    stream.readline()
    naomi = parse_blocks(stream.readline())
    ken   = parse_blocks(stream.readline())
    cases.append(Case(i, naomi, ken))
  return cases

def main():
  cases = parse_input(sys.stdin)
  #pp(cases)
  for case in cases:
    print(case.solve())

if __name__ == "__main__":
  main()
  
