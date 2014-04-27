#!/usr/bin/env python3
import sys
import pprint
import argparse
import collections
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


class Tree:
  def __init__(self, node):
    self.node = node
    self.children = []

def print_tree(tree):
  print("{}({})".format(tree.node, tree.size))
  for child in tree.children:
    print("  {}({})".format(child.node, child.size))
  for child in tree.children:
    print_tree(child)

def build_tree(root, edges):
  def dfs(node, visited):
    visited.add(node)
    n = Tree(node)
    children = []
    for child in edges[node]:
      if child not in visited:
        n.children.append(dfs(child, visited))
    n.size = 1 + sum(map(lambda c: c.size, n.children))
    return n

  def bfs(rootnode):
    queue = collections.deque()
    tree = Tree(rootnode)
    queue.append(tree)
    visited = set([rootnode])
    while len(queue) > 0:
      n = queue.popleft()
      for child in edges[n.node]:
        if not child in visited:
          c = Tree(child)
          n.children.append(c)
          queue.append(c)
          visited.add(child)
    return tree
  
  def annotate_size(tree):
    size = 1
    for c in tree.children:
      annotate_size(c)
      size += c.size
    tree.size = size

  tree = bfs(root)
  annotate_size(tree)
  return tree
  #return dfs(root, set())

def prune_tree(root):
  def dfs(node):
    log("N: {}", node.node)
    if len(node.children) == 0 or len(node.children) == 2:
      return sum([dfs(c) for c in node.children])
    if len(node.children) == 1:
      return node.children[0].size
    
    cs = [(c.size, dfs(c)) for c in node.children]
    cs.sort(key=lambda x: (x[0], x[0]-x[1]), reverse=True)
    return cs[0][1] + cs[1][1] + sum(map(itemgetter(0), cs[2:]))


    #childs = sorted(node.children, key=attrgetter('size'), reverse=True)
    #return dfs(childs[0]) + dfs(childs[1]) + sum(map(attrgetter('size'), childs[2:]))

  return dfs(root)

class Case:
  def __init__(self, i, edges):
    self.i = i
    self.edges = edges

  def solve(self):
    log("Solving: {}", self)
    counts = []
    for n in self.edges.keys():
      tree = build_tree(n, self.edges)
      cnt = prune_tree(tree)
      #print_tree(tree)
      log("####{}",cnt)
      counts.append(cnt)

    sol = str(min(counts))
    return self.case() + sol

  def case(self):
    return "Case #{}: ".format(self.i)

  def __repr__(self):
    return self.case() + str(self.edges)

def parse_input(stream):
  cases = []
  T = int(stream.readline())
  for i in range(1, T+1):
    N = int(stream.readline())
    edges = collections.defaultdict(list)
    for j in range(N-1):
      n1,n2 = map(int, stream.readline().split())
      edges[n1].append(n2)
      edges[n2].append(n1)
    # parse case input
    cases.append(Case(i, edges))
  return cases

def main():
  sys.setrecursionlimit(1500)
  options = parse_args()
  cases = parse_input(sys.stdin)
  for case in cases:
    if not options.case or options.case == case.i:
      print(case.solve())
      sys.stdout.flush()


main()
  
