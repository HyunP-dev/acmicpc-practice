from math import sqrt


def filter_(p, min_, max_):
    p2 = p * p
    start = min_ // p2 * p2
    for i in range(1_000_000+1):
        if (e := start + p2 * i) <= max_:
            yield e
        else:
            break


def main():
    min_, max_ = map(int, input().split())
    sieve = set(range(min_, max_ + 1))
    for p in range(2, int(sqrt(max_ + 1) + 1)):
        sieve -= set(filter_(p, min_, max_))       
    print(len(list(sieve)))


if __name__ == "__main__":
    main()
