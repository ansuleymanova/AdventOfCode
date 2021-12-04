def oxygen_rating(strings, counter):
    # exit recursion when all positions have been looped
    # or if there's only one number left
    if counter == len(strings[0]) or len(strings) == 1:
        return strings[0]
    sum = 0
    positional_mode = '0'
    for string in strings:
        if string[counter] == '1':
            sum += 1
    if sum / len(strings) >= 0.5:
        positional_mode = '1'
    oxygen = []
    # if the number has positional mode in the currently looped position,
    # add the number to the list
    for string in strings:
        if string[counter] == positional_mode:
            oxygen.append(string)
    counter += 1
    return oxygen_rating(oxygen, counter)


# this function doesn't follow DRY
# and should be refactored someday when I'm bored
def co2_rating(strings, counter):
    if counter == len(strings[0]) or len(strings) == 1:
        return strings[0]
    sum = 0
    positional_mode = '0'
    for string in strings:
        if string[counter] == '1':
            sum += 1
    if sum / len(strings) < 0.5:
        positional_mode = '1'
    co2 = []
    for string in strings:
        if string[counter] == positional_mode:
            co2.append(string)
    counter += 1
    return co2_rating(co2, counter)


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
    oxygen = oxygen_rating(strings, 0)
    co2 = co2_rating(strings, 0)
    result = int(oxygen, 2) * int(co2, 2)
    print(result)


if __name__ == '__main__':
    main()
