from enum import Enum
from typing import NamedTuple
from operator import attrgetter


class Action(Enum):
    BREAK = 2
    PLACE = 1

    @property
    def cost(self):
        return self.value


class Result(NamedTuple):
    cost: int
    height: int


def costs(sorted_space: list[int], height: int, initial_items: int) -> Result:
    items = initial_items
    t = 0
    for block in sorted_space:
        if block > height:
            diff = block - height
            items += diff
            t += diff * Action.BREAK.cost
        if block < height:
            diff = height - block
            if items >= diff:
                items -= diff
                t += diff * Action.PLACE.cost
            else:
                return Result(-1, height)
    return Result(t, height)


def main():
    n, m, b = map(int, input().split())
    s = []
    for _ in range(n):
        s += list(map(int, input().split()))
    s.sort(reverse=True)
    samples = list[Result]()
    for h in range(0, 256 + 1):
        samples.append(costs(s, h, b))

    samples = list(filter(lambda sample: sample.cost >= 0, samples))
    minimal_cost = min(samples, key=attrgetter("cost")).cost

    samples = list(filter(lambda sample: sample.cost == minimal_cost, samples))
    maximum_height = max(samples, key=attrgetter("height")).height

    print(minimal_cost, maximum_height)


main()
