def indexes_of_inverse(array: list[int]):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == -array[j]:
                return i, j
    return 0
