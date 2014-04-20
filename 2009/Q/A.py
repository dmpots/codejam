#!/usr/bin/env python3

import sys

def solve(words, prob):
    cnt = 0
    for w in words:
        for (i,c) in enumerate(w):
            if c not in prob[i]:
                break
        else:
            cnt += 1
    return cnt

def main():
    ifp = sys.stdin
    ofp = sys.stdout

    L,D,N = map(int, ifp.readline().split())

    words = set()
    for i in range(0, D):
        words.add(ifp.readline().rstrip())
        
    for i in range(1, N+1):
        pattern = ifp.readline().rstrip()
        prob = []
        c = 0
        state = 0
        for c in pattern:
            if c == "(":
                state = 1
                prob.append("")
            elif c == ")":
                state = 0
            else:
                if state == 0:
                    prob.append(c)
                elif state == 1:
                    prob[-1] += c
        
                    #print(prob)
        sol = solve(words, prob)
        print("Case #{}: {}".format(i, sol), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
