import timawrap
import random


@timawrap.cal_time
def maopao_sort(data):
    length = len(data)
    for i in range(length-1):
        exchange = False
        for j in range(length-1-i):
            if data[j] > data[j+1]:
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                exchange = True

        if not exchange:
            break

def get_min_pos(data):
    min_pos = 0
    for i in range(1,len(data)):
        if data[i] < data[min_pos]:
            min_pos = i
    return min_pos


@timawrap.cal_time
def select_sort(data):
    length = len(data)
    for i in range(length-1):
        min_pos = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_pos]:
                min_pos = j
        data[i],data[min_pos] = data[min_pos],data[i]


@timawrap.cal_time
def select_sort2(data):
    length = len(data)
    for i in range(length - 1):
        min_pos = i
        for j in range(i + 1,length):
            if data[min_pos] > data[j]:
                min_pos = j
        data[min_pos],data[i] = data[i],data[min_pos]

@timawrap.cal_time
def insert_sort(data):
    length = len(data)
    for i in range(1,length):
        temp = data[i]
        j = i -1
        while j >= 0 and data[j] > temp:
            data[j+1] = data[j]
            j-=1
        data[j+1] = temp



def _quick_sort1(data):
    length = len(data)
    if length < 2:
        return data
    temp = data[0]
    left  = [data[i] for i in range(1,length) if data[i] < temp]
    right = [data[i] for i in range(1,length) if data[i] > temp]
    left = _quick_sort1(left)
    right = _quick_sort1(right)
    return left + [temp] + right

@timawrap.cal_time
def quick_sort1(data):
    return _quick_sort1(data)



def patition(data,left,right):
    temp = data[left]
    while left < right:

        while left < right and temp <= data[right]:
            right -= 1
        data[left] = data[right]
        while left < right and temp >= data[left]:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return left

def random_patiton(data,left,right):
    i = random.randint(left,right)
    data[left],data[i] = data[i],data[left]
    return patition(data, left, right)


def _quick_sort2(data,left,right):
    if left < right:
        mid = random_patiton(data,left,right)
        _quick_sort2(data,left,mid-1)
        _quick_sort2(data,mid+1,right)

@timawrap.cal_time
def quick_sort2(data):
    _quick_sort2(data,0,len(data)-1)

def sift(data,low,high):
    #data 表示树，low表示树根，high表示树最后一个节点的位置
    temp = data[low]
    i = low
    j = 2 * i + 1
    #i表示空位，j表示2个孩子
    while j <= high:
        if j + 1 <= high and data[j+1] > data[j]:  #如果又孩子存在且比左孩子大
            j += 1
        if data[j] > temp:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = temp
    

#(n-1)//2  n-1  n//2-1

def heap_sort(data):
    n = len(data)
    for low in range(n//2 -1,-1,-1):
        sift(data,low,n-1)
    print(data)
    for high in range(n-1,-1,-1):
        data[0],data[high] = data[high],data[0]
        sift(data,0,high-1)

@timawrap.cal_time
def merge_sort(data,low,mid,high):
    i = low
    j = mid+1
    data_temp = []
    while i<=mid and j<high:
        try:
            if data[i] <= data[j]:
                data_temp.append(data[i])
                i +=1
            else:
                data_temp.append(data[j])
                j+=1
        except:
            print(i,j)

    if i > mid:
        data_temp += data[j:]
    if j >= high:
        data_temp += data[i:mid+1]
    for i in range(low,high+1):
        data[i] = data_temp[i-low]

def insert_sort_gap(data,d):
    length = len(data)
    for i in range(d,length):
        temp = data[i]
        j = i -d
        while j >= 0 and data[j] > temp:
            data[j+d] = data[j]
            j-=d
        data[j+d] = temp
@timawrap.cal_time
def shell_sort(data):
    d = len(data) //2
    while d > 0 :
        #do sonmething
        insert_sort_gap(data,d)
        d = d // 2
@timawrap.cal_time
def count_sort(data,max_num=100):
    count_data = [0 for i in range(max_num + 1)]
    for i in data:
        count_data[i] +=1
    data.clear()
    for i in range(0,len(count_data)):
        if count_data[i] > 0:
            data += count_data[i] * [i]

@timawrap.cal_time
def radix_sort(data):
    max_num = max(data)
    i = 0
    while 10 ** i <= max_num:
        buckets = [[] for i in range(10)]
        for val in data:
            digit = val // (10 ** i) % 10
            buckets[digit].append(val)
        data.clear()
        for bucket in buckets:
            for val in bucket:
                data.append(val)
        i += 1

if __name__ == "__main__":
    l10 = list(random.randint(0,99) for i in range(100000))
    random.shuffle(l10)
    radix_sort(l10)
    print(l10)
    
    l9 = [2,2,2,2,2,2,34,2,4,5,6]
    random.shuffle(l9)
    count_sort(l9,100)
    print(l9)

    # l3 = list(range(0,10000))
    # random.shuffle(l3)
    # result = quick_sort1(l3)
    # print(result)
    #
    # l4 = list(range(0, 10000))
    # random.shuffle(l4)
    # insert_sort(l4)
    # print(l4)

    # l5 = list(range(0, 10000))
    # random.shuffle(l5)
    # quick_sort2(l5)
    # print(l5)
    #
    # l6 = list(range(0, 10))
    # random.shuffle(l6)
    # heap_sort(l6)
    # print(l6)

    # l7 = [2,4,6,8,9,1,2,3,4,5,6,7,8]
    # result = merge_sort(l7,0,4,len(l7))
    # print(result)

    # l8 = list(range(0, 10))
    # random.shuffle(l8)
    # shell_sort(l8)
    # print(l8)



























