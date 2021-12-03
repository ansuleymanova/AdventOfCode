def dive(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        units = int(command[1])
        if command[0] == 'forward':
            horizontal += units
            depth += aim * units
        elif command[0] == 'down':
            aim += units
        else:
            aim -= units
    return depth * horizontal


def main():
    commands = []
    while True:
        try:
            inp = input().split()
            if not inp:
                break
            commands.append(inp)
        except SyntaxError:
            break
    multiplication = dive(commands)
    print(multiplication)


if __name__ == '__main__':
    main()
