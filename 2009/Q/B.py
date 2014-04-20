#!/usr/bin/env python3

import sys

def solve(W,H, em):
    dm = []
    sol = []
    for r in range(0,H):
        sol.append([])
        dm.append([])
        for c in range(0,W):
            dm[r].append(-1)
            sol[r].append(-1)
    basin = 0
    for r in range(0,H):
        for c in range(0,W):
            e = em[r][c]
            elevs = [e]
            # N
            if r != 0:
                elevs.append(em[r-1][c])
                
            # S
            if r != H-1:
                elevs.append(em[r+1][c])
            # E
            if c != W-1:
                elevs.append(em[r][c+1])
            # W
            if c != 0:
                elevs.append(em[r][c-1])

            if min(elevs) == e:
                dm[r][c] = basin
                basin += 1

    for row in range(0,H):
        for col in range(0,W):
            pos = row,col
            d = dm[row][col]
            while d < 0:
                r,c = pos
                e   = em[r][c]
                ne = 10000
                #N
                if r != 0 and em[r-1][c] < ne:
                    pos = r-1,c
                    ne  = em[r-1][c]
                    d   = dm[r-1][c]
                #W
                if c != 0 and em[r][c-1] < ne:
                    pos = r,c-1
                    ne = em[r][c-1]
                    d = dm[r][c-1]
                #E
                if c != W-1 and em[r][c+1] < ne:
                    pos = r,c+1
                    ne = em[r][c+1]
                    d = dm[r][c+1]
                #S
                if r != H-1 and em[r+1][c] < ne:
                    pos = r+1,c
                    ne = em[r+1][c]
                    d = dm[r+1][c]
            sol[row][col] = d

    lex = {}
    i = 0
    for r in range(0,H):
        for c in range(0,W):
            if sol[r][c] not in lex:
                lex[sol[r][c]] = chr(97+i)
                i += 1
            sol[r][c] = lex[sol[r][c]]
    return sol

def main():
    ifp = sys.stdin
    ofp = sys.stdout

    N = int(ifp.readline())
    for i in range(1,N+1):
        H,W = map(int, ifp.readline().split())

        em = []
        for j in range(0,H):
            row = list(map(int, ifp.readline().split()))
            em.append(row)

        print("Case #{}:".format(i))
        sol = solve(W,H,em)
        for row in sol:
            print(' '.join(map(str,row)), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
