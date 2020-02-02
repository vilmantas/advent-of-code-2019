

def part_1(start: int, end: int):

    valid_results = []

    for i in range(start, end):
        if all_increasing(i) and has_two_duplicates(i):
            valid_results.append(i)

    print(valid_results)
    print(len(valid_results))
    return valid_results

def part_2(start: int, end: int):
    valid_results = []

    for i in range(start, end):
        if all_increasing(i) and has_exactly_two_duplicates(i):
            valid_results.append(i)

    print(valid_results)
    print(len(valid_results))
    return valid_results

def all_increasing(number: int):

    current = 0
    prev = -1 

    for i in range(6):

        current = int(str(number)[i])

        if current < prev:
            return False

        prev = current

    return True

def has_two_duplicates(number: int):

    current = -1
    prev = -1

    for i in range(6):
        current = int(str(number)[i])

        if prev == current:
            return True

        prev = current

    return False

def has_exactly_two_duplicates(number: int): 

    item = -1
    count = 1
    valid = False

    for i in range(6):
        
        current = int(str(number)[i])

        if current == item:
            count += 1

            if count == 2 and i != 5 and int(str(number)[i + 1]) != current:
                return True

            if count == 2 and i == 5:
                return True
        else:
            item = current
            count = 1
            valid = False

    return valid






def match(num):
    """
    count the recurrence of digits
    -1 if any digits are in the wrong order: filter this out
     2 if any digit appears exactly twice: count these for part 1 and 2
     max recurrence otherwise: count for part 1 if > 2, but filter if 1
    """
    s = str(num)
    for i, c in enumerate(s):
        if i > 0 and s[i-1] > c:
            return -1
    l = list(s)
    counts = set(l.count(c) for c in set(s))
    return 2 if 2 in counts else max(counts)

# digit_counts = list(match(n) for n in range(197487,673251))

# print("Day 04")
# print(f"1. {sum(1 for n in digit_counts if n > 1)}")
# print(f"2. {sum(1 for n in digit_counts if n == 2)}")




if __name__ == "__main__":

    # v1 = part_1(197487, 673251)
    v2 = part_2(197487, 673251)

    # [print(x) for x in v1 if not v2.__contains__(x)]

    # print(v2)

    result = []

    for i in range(197487,673251):
        x = match(i)

        if x == 2:
            result.append(i)

    print(len(result))

    [print(x) for x in v2 if not result.__contains__(x)]

    # print(has_exactly_two_duplicates(466777))

    # print(has_exactly_two_duplicates(123456))

    # print(has_exactly_two_duplicates(123455))

    # print(has_exactly_two_duplicates(123334))

    # print(has_exactly_two_duplicates(666789))
    
    # print(has_exactly_two_duplicates(666689))

    pass