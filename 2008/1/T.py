#!/usr/bin/env python3

import sys

def solve():
    pass

def main():
    ifp = sys.stdin
    ofp = sys.stdout

    N = int(ifp.readline())
    for (i,line) in enumerate(ifp, start=1):
        sol = solve()
        print("Case #{}: {}".format(i, sol), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
