from typing import NamedTuple
from operator import attrgetter


class Choco(NamedTuple):
    height: int
    width: int

    @staticmethod
    def of(pair: tuple[int, int]):
        return Choco(*pair)

    @property
    def size(self):
        return self.height * self.width


n = int(input())
hs = [int(s) for s in input().split()]
ws = [int(s) for s in input().split()]
chocos = [Choco.of(pair) for pair in zip(hs, ws)]
chocos = reversed(sorted(chocos, key=attrgetter("height")))

total_width = 0
maximum_size = 0
for choco in chocos:
    total_width += choco.width
    if total_width * choco.height > maximum_size:
        maximum_size = total_width * choco.height
print(maximum_size)
