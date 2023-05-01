#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!" 
        

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def calculator(operation, num1, num2):
    # your code here
    def add(a,b): return a+b
    def subtract(a,b): return a-b
    def multiply(a,b): return a*b
    def divide(a,b): return a/b

    calc_obj = {
        "+": add(num1, num2),
        "-": subtract(num1, num2),
        "*": multiply(num1, num2),
        "/": divide(num1, num2)
    }
    result = calc_obj.get(operation)
    # ipdb.set_trace()
    if(result or result == 0):
        return result
    else:
        print("Invalid operation!")
