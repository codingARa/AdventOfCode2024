def getTestInput():
    l1 = [3, 4, 2, 1, 3, 3]
    l2 = [4, 3, 5, 3, 9, 3]
    return {"l1": l1, "l2": l2}


def getInput():
    with open("input.txt") as file:
        raw = file.read().split("\n")
    num1, num2 = [], []
    for r in raw:
        n1, n2 = r.split("   ")
        num1.append(int(n1))
        num2.append(int(n2))
    return {"l1": num1, "l2": num2}


def solution_part1(input):
    l1 = input["l1"]
    l2 = input["l2"]

    l1 = sorted(l1)
    l2 = sorted(l2)
    diff = [abs(x1 - x2) for x1, x2 in zip(l1, l2)]
    return sum(diff)


def solution_part2(input):
    l1 = input["l1"]
    l2 = input["l2"]

    l1 = sorted(l1)
    l2 = sorted(l2)

    result = 0
    for i in l1:
        c = l2.count(i)
        result += c * i

    return result


def test_part1():
    test_input = getTestInput()
    assert solution_part1(test_input) == 11


def test_part2():
    test_input = getTestInput()
    assert solution_part2(test_input) == 31


if __name__ == "__main__":
    input = getInput()

    sol1 = solution_part1(input)
    print("Part 1: ", sol1)

    sol2 = solution_part2(input)
    print("Part 2: ", sol2)
