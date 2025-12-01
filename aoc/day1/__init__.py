from typing import override

from aoc import Aoc


class Solution(Aoc):
    @override
    def part1(self, data: list[str]) -> str:
        # how many times do we land on zero?

        zero_hits = 0
        dial_position = 50

        for line in data:
            if not line:
                break
            direction = line[0]
            turns = int(line[1:])

            for _ in range(turns):
                if direction == "R":
                    dial_position += 1
                elif direction == "L":
                    dial_position -= 1

                dial_position %= 100  # keep the dial between 0-99

            if dial_position == 0:
                zero_hits += 1

        return str(zero_hits)

    @override
    def part2(self, data: list[str]) -> str:
        # how many times do we see zero?

        zero_occurances = 0
        dial_position = 50

        for line in data:
            if not line:
                break
            direction = line[0]
            turns = int(line[1:])

            for _ in range(turns):
                if direction == "R":
                    dial_position += 1
                elif direction == "L":
                    dial_position -= 1

                dial_position %= 100  # keep the dial between 0-99

                if dial_position == 0:
                    zero_occurances += 1

        return str(zero_occurances)
