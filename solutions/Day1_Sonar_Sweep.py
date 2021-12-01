def sonar_sweep(depths):
    last_depth = 0
    increases_counter = 0
    for depth in depths:
        if last_depth == 0:
            last_depth = depth
        else:
            if depth > last_depth:
                increases_counter += 1
                last_depth = depth
            else:
                last_depth = depth
    return increases_counter


def main():
    depths = []
    measurement_a = int(input())
    measurement_b = int(input())
    measurement_c = int(input())
    depths.append(measurement_a + measurement_b + measurement_c)
    while True:
        try:
            inp = int(input())
            measurement_a = measurement_b
            measurement_b = measurement_c
            measurement_c = inp
            depths.append(measurement_a + measurement_b + measurement_c)
        except SyntaxError:
            break
    print(depths)
    num_of_increases = sonar_sweep(depths)
    print(num_of_increases)


if __name__ == '__main__':
    main()
