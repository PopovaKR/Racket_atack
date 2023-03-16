from sys import argv, exit
from math import sqrt


def get_target(XYW: list, R: float) -> list:
    while True:
        sum_W = sum(XYW[2])

        Xc = sum([x * w for x, w in zip(XYW[0], XYW[2])]) / sum_W
        Yc = sum([y * w for y, w in zip(XYW[1], XYW[2])]) / sum_W

        ED = [sqrt((x - Xc) ** 2 + (y - Yc) ** 2) for x, y in
              zip(XYW[0], XYW[1])]
        ED_max = max(ED)
        ED_max_index = ED.index(ED_max)

        if ED_max > R:
            del XYW[0][ED_max_index], XYW[1][ED_max_index], XYW[2][
                ED_max_index]
        else:
            return [XYW[0][ED_max_index], XYW[1][ED_max_index], sum_W]


def main():
    if len(argv) < 2:
        raise IndexError('Incorrect number of entered variables')

    path, R = argv[1], argv[2]
    if not all([R.isdigit(), float(R) > 0]):
        raise ValueError('Invalid type of entered data')

    with open(path) as file:
        XYW = [[], [], []]
        for line in file.readlines():
            x, y, w = line.split()
            XYW[0].append(float(x))
            XYW[1].append(float(y))
            XYW[2].append(float(w))

    print(get_target(XYW, float(R)))


if __name__ == '__main__':
    exit(main())
