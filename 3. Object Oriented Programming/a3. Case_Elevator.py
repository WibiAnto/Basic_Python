class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        self.current = self.current + 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current <= 0:
            print("Sudah di lantai dasar")
        else:
            self.current = self.current - 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor <= 1:
            print(f"You cant go to floor {floor}")
        else:
            self.current = floor

elevator = Elevator(-1, 10, 0)

elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
print(elevator.current)