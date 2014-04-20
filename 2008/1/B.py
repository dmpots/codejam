#!/usr/bin/env python3

import sys

class Solution(Exception):
    def __init__(self, assignment):
        self.assignment = assignment

def solve(clauses):
    try:
        dpll({}, clauses)
    except Solution as sol:
        return sol.assignment
    return None

def dpll(assignment, clauses):
    if len(clauses) == 0:
        raise Solution(assignment)
    
    # check unsolvable clauses
    for clause in clauses:
        if len(clause) == 0:
            return False

    # check forced assignments
    forced = []
    for clause in clauses:
        if len(clause) == 1:
            forced.append(clause[0])
    for (flavor, value) in forced:
        #print("F")
        (clauses, assignment) = assign(assignment, clauses, flavor, value)

    # check pure assignmetns
    pure = set()
    ways = {}
    for clause in clauses:
        for flavor,value in clause:
            pure.add(flavor)
            ways[flavor] = value
    for clause in clauses:        
        for flavor,value in clause:
            if ways[flavor] != value and flavor in pure:
                pure.remove(flavor)
    #for flavor in pure:
    #    print("P")
    #    (clauses, assignment) = assign(assignment, clauses, flavor, ways[flavor])

    if len(clauses) == 0:
        raise Solution(assignment)

    for clause in clauses:
        if len(clause) == 0:
            return False  

    # assign least malted flavor
    #print("C")
    nmcounts = {}
    mcounts = {}
    for clause in clauses:
        for (flavor, malted) in clause:
            if malted:
                mcounts[flavor] = mcounts.get(flavor,0) + 1
            else:
                nmcounts[flavor] = nmcounts.get(flavor,0) + 1

    oc, oa = clauses, assignment
    if len(nmcounts) > 0:
        (flavor,_c) = max(nmcounts.items(),  key=lambda c: c[1]) 
        clauses,assignment = assign(assignment, clauses, flavor, False)
        if not dpll(assignment, clauses):
            clauses,assignment = assign(oa, oc, flavor, True)
            return dpll(assignment, clauses)
    else:
        (flavor,_c) = max(mcounts.items(),  key=lambda c: c[1]) 
        clauses,assignment = assign(assignment, clauses, flavor, True)
        if not dpll(assignment, clauses):
            clauses,assignment = assign(oa, oc, flavor, False)
            return dpll(assignment, clauses)

    return False


    
def assign(assignment, clauses, flavor, value):
    newA = assignment.copy()
    newC = []

    newA[flavor] = value
    for clause in clauses:
        c = []
        erase = False
        for f,v in clause:
            # remove clause if it is satisfied
            if f == flavor and v == value:
                erase = True
            # remove term if it is negated
            elif (f == flavor) and (v == (not value)):
                pass
            # otherwise let it be
            else:
                c.append((f,v))
        if not erase:
            newC.append(c)
    #print("A({}) = {}: {}".format(flavor, value, newA))
    return newC,newA

def main():
    ifp = sys.stdin
    ofp = sys.stdout

    C = int(ifp.readline())
    for c in range(1, C+1):
        #if c == 44:
        #    print(" ".join(ifp.readlines()[:15]))
        N = int(ifp.readline())
        M = int(ifp.readline())
        clauses = []
        for i in range(0, M):
            customer = ifp.readline().split()
            T = int(customer.pop(0))
            clause = []
            for x in range(0, T):
                X = int(customer.pop(0))
                Y = bool(int(customer.pop(0)))
                clause.append((X,Y))
            clauses.append(clause)

        sol = solve(clauses)
        if sol:
            print("Case #{}: ".format(c), end="",file=ofp)
            for f in range(1, N+1):
                if f in sol:
                    print(int(sol[f]),end=" ",file=ofp)
                else:
                    print(0, end=" ",file=ofp)
            print()
        else:
            print("Case #{}: {}".format(c, "IMPOSSIBLE"), file=ofp)
        ofp.flush()
        
if __name__ == "__main__":
    main()
