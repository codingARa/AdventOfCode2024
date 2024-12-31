def getTestInput():
    return [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]


def getInput():
    with open("input.txt") as file:
        line = [l for l in file.read().split("\n") if l]
    return line


def solution_part1(input) -> int:
    save_reports = len(input)
    print("inital no of save reports: ", save_reports)
    for report in input:
        nums = [int(x) for x in report.split(" ")]
        print("nums", nums)
        diffs = [a - b for a, b in zip(nums[:-1], nums[1:])]
        print("diffs", diffs)

        zeros = diffs.count(0)
        if zeros > 0:
            print("zeros", zeros)
            save_reports -= 1
            print("---")
            continue

        too_steep = any(abs(d) > 3 for d in diffs)
        if too_steep:
            print("too steep")
            save_reports -= 1
            print("---")
            continue

        ascending = all(a < b and b - a <= 3 for a, b in zip(nums[:-1], nums[1:]))
        print("ascending", ascending)
        descending = all(a > b and abs(a - b) <= 3 for a, b in zip(nums[:-1], nums[1:]))
        print("descending", descending)

        if not ascending and not descending:
            print("no strikt inclination")
            save_reports -= 1
            print("---")
            continue
        print("---")

    return save_reports


def solution_part2(input) -> int:
    save_reports = len(input)
    unsave_reports = 0
    for report in input:
        nums = [int(x) for x in report.split(" ")]
        check = check_single_array(nums)
        if not check:
            unsave_reports -= 1

    return save_reports - unsave_reports


def check_single_array(nums):
    # TODO-ARA: funktioniert so noch nicht wie gefordert
    i = 0
    error_count = 0
    ascending = True
    for a, b in zip(nums[nums:-1], nums[1:]):
        if error_count > 1:
            break
        if a == b:
            error_count += 1
        elif a > b:
            ascending = False
        diff = abs(a - b)
        if diff > 3:
            error_count += 1
            break
        i += 1


def test_part1():
    test_input = getTestInput()
    assert solution_part1(test_input) == 2


def test_part2():
    test_input = getTestInput()
    assert solution_part2(test_input) == 4


if __name__ == "__main__":
    input = getInput()

    sol1 = solution_part1(input)
    print("Part 1: ", sol1)

    sol2 = solution_part2(input)
    print("Part 2: ", sol2)
