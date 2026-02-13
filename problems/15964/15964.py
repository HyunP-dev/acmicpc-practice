def at(a, b):
    return (a + b) * (a - b)


print(at(*map(int, input().split())))
