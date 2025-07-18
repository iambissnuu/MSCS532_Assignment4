class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def change_priority(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                old_priority = self.heap[i].priority
                self.heap[i].priority = new_priority
                if new_priority > old_priority:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                break

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        n = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#test
if __name__ == "__main__":
    pq = PriorityQueue()
    task1 = Task("T1", 4, "08:00", "10:00")
    task2 = Task("T2", 2, "08:10", "09:00")
    task3 = Task("T3", 6, "08:20", "11:00")

    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)

    print("Extracted:", pq.extract_max().task_id)

    pq.change_priority("T2", 7)
    print("Extracted after priority change:", pq.extract_max().task_id)
