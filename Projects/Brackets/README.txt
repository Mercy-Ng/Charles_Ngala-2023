Program Description
This program is designed to check whether an input string with different types of brackets (e.g., `[`, `{`, `(`) and their corresponding closing brackets (e.g., `]`, `}`, `)`) is balanced. A balanced string has matching opening and closing brackets, with no nesting issues.
How to Use
1. Run the program, and it will prompt you to enter an expression containing brackets.
2. Input your expression and press Enter.
3. The program will analyze the input and print whether the expression is balanced or unbalanced.
Design Decisions
•	The program uses two lists, `listOne` and `listTwo`, to define the opening and closing brackets, respectively.
•	It employs a stack to keep track of the opening brackets encountered in the input string.
•	As the program reads each character in the input string, it checks if it is an opening or closing bracket and whether it is balanced or unbalanced.
Ensuring Code Correctness
The code ensures correctness through the following mechanisms:
1.	It uses a stack to keep track of opening brackets, ensuring that they are matched with the correct closing brackets.
2.	It checks if the stack is empty after processing the entire input string to ensure that all brackets are balanced.

