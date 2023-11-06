Number Guessing Game
This is a simple Python program that lets you play a number guessing game with the computer. You have to guess a number between 1 and 10, and the computer will randomly generate a number. The program will give you feedback on your guesses until you guess the correct number.

How to Use

1. Make sure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Open the terminal or command prompt and navigate to the directory where the code is located.
4. Run the Python script 
5. The program will prompt you to enter a number between 1 and 10.
6. You will receive feedback on your guess. The program will tell you if your guess is too high or too low compared to the computer-generated number.
7. Keep guessing until you guess the correct number. Once you do, the program will congratulate you.
8. You can play the game as many times as you like by restarting the program.

Functions
•	`generated_num()`: Generates a random number between 1 and 10 for the computer.
•	`different_num(userNum, compNum)`: Calculates the difference between the user's guess and the computer-generated number.
•	`compareNumbers(userNum, compNum)`: Compares the user's guess to the computer-generated number and provides feedback on the guess.
•	`checkValid(userNum)`: Checks if the user's input is a valid number. If not, it will prompt the user to enter a valid number.
