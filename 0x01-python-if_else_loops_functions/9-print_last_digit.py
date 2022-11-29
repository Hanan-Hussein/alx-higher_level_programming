#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new_number = abs(number)
        answer = -abs(new_number % 10)
        return answer
    else:
        return number % 10

