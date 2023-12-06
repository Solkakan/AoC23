from pathlib import Path


def main():
    data = Path(r"C:\Users\johan\AoC23\Day1\input2.txt")

    with open(data, encoding="utf-8") as f:
        content = f.readlines()

    total = 0

    for line in content:
        total += linecalc(line)

    print(total)


def linecalc(line):
    out = []
    for index, element in enumerate(line):
        match element:
            case "1":
                out.append(1)
            case "2":
                out.append(2)
            case "3":
                out.append(3)
            case "4":
                out.append(4)
            case "5":
                out.append(5)
            case "6":
                out.append(6)
            case "7":
                out.append(7)
            case "8":
                out.append(8)
            case "9":
                out.append(9)
            case "0":
                out.append(0)
            case _:
                result, val = chareval(element, index, line)
                if result:
                    out.append(val)
                else:
                    continue

    nums = [out[0], out[-1]]
    value = "".join(str(item) for item in nums)
    return int(value)


def chareval(char, index, line):
    match char:
        case "o":
            if index + 2 < len(line) and (
                line[index + 1] == "n" and line[index + 2] == "e"
            ):
                return True, 1
            return False, 0

        case "t":
            if index + 2 < len(line) and (
                line[index + 1] == "w" and line[index + 2] == "o"
            ):
                return True, 2
            if index + 3 < len(line) and (
                line[index + 1] == "h"
                and line[index + 2] == "r"
                and line[index + 3] == "e"
                and line[index + 4] == "e"
            ):
                return True, 3
            return False, 0

        case "f":
            if index + 3 < len(line) and (
                line[index + 1] == "o"
                and line[index + 2] == "u"
                and line[index + 3] == "r"
            ):
                return True, 4
            if index + 4 < len(line) and (
                line[index + 1] == "i"
                and line[index + 2] == "v"
                and line[index + 3] == "e"
            ):
                return True, 5
            return False, 0

        case "s":
            if index + 3 < len(line) and (
                line[index + 1] == "i" and line[index + 2] == "x"
            ):
                return True, 6
            if index + 4 < len(line) and (
                line[index + 1] == "e"
                and line[index + 2] == "v"
                and line[index + 3] == "e"
                and line[index + 4] == "n"
            ):
                return True, 7
            return False, 0

        case "e":
            if index + 4 < len(line) and (
                line[index + 1] == "i"
                and line[index + 2] == "g"
                and line[index + 3] == "h"
                and line[index + 4] == "t"
            ):
                return True, 8
            return False, 0

        case "n":
            if index + 3 < len(line) and (
                line[index + 1] == "i"
                and line[index + 2] == "n"
                and line[index + 3] == "e"
            ):
                return True, 9
            return False, 0

    return False, 0


if __name__ == "__main__":
    main()
