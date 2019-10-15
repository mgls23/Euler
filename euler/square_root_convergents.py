def square_root_2(number):
    count = 0
    small, big = 0, 1
    for i in range(number):
        small, big = big, big * 2 + small
        if len(str(small + big)) > len(str(big)):
            count += 1

    return count
