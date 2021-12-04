def gamma_rate(strings):
    sum_list = [0] * len(strings)
    # first we sum the 1's in every position
    for string in strings:
        for index, bit in enumerate(string):
            sum_list[index] += int(bit)
    # then we check if the average for the position is over 0,5
    # if it is, then there were more 1's than 0's
    for index, sum in enumerate(sum_list):
        if sum / len(strings) >= 0.5:
            # if there's a tie, we should also select 1
            sum_list[index] = '1'
        else:
            sum_list[index] = '0'
    return ''.join(sum_list)


def epsilon_rate(gamma):
    # this function puts 0's in place of 1's in the string
    # there's probably a better way to work with binary than strings,
    # but this way is a little more efficient as I don't need to convert
    epsilon = ['0'] * len(gamma)
    for index, bit in enumerate(gamma):
        if bit == '0':
            epsilon[index] = '1'
    return ''.join(epsilon)


def main():
    strings = []
    # taking in indeterminate number of input strings
    while True:
        try:
            inp = input()
            if not inp:
                break
            strings.append(inp)
        except SyntaxError:
            break
    gamma = gamma_rate(strings)
    epsilon = epsilon_rate(gamma)
    result = int(gamma, 2) * int(epsilon, 2)
    print(result)


if __name__ == '__main__':
    main()
