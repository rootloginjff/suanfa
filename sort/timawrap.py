import time


def cal_time(func):
    def wrapper(*args,**kwags):
        t1 = time.time()
        result = func(*args,**kwags)
        t2 = time.time()
        print("%s running time : %s secs." %(func.__name__,t2-t1))
        return result
    return wrapper