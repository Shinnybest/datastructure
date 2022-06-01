def insertionsort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j]<lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    print(lst)
    return lst

insertionsort([2, 5, 6, 7, 8, 9, 1, 3, 4, 10])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]