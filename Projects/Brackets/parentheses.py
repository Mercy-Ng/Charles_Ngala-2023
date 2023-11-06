
#this is the opening and the closing barckets
listOne = ["[","{","("]
listTwo = ["]","}",")"]

#This is a function that takes an input string txt and uses a stack to check if the expression is balanced
def checkList(txt):
    stack = []
    for i in txt:
        if i in listOne:
            stack.append(i)
        elif i in listTwo:
            pos = listTwo.index(i)
            if ((len(stack) > 0) and
                (listOne[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
while True:
    userInput = input("Enter Expression: ")
    print(userInput, ": ", checkList(userInput))
        