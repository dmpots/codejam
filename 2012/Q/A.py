#!/usr/bin/env python3

import sys
import re

translation = {97: 121, 98: 104, 99: 101, 100: 115, 101: 111, 102: 99, 103: 118, 104: 120, 105: 100, 106: 117, 107: 105, 108: 103, 109: 108, 110: 98, 111: 107, 112: 114, 113: 122, 114: 116, 115: 110, 116: 119, 117: 106, 118: 112, 119: 102, 120: 109, 121: 97, 122: 113}

def train(inp):
    trans = {}
    src = inp.readline()
    while src:
        target = inp.readline()
        target = target.replace(" ", "").replace("\n", "")
        src    = src.replace(" ", "").replace("\n", "")
        trans.update(str.maketrans(src, target))
        src = inp.readline()

    trans.update({ord('z') : ord('q')})
    trans.update({ord('q') : ord('z')})
    return trans

def print_trans(trans):
    print("{")
    items = []
    for (x,y) in trans.items():
        items.append("  {} : {}".format(chr(x), chr(y)))
    print(",\n".join(items))
    print("}")

def run_trans(inp):
    inp.readline() # size
    for (i, line) in enumerate(inp, start=1):
        line = line.rstrip()
        print("Case #{}: {}".format(i, line.translate(translation)))
    

def main():
    inp = sys.stdin
    training = False
    if training:
        trans = train(inp)
        print_trans(trans)
        print(trans)
    else:
        run_trans(inp)

        
if __name__ == "__main__":
    main()
