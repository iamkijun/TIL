N = 10
q = [0] * 10
front = 0
rear = 0

rear = (1 + rear) % N           # enqueue(10)
q[rear] = 10

rear = (1 + rear) % N               # enqueue(20)
q[rear] = 20

rear = (1 + rear) % N               # enqueue(30)
q[rear] = 30

front = (1 + front) % N               # dequeue()
print(q[front])

print(q)