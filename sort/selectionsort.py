# my code
def selectionsort(lst):
    for i in range(len(lst)-1):
        min_num = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < min_num:
                index_v, min_num = j, lst[j]
        if lst[i] != min_num:
            lst[i], lst[index_v] = lst[i], min_num
    return lst