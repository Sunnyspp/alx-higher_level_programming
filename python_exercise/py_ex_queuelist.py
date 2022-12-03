Topic = '''Using Lists as Queues
To implement a queue, use collections.deque which was designed 
to have fast appends and pops from both ends. For example:
For example:
'''
queue = ["Eric", "John", "Michael"]
print(queue)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)
print(queue.popleft())  # The first to arrive now leaves
print(queue.popleft()) # The second to arrive now leaves
print(queue)   # The resultant list

queue = ['Apple', 'Orange', 'Banana', 'Grape']
print(queue)
from collections import deque
queue = deque(['Apple', 'Orange', 'Banana', 'Grape'])
queue.append("Pawpaw")  # pawpaw arrived
queue.append("Strawberry")  # strawberry arrived
queue.append("Lemon")  # lemon arrived
print(queue)  # prints the new queue after their arrival
print(queue.popleft())
print(queue.popleft())
print(queue)  # prints the new queue after they left
