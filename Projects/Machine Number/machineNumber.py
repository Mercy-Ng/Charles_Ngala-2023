
#function to reverse the number
def reverse_number(number):
  reversed_number = 0
  while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number //= 10
  return reversed_number

#function for calculating the sum of the digits
def sum_of_digits(number):
  sum_of_digits = 0
  while number > 0:
    remainder = number % 10
    sum_of_digits += remainder
    number //= 10
  return sum_of_digits

#function for generating a new nuumber by adding 1 to the digits
def add_one_to_digits(number):
  new_number = 0
  while number > 0:
    remainder = number % 10
    new_number = (new_number * 10) + (remainder + 1)
    number //= 10
  return new_number


if __name__ == '__main__':
  input_number = int(input('Enter a five-digit number: '))  # Get the input number from the user.
  reversed_number = reverse_number(input_number) # Reverse the number.
  sum_of_digits = sum_of_digits(input_number)   # Calculate the sum of the digits of the number.
  new_number = add_one_to_digits(input_number)   # Generate a new number by adding one to each of the digits.

  # Print the results.
  print('The reversed number is:', reversed_number)
  print('The sum of the digits is:', sum_of_digits)
  print('The new number is:', new_number)
