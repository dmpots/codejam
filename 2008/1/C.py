#!/usr/bin/env python3

import sys
import math

s5 = 22360679774997896964091736687312762354406183596115257242708972454105209256378048994144144083787822750
sig = 10**100

def mul(x,y):
    const = x[0]*y[0] + x[1]*y[1] * 5
    sqrt  = x[0] * y[1] + x[1] * y[0]

    (_,const) = divmod(const, sig)
    (_,sqrt) = divmod(sqrt, sig)
    return [const, sqrt]

def fast(n, x):
    s = 1
    while (s*2) < n:
        x = mul(x,x)
        s = s * 2

        #print("S: "+str(s)+" R: "+str(n-s))
    return (n-s, x)

def expand(x):
    #print("E")
    b,a = divmod((x[1] * sig * s5), sig*sig)
    b = b + x[0]

    #print("X: ",x,"A: ",a, "B: ",b)
    bs   = str(b)
    digs = bs[-3:]
    digs = "0"*(3-len(digs))+digs

    return digs

def solve(n):
    x = [3, 1]
    first = True
    while n > 0:
        #print("N: "+str(n))
        n,y = fast(n,[3,1])
        if first:
            first = False
            x = y
        else:
            x = mul(x,y)
    return expand(x)
 
def main():
    ifp = sys.stdin
    ofp = sys.stdout

    N = int(ifp.readline())
    for (i,line) in enumerate(ifp, start=1):
        n = int(line)
        sol = solve(n)
        print("Case #{}: {}".format(i, sol), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
