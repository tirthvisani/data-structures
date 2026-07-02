class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, vehicle):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print("Vehicle Added")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Vehicle Passed:", self.queue[self.front])

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue Empty")
            return

        print("\nVehicles in Queue:")

        i = self.front
        while True:
            print(self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % self.size


cq = CircularQueue()

while True:
    print("\n1.Arrival")
    print("2.Vehicle Passed")
    print("3.Display Queue")
    print("4.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        vehicle = input("Enter Vehicle Number: ")
        cq.enqueue(vehicle)

    elif ch == 2:
        cq.dequeue()

    elif ch == 3:
        cq.display()

    elif ch == 4:
        break

    else:
        print("Invalid Choice")
