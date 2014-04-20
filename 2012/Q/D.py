#!/usr/bin/env python3

import sys

M= "#"
E= "."
I= "X"


class Board:
    def __init__(self, w,h):
        self.width  = w
        self.height = h
        self.board  = [["!"] * h for x in range(0,w)]

    def __getitem__(self, x):
        return self.board[x]

    def __repr__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self[x][y]
            s += "\n"
        return s

class Ray:
    def __init__(self, x,y,theta):
        self.x = x
        self.y = y
        self.theta = theta




def main():
    inp = sys.stdin   

    T = int(inp.readline())
    for i in range(1, T+1):
        prob = inp.readline().split()
        H = int(prob[0])
        W = int(prob[1])
        D = int(prob[2])

        B = Board(w=W, h=H)
        for y in range(0, H):
            line = inp.readline().rstrip()
            for (x, c) in enumerate(line):
                B[x][y] = c
                if c == "X":
                    B.start = (x,y)
                    print(B.start)

        sol = 9
        print("Case #{}: {}".format(i, sol))
        print(B)
        sys.stdout.flush()
        
if __name__ == "__main__":
    main()
