from collections import deque

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
print(queue)

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.pop(0)
# print(queue)