from typing import override

from aoc import Aoc


class Solution(Aoc):
    @override
    def part1(self, data: list[str]) -> str:
        sum = 0
        for line in data:
            start = line.split("-")[0]
            end = line.split("-")[1]
            for id_to_check in range(int(start), int(end) + 1):
                id_as_str = str(id_to_check)
                id_length = len(id_as_str)
                if id_length % 2 == 1:  # pip install is_even
                    # if the string is an odd number in length then we can't evenly split it in two
                    continue
                # is the first half equal to the second half
                if id_as_str[int(id_length / 2) :] == id_as_str[: int(id_length / 2)]:
                    sum += id_to_check

        return str(sum)

    @override
    def part2(self, data: list[str]) -> str:
        sum = 0
        for line in data:
            start = line.split("-")[0]
            end = line.split("-")[1]
            for id_to_check in range(int(start), int(end) + 1):
                id_as_str = str(id_to_check)
                cumulative = ""
                for num in id_as_str:
                    cumulative += num
                    if cumulative == id_as_str:
                        break
                    # can we split the id cleanly without leaving anything remaining?
                    if not any(id_as_str.split(cumulative)):
                        sum += id_to_check
                        break

        return str(sum)
