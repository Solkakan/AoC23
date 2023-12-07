from pathlib import Path


def main():
    data = Path(r"C:\Users\johan\AoC23\Day2\input.txt")

    with open(data) as f:
        content = f.readlines()

    total = 0

    for line in content:
        switch, value = calc(line)

        if switch:
            total += value
            print(f"VAL: {value}")
            print(f"TOT: {total}")
            print(f"LINE: {line}")

        else:
            continue

    print(total)


def calc(game):
    ident, sets = game.split(": ")
    ident = ident.split()
    ident_num = int(ident[-1])
    sets = sets.split("; ")
    max_counts = {"red": 0, "green": 0, "blue": 0}

    for set_data in sets:
        items = set_data.split(", ")

        for item in items:
            count, color = item.split(" ")
            count = int(count)
            color = color.rstrip()
            if color not in max_counts:
                max_counts[color] = count
                print(f"ID: {ident} MAX: {max_counts}")

            else:
                max_counts[color] = max(max_counts[color], count)
                print(f"ID: {ident} MAX: {max_counts}")
    if (
        max_counts["red"] <= 12
        and max_counts["green"] <= 13
        and max_counts["blue"] <= 14
    ):
        return True, ident_num
    return False, 0


if __name__ == "__main__":
    main()
