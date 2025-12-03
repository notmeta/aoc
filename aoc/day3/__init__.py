import itertools
from typing import override

from aoc import Aoc


class Solution(Aoc):
    @override
    def part1(self, data: list[str]) -> str:
        sum = 0
        for battery_bank in data:
            if not battery_bank:
                break
            sum += int(sorted([left + right for left, right in itertools.combinations(battery_bank, 2)], reverse=True)[0])
        return str(sum)

    @override
    def part2(self, data: list[str]) -> str:
        raise NotImplementedError()
