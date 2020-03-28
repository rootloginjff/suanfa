import queue
from collections import deque
# a = queue.SimpleQueue()
# a.put(1)
# a.put(2)
# a.put(4)
# print(a.get())
# print(a.get())
# print(a.get())

#双向队列
#读取3个以后，读取第四个，第一个就会被顶出去
q = deque(open('text.txt','r',encoding='utf-8'),3)
print(list(q))

