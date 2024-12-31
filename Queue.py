from queue import Queue

q = Queue()

for _ in range(int(input())):
    a = input()
    if a[0] == 'E':  # For enqueue operation
        _, cc = a.split()
        c = int(cc)
        q.put(c)
    else:  # For dequeue operation
        if q.qsize() == 0:  # Check if the queue is empty
            print('Empty')
        else:
            print(q.get())
