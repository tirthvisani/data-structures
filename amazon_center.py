class ConveyorBelt:
    def __init__(self):
        self.size = 8
        self.belt = [None] * self.size

    def update_slot(self, slot, product):
        if 0 <= slot < self.size:
            self.belt[slot] = product
            print("Product Updated.")
        else:
            print("Invalid Slot!")

    def check_slot(self, slot):
        if 0 <= slot < self.size:
            if self.belt[slot] is None:
                print("Slot is Empty")
            else:
                print("Product:", self.belt[slot])
        else:
            print("Invalid Slot!")

    def is_full(self):
        if None not in self.belt:
            print("Conveyor Belt is Full")
        else:
            print("Conveyor Belt is NOT Full")

    def display(self):
        print("\nCurrent Conveyor Belt")
        for i in range(self.size):
            print(f"Slot {i} : {self.belt[i]}")

belt = ConveyorBelt()

while True:
    print("\n1.Update Slot")
    print("2.Check Slot")
    print("3.Check Belt Full")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        slot = int(input("Enter Slot Number (0-7): "))
        product = input("Enter Product Name: ")
        belt.update_slot(slot, product)

    elif ch == 2:
        slot = int(input("Enter Slot Number: "))
        belt.check_slot(slot)

    elif ch == 3:
        belt.is_full()

    elif ch == 4:
        belt.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
