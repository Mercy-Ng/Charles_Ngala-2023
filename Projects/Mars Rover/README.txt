Mars Rover Program README
Overview
This Python program simulates a Mars rover's navigation system. It allows you to input the zone's boundary, initial rover position, and a list of commands to navigate the rover. The program follows the given specifications to compute the rover's final location.
How to Use the Program
1. Open a terminal or command prompt.
2. Save the program code into a Python file, e.g., “mars_rover.py”.
3. Run the program 
4. The program will prompt you for input in the following format:
•	Enter the zone's boundary as two integers separated by a space (e.g., "8 8").
•	Enter the rover's initial position and direction (e.g., "1 2 E").
•	Enter the list of commands for the rover (e.g., "MMLMRMMRRMML").
5. The program will calculate and display the final position of the rover on the console.

Design Decisions
•	The program uses a “MarsRover” class to encapsulate the rover's functionality. This design choice allows for better organization and readability.
•	The rover's movements and rotations are implemented within the “move”, “turn_right”, and “turn_left” methods of the “MarsRover” class.
•	The program validates boundaries to ensure that the rover stays within the defined zone.
•	The program uses a list of cardinal directions to simplify direction changes.
•	The “main” function handles user input and initiates rover navigation.

Ensuring Code Correctness
•	The code ensures correctness by:
•	Checking boundaries to prevent the rover from moving outside the defined zone.
•	Validating user inputs to ensure they follow the specified format.
•	Handling rotations and movements accurately based on the rover's current direction.
•	Employing modulo operations to manage direction changes cyclically.
•	The program includes minimal error handling for simplicity. You may consider adding more comprehensive error handling if needed.
•	Extensive testing with different inputs can further validate the program's correctness.

Additional Inputs
The program accepts inputs in the format described in the original question. You can run the program with various inputs to simulate different rover missions. Make sure to provide valid boundary coordinates, initial positions, and command sequences to see the rover's final position.
