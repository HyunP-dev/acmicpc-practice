import sys

input = sys.stdin.readline

S = 0
m = int(input())
for _ in range(m):
    line = input()
    tokens = line.split(maxsplit=1)
    if len(tokens) > 1:
        op, value = tokens
        value = int(value)

        if op == "add":
            S |= 1 << (value - 1)
        if op == "remove":
            S &= ~(1 << (value - 1))
        if op == "check":
            if S & 1 << (value - 1):
                sys.stdout.write("1\n")
            else:
                sys.stdout.write("0\n")
        if op == "toggle":
            S ^= 1 << (value - 1)
    else:
        op = tokens[0]
        if op == "all":
            S = 0b11111111111111111111
        if op == "empty":
            S = 0
