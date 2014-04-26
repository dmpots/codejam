#!/usr/bin/env python3
import sys
import pprint
import random
import collections

def pp(d):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(d)

class Case:
  def __init__(self, i, data):
    self.i = i
    self.data = data

  def solve(self, p_good, p_bad):
    pg = 0.0
    pb = 0.0
    for (i, v) in enumerate(self.data):
      pg += p_good[(i,v)]
      pb += p_bad[(i,v)]

    if pg > pb:
      sol ="GOOD"
    else:
      sol ="BAD"

    #print(pg, pb)
    return "Case #{}: {}".format(self.i, sol)

  def __repr__(self):
    return "Case #{}: {}".format(self.i, self.data)

def parse_input(stream):
  cases = []
  N = int(stream.readline())
  for i in range(1, N+1):
    stream.readline()
    data = list(map(int, stream.readline().split()))
    cases.append(Case(i, data))
  return cases

def main():
  cases = parse_input(sys.stdin)
  p_good = gen_prob(gen_good)
  p_bad = gen_prob(gen_bad)
  for case in cases:
    print(case.solve(p_good, p_bad))


def gen_prob(gen):
  random.seed(0xd00d)
  N = 1000
  T = 1000
  dist_map = {}
  for i in range(N):
    dist_map[i] = collections.defaultdict(int)

  for i in range(T):
    a = gen(N)
    #print(a)
    dist(a, dist_map)

  prob_map = collections.defaultdict(float)
  for i in range(N):
    for v,cnt in dist_map[i].items():
      p = cnt/T
      prob_map[(i,v)] = p
      #print("{}@{}: {}".format(v, i, cnt/T))
    #print()

    #print("{}: {}".format(i, dist_map[i].items()))
  return prob_map


def dist(a,dist_map):
  for (i,k) in enumerate(a):
    dist_map[i][k] += 1

def gen_good(N):
  a = [i for i in range(N)]
  for k in range(N):
    p = random.randint(k, N-1)
    t = a[k]
    a[k] = a[p]
    a[p] = t
  return a

def gen_bad(N):
  a = [i for i in range(N)]
  for k in range(N):
    p = random.randint(0, N-1)
    t = a[k]
    a[k] = a[p]
    a[p] = t
  return a

main()
  
