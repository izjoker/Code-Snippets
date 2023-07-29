def bisearch(lst):
    min_ = 0
    max_ = len(lst)-1
    while min_+1 < max_:
        med = (max_+min_)//2
        if lst[med] <= lst[r]:
            max_ = med
        else:
            min_ = med
    return max_