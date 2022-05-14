# my code
def bubblesort(lst):
    for x in range(len(lst)-1, 0, -1):
        for i in range(0, x):
            if lst[i] > lst[i+1]:        
                lst[i], lst[i+1] = lst[i+1], lst[i]
    
    return lst

# book code
def bubblesort_b(lst):
    index_cnt = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(index_cnt):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False
        index_cnt -= 1
    
    return lst