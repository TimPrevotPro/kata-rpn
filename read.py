import math

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def addition(stack):
    stack.insert(0,stack.pop(0)+stack.pop(0))

def substraction(stack):
    stack.insert(0,stack.pop(0)-stack.pop(0))

def multiplication(stack):
    stack.insert(0,stack.pop(0)*stack.pop(0))

def square(stack):
    stack[0] = math.sqrt(stack[0])

def read(input):
    sp = input.split(' ')
    while(sp != []):
        value = sp.pop(0)
        print(value)
        if(is_number(value)):
            stack.insert(0,float(value))
        else:
            if(len(stack) >= 2):
                if(value == '+'):
                    addition(stack)
                elif (value == '-'):
                    substraction(stack)
                elif (value == '*'):
                    multiplication(stack)
            if(len(stack) >= 1):
                if (value == 'sqrt'):
                    square(stack)
    print(stack)
    
stack = []
    
read('8 7 4 5 + - * sqrt')