'''
File:  cosc-1010-fall-fuctions-FourX11gd

Name:  John Levengood

Requirements:  Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.
  The user is asked to input two numbers. These numbers will be passed as arguments into one of the subroutines.
  The user is asked to input 1 to add, 2 to subtract etc.
  If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
  Output the returned result as part of a sentence.

Variables:
  Inptus: Menu Inputes and Numerical Inputs
  Calculated:  Mathematical statements
  
Outputs:  Mathemeatcal statements, dynamic sentances

Key calculations:  Mathematical satements, Menu selections

Key design considerations:
  Ease of reading (formating)

Test data:
  I accidentally deleted the first program, but this one will have the same testing, multiple numbers to check the math
  Numbers to check menuing, including indicating a incorrect number and asking again.  While testing I did some
  fomating to make easier to read the actual program
'''
#setting constants and defining functions
operation = ''
exit = '1'
menu = '0'

def add(a, b):
    global operation
    operation = 'added'

    return (a + b)

def subtract(c, d):
    global operation
    operation = 'subtracted'

    return (c - d)

def multiply(e, f):
    global operation
    operation = 'multiplied'

    return(e * f)

def divide(g, h):
    global operation
    operation = 'divided'

    return(g / h)

#begin main part of program, ask for numbers and menu choices

while exit != '0':
    print('\nEnter your choice of numbers. Remember position matters for subtraction and division')
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('\nEnter number to select mathmatical function\n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division')

    while menu != '1' or '2' or '3' or '4':
        menu = input('\nSelect mathmatical function: ')
        if menu == '1':
            math = add(num1, num2)
            break

        elif menu == '2':
            math = subtract(num1, num2)
            break

        elif menu == '3':
            math = multiply(num1, num2)
            break

        elif menu == '4':
            math = divide(num1, num2)
            #Couldn't remember a way to keep decimal places short, when online to find the round funciton
            math = round(math, 2)
            break

        else:
            print('\nYou have entered a incorrect menu option, please try again')
    
    print(f'\nYour first number {num1} was {operation} by your second number {num2} for a total of {math}!')

    exit = input('\nEnter 0 to exit, anything else to try again: ')