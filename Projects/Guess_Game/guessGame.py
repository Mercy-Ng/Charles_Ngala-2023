import random #to generated random numbers

#this is a function to generate a rundom number 
def generated_num():
    comp_num = random.randint(1,10)
    return comp_num

#calculating the different between the two numbers
def different_num(userNum, compNum):
    diffNum = userNum - compNum
    return diffNum

#check if the user guessed correctly or not
def compareNumbers(userNum, compNum):
    if userNum == compNum:
        print("Congratulations! You guessed right.")
        #compNum = 0
        #return compNum
    elif userNum < compNum:
        print("The number is too low")
    if userNum > compNum:
        print("The number is too high")

#this fucntion will check if the user entered a valid number 
def checkValid(userNum): 
            if not userNum.isdigit():
                return ("Invalid number: Please enter a number: ")
            else: return ""

if __name__ == "__main__":
   generatedNumber = generated_num() #8 
   while True:
        userInputNumber = input("Enter a number between 1 and 10: ")
        
        
        errorMessage = checkValid(userInputNumber)
        print(errorMessage)
        userInputNumber = int(userInputNumber)
        
        differntNumber = different_num(userInputNumber, generatedNumber)
        compareNumbers(userInputNumber, generatedNumber)