#!/usr/bin/env python3

import json

def more_even(i):
    nstr = str(i)
    nevens = 0
    for d in map(int, nstr):
        if d % 2 == 0:
            nevens += 1
    nodds = len(nstr) - nevens 
    return nevens > nodds

def main():
    ns = [30, 0, 1, 2, 3, 4, 10, 27, 64]    
    test_cases = []
    for n in ns:
        ev = []
        for i in range(1, n + 1):
            if more_even(i):
                ev.append(i)
        test_cases.append((n, "\n".join(map(str, ev))))
    for t in test_cases:
        print(f"{json.dumps(t)},")
    return 0


if __name__ == '__main__':
    exit(main())
