

def filter1(ge):
    for i in range(len(ge)-1):
        if ge[i] < ge[i+1]:
            continue
        else:
            return False
    return True

def filter2(ge):
    for i in range(len(ge)-1):
        if ge[i] > ge[i+1]:
            continue
        else:
            return False
    return True

def good(ge):
    if filter1(ge) or filter2(ge):
        return True
    else:
        return False


def count_fire(data):
    from itertools import permutations,combinations
    temp = []
    for i in combinations(data,3):
        temp.append(i)
    result = filter(good, temp)
    result = [i for i in result]
    return result


if __name__ == '__main__':
    rating = [2,5,3,4,1]
    all_result = count_fire(rating)
    print(all_result)

'''
53 / 53 个通过测试用例
状态：通过
执行用时：8244 ms
内存消耗：90.6 MB
提交时间：3 分钟之前
'''