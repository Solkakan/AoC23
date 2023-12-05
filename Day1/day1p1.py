from pathlib import Path


def main():

    data = Path(r'C:\Users\johan\AoC23\Day1\input.txt')

    with open(data) as f:
        content = f.readlines()

    total = 0

    for line in content:
        total += linecalc(line)

    print(total)


def linecalc(line):
    out = []
    for element in line:
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

    nums = [out[0], out[-1]]
    value = "".join(str(item) for item in nums)
    return int(value)


if __name__ == "__main__":
    main()
