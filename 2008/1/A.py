#!/usr/bin/env python3

import sys

def dotp(xs, ys):
    return sum([x * y for (x,y) in zip(xs,ys)])

def solve(xs, ys):
    return dotp(sorted(xs), sorted(ys, reverse=True))

def main():
    ifp = sys.stdin
    ofp = sys.stdout

    T = int(ifp.readline())
    for i in range(1, T+1):
        n  = ifp.readline()
        xs = map(int, ifp.readline().split())
        ys = map(int, ifp.readline().split())
        sol = solve(xs, ys)
        print("Case #{}: {}".format(i, sol), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
