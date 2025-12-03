from aoc import day3

if __name__ == "__main__":
    day3 = day3.Solution()

    print("Part 1:", day3.part1(open("aoc/day3/part1.txt").read().split("\n")))
    print("Part 2:", day3.part2(open("aoc/day3/part1.txt").read().split(",")))
