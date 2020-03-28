import timawrap


@timawrap.cal_time
def bin_search(data,value):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == value:
            return True
        elif data[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False



if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 43, 45]
    result1 = bin_search(l1,43)
    print(result1)
    l2 = list(range(0,900000000,2))
    result2 = bin_search(l2, 0)
    print(result2)