# Description: Solution for Advent of Code - Day 1: Chronal Calibration - Part 1
import re

file_path = './input-day-1.txt'

def sum_calibration_values(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            #extract the first and last digit from each line
            digits = [char for char in line if char.isdigit()]
            #convert the list of strings to a list of ints
            if digits:
                first_digit = digits[0]
                last_digit = digits[-1]
                #combine them to form a two-digit number
                calibration_value = int(first_digit + last_digit)
                #add to the total sum
                total += calibration_value
    return total

result_1 = sum_calibration_values(file_path)
print(f"The sum of all calibration values is {result_1} -- PART 1")

# Part 2
def sum_calibration_values(lines):
    total = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        if digits:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])
            total += first_digit * 10 + last_digit
    return total

def find_spelled_out_digits(line, word_to_digit):
    digits = []
    i = 0
    while i < len(line):
        found = False
        for word, digit in word_to_digit.items():
            if line[i:i+len(word)] == word:
                digits.append(digit)
                i += len(word) - 1
                found = True
                break
        if not found and line[i].isdigit():
            digits.append(int(line[i]))
        i += 1
    return digits

def sum_calibration_values_v2(lines):
    word_to_digit = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    total = 0
    for line in lines:
        digits = find_spelled_out_digits(line, word_to_digit)
        if digits:
            total += digits[0] * 10 + digits[-1]
    return total

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# File path to your input data
file_path = "./input-day-1.txt"

# Reading from the file for Part One
lines_part_one = read_file(file_path)
print("Sum for Part One:", sum_calibration_values(lines_part_one))

# Reading from the file for Part Two
lines_part_two = read_file(file_path)
print("Sum for Part Two:", sum_calibration_values_v2(lines_part_two))