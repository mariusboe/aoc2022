def day_one():
    with open("input.txt") as f:
        x: dict = []
        current: int = 0
        for kcal in [line.rstrip() for line in f.readlines()]:
            if kcal:
                current += int(kcal)
            else:
                x.append(current)
                current = 0
        print(max(x))
        print(sum(sorted(x, reverse=True)[0:3]))


day_one()
