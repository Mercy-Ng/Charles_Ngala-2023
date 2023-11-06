#The MarsRover class is defined with methods to move, 
#rotate left, rotate right, 
#execute commands, 
#and get the current location.
class MarsRover:
    def __init__(self, x, y, direction, boundary_x, boundary_y):
        self.x = x
        self.y = y
        self.direction = direction
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y

    def move(self):
        if self.direction == 'N' and self.y < self.boundary_y:
            self.y += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'E' and self.x < self.boundary_x:
            self.x += 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                self.move()
            elif command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()

    def get_location(self):
        return f"{self.x} {self.y} {self.direction}"


#The MarsRover function takes a list of input lines, 
# where the first line specifies the boundary coordinates, 
# the second line specifies the rover's initial location and direction, 
# and the third line contains the movement commands.
def MarsRover(listInput):
    boundary_x, boundary_y = map(int, listInput[0].split())
    start_x, start_y, start_direction = listInput[1].split()
    commands = listInput[2].strip()

    rover = MarsRover(int(start_x), int(start_y), start_direction, boundary_x, boundary_y)
    rover.execute_commands(commands)
    return rover.get_location()

if __name__ == "__main__":
    listInput = [
        "8 8",
        "1 2 E",
        "MMLMRMMRRMML"
    ]
    final_location = MarsRover(listInput)
    print("Final Rover Location:", final_location)
    
    bounInput = input("Enter the boundary coordinates (e.g., '8 8'): ")
    startingLocationIn = input("Enter the start location and direction (e.g., '1 2 E'): ")
    userCommand = input("Enter the movement commands (e.g., 'MMLMRMMRRMML'): ")

    listInput = [bounInput, startingLocationIn, userCommand]
    final_location = MarsRover(listInput)
    print("Final Rover Location:", final_location)