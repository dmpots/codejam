#!/usr/bin/env python3

import sys

dups = set()

def recycled(n, b):
    count = 0
    ns = str(n)
    if len(ns) <= 1:
        return 0

    for i in range(1, len(ns)):
        ms = ns[i:] + ns[:i]
        m = int(ms)
        if m <= b and n < m:
            r = (n,m)
            if r not in dups:
                dups.add(r)
                count += 1
    return count

def solve(a, b):
    dups.clear()
    return sum([recycled(n, b) for n in range(a, b+1)])

def main():
    inp = sys.stdin

    inp.readline()
    for (i,line) in enumerate(inp, start=1):
        (a, b) = line.split()
        sol = solve(int(a), int(b))
        print("Case #{}: {}".format(i, sol))
        sys.stdout.flush()
        
if __name__ == "__main__":
    main()
