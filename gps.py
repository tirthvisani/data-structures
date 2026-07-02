class GPS:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = "Home"

    def visit(self, place):
        self.back_stack.append(self.current)
        self.current = place
        self.forward_stack.clear()
        print("Current Location:", self.current)

    def back(self):
        if len(self.back_stack) == 0:
            print("Cannot Go Back")
        else:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            print("Current Location:", self.current)

    def forward(self):
        if len(self.forward_stack) == 0:
            print("Cannot Go Forward")
        else:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            print("Current Location:", self.current)

    def show(self):
        print("\nCurrent:", self.current)
        print("Back Stack:", self.back_stack)
        print("Forward Stack:", self.forward_stack)


gps = GPS()

while True:
    print("\n1.Visit Place")
    print("2.Back")
    print("3.Forward")
    print("4.Show Current")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        place = input("Enter Place: ")
        gps.visit(place)

    elif ch == 2:
        gps.back()

    elif ch == 3:
        gps.forward()

    elif ch == 4:
        gps.show()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
