import queue
a = queue.SimpleQueue()
a.put(1)
a.put(2)
a.put(4)
print(a.get())
print(a.get())
print(a.get())
