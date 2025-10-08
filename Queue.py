queue = []
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)
print("Removed:", queue.pop(0))
print("Queue after removing one element:", queue)
print("Front element:", queue[0])
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
