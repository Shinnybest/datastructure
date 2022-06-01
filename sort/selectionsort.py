# my code
# 최소값을 항상 제일 왼쪽으로 보내는 것
def selectionsort(lst):
    for i in range(len(lst)-1):
        minimum = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < minimum:
                idx, minimum = j, lst[j]
        if lst[i] != minimum:
            lst[i], lst[idx] = lst[idx], lst[i]
    return lst


selectionsort([2, 5, 6, 7, 8, 9, 1, 3, 4, 10])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]