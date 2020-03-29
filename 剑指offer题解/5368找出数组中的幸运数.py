def find_lunckily_number(data):
    length = len(data)
    count = [0 for i in range(max(data) + 1)]
    luck = []
    for d in range(0,length):
        count[data[d]] += 1
    for d in range(0,len(count)):
        if d == count[d]:
            luck.append(d)
    if luck:
        if count[0] == 0 and len(luck) == 1:
            return -1
        return max(luck)
    else:
        return -1


if __name__ == '__main__':
    data1 = [2,2,3,4]
    data2 = [1,2,2,3,3,3]
    data3 = [2,2,2,3,3]
    data4 = [5]
    data5 = [7,7,7,7,7,7,7]

    result = find_lunckily_number(data5)
    print(result)

    '''
    100 / 100 个通过测试用例
    状态：通过
    执行用时：56 ms
    内存消耗：13.7 MB
    提交时间：0 分钟之前
    '''