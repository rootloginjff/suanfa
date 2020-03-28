import timawrap


def feibonaqian(n):
    if n == 0 or n == 1:
        return 1
    else:
        return feibonaqian(n-1) + feibonaqian(n-2)
# 1 1 2 3 5 8
# 0 1 2 3 4 5
# a = feibonaqian(20)   #2^n
# print(a)

@timawrap.cal_time
def fib1(n):
    a = feibonaqian(n)
    return a



@timawrap.cal_time
def fib2(n):
    li = [1,1]
    for i in range(2,n):
        li.append(li[-1] + li[-2])
        print(li)
    return li[-1]

def fib3(n):
    li = [1,1]
    for i in range(2,n+1):
        li[0] = li[0] + li[1]
        li[1] = li[0] + li[1]

print(fib1(5))
print(fib2(5))
# print(type(fib2(3400)))