from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)
queue.popleft()