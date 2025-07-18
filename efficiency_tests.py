import time
import random
from heapsort import heapsort
from priority_queue import Task, PriorityQueue

print("\nHeapsort Efficiency Test")

data1 = [random.randint(1, 10000) for _ in range(10000)]
start = time.time()
heapsort(data1)
end = time.time()
print("Heapsort (10,000 items):", round(end - start, 4), "seconds")

print("\nBuilt-in Sort Comparison")

data2 = [random.randint(1, 10000) for _ in range(10000)]
start = time.time()
data2.sort()
end = time.time()
print("Built-in sort (10,000 items):", round(end - start, 4), "seconds")

print("\nPriority Queue Insert & Extract Test")

pq = PriorityQueue()

start = time.time()
for i in range(10000):
    pq.insert(Task(f"T{i}", random.randint(1, 100), "00:00", "01:00"))
end = time.time()
print("Priority Queue - Insert 10,000 tasks:", round(end - start, 4), "seconds")

start = time.time()
for _ in range(10000):
    pq.extract_max()
end = time.time()
print("Priority Queue - Extract 10,000 tasks:", round(end - start, 4), "seconds")
