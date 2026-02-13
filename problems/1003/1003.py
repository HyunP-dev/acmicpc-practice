from typing import NamedTuple
from functools import cache


class Writer[V, N](NamedTuple):
    value: V
    note: N

    def __add__(self, other):
        value = self.value + other.value
        note = self.note + other.note
        return Writer(value, note)


class Counter(NamedTuple):
    zero: int
    one: int

    def __add__(self, other):
        return Counter(self.zero + other.zero, self.one + other.one)


Counted = Writer[int, Counter]


@cache
def fibonacci(n: Counted) -> Counted:
    if n.value == 0:
        return Counted(value=0, note=Counter(n.note[0] + 1, n.note[1]))
    if n.value == 1:
        return Counted(value=1, note=Counter(n.note[0], n.note[1] + 1))

    left = Counted(n.value - 1, n.note)
    right = Counted(n.value - 2, n.note)
    return fibonacci(left) + fibonacci(right)


def count(n: int):
    ic = Counter(0, 0)
    result = fibonacci(Counted(n, ic))
    counter = result.note
    print(counter.zero, counter.one)


t = int(input())
for _ in range(t):
    n = int(input())
    count(n)
