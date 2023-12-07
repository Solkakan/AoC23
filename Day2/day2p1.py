from pathlib import Path


def main():
    data = Path(r"C:\Users\johan\AoC23\Day1\input2.txt")

    with open(data, encoding="utf-8") as f:
        content = f.readlines()

    total = 0

    for line in content:
        switch, value = calc(line)
        if switch:
            total += value
        else:
            continue

    print(total)


def calc(game):
    ident, sets = game.split(": ")
    ident_num = int(ident[-1])
    sets = sets.split("; ")
    max_counts = {}

    for set_data in sets:
        items = set_data.split(", ")

        for item in items:
            count, color = item.split(" ")
            count = int(count)

            if color not in max_counts:
                max_counts[color] = count
                p
            else:
                max_counts[color] = max(max_counts[color], count)

        if (
            max_counts["red"] <= 12
            and max_counts["green"] <= 13
            and max_counts["blue"] <= 14
        ):
            return True, ident_num
        return False, ident_num
