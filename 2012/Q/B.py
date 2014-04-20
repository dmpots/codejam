#!/usr/bin/env python3

import sys

INVALID   = 0
VALID     = 1
SUPRISE   = 2

def maxdist(x,y):
    return max(abs(x), abs(y), abs(x - y))

def hit(xs, t):
    return any(map(lambda s: sum(s) == t, xs))

def gen(p, limit):
    def valid(s):
        for i in [0,1,2]:
            if s[i] > 10 or s[i] < 0:
                return False
        return True

    ranges = [0,1,-1,2,-2]
    elems = [(p, p+x, p+y) for x in ranges for y in ranges if maxdist(x,y) <= limit]
    return filter(valid, elems)

def search(p, t):
    for g in range(p, 11):
        valid = gen(g, 1)
        if hit(valid, t):
            return VALID
    for g in range(p, 11):
        suprise = gen(g, 2)
        if hit(suprise, t):
            return SUPRISE

    return INVALID
        

def solve(s, p, ts):
    hits = 0
    surprises_left = s
    for t in ts:
        res = search(p, t)
        if res == VALID:
            hits += 1
        elif res == SUPRISE and surprises_left > 0:
            hits += 1
            surprises_left -= 1
    return hits

def main():
    inp = sys.stdin

    inp.readline()
    for (i,line) in enumerate(inp, start=1):
        problem = line.split()
        s = int(problem[1])
        p = int(problem[2])
        ts = map(int, problem[3:])

        sol = solve(s, p, ts)
        print("Case #{}: {}".format(i, sol))
        sys.stdout.flush()
        
if __name__ == "__main__":
    main()
