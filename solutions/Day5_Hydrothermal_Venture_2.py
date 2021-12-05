# this is a mess and i am truly sorry but it's way past midnight goodbye

def hydrothermal_venture(entries, x_max, y_max):
    row = [0] * (x_max + 1)
    matrix = [([0] * (x_max + 1)) for count in range(y_max + 1)]
    for entry in entries:
        x1 = entry[0]
        x2 = entry[2]
        y1 = entry[1]
        y2 = entry[3]
        x_movement = abs(x2 - x1)
        y_movement = abs(y2 - y1)
        x = min(x1, x2)
        y = min(y1, y2)
        if x1 == x2 or y1 == y2:
            if y_movement == 0:
                for i in range(x_movement + 1):
                    matrix[y][x + i] += 1
            else:
                for i in range(y_movement + 1):
                    matrix[y + i][x] += 1
        else:
            for i in range(y_movement + 1):
                if (y1 < y2 and x1 > x2) or (y1 > y2 and x1 < x2):
                    matrix[y + y_movement - i][x + i] += 1
                else:
                    matrix[y + i][x + i] += 1
    overlap_counter = 0
    for row in matrix:
        for point in row:
            if point >= 2:
                overlap_counter += 1
    return overlap_counter


def main():
    entries = []
    xs = []
    ys = []
    # taking in indeterminate number of input strings
    while True:
        try:
            inp = input().split()
            if not inp:
                break
            a = inp[0].split(',')
            b = inp[2].split(',')
            entry = [int(i) for i in (a[0], a[1], b[0], b[1])]
            xs.append(int(a[0]))
            xs.append(int(b[0]))
            ys.append(int(a[1]))
            ys.append(int(b[1]))
            entries.append(entry)
        except SyntaxError:
            break
    x_max = max(xs)
    y_max = max(ys)
    result = hydrothermal_venture(entries, x_max, y_max)
    print(result)


if __name__ == '__main__':
    main()
