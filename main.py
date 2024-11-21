# Programmers:  Donovan,
# Course:  CS151,
# Due Date: november 21h
# Lab Assignment: PA 04
# Problem Statement: You are creating a program to analyze headlines from the Australian Broadcasting Company (ABC).
# Data In:
# Data Out:
# Credits:

import os

# Purpose:  reading file
  # Parameters: none
  # Return: file
def read_filename():
    # Prompt user for the filename to read
    name = input("What is the name the name of a headline file they would like to analyze? ")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(name):
        print("That file does not exist. Please try again.")
        name = input("what is the name of a headline file they would like to analyze? ")

    # Return the valid filename
    return name


# Purpose:  reading file to list
  # Parameters: file name
  # Return: data
def file_to_list(file_name):

    # Open the file
    file_data = open(file_name, 'r')

    # Read all lines from the file and store them as a list of strings in a list called data
    data = file_data.readlines()

    # Close the file
    file_data.close()

    # Return the list of lines from the file
    return data

# Purpose: Determine how many headlines have a particular word
  # Parameters: data
  # Return: word occurance statement
def word_amount(data):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          'This program is to find how many headlines have a specific word in it\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '\n')
    word = input("what word do you want to find? ")
    count = 0
    for line in data:
        if word in line:
            count += 1

    print(f'The word {word} occurs {count} times in total.')

# Purpose: Determine how many headlines have a particular word
  # Parameters: data
  # Return: new file
def lines_with_word(data):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          'This program is to create a file with headlines that have a specific word in it\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '\n')
    word = input("what word do you want to find? ")
    headlines = []
    for line in data:
        if word in line:
            headlines.append(line)

    new_file = open('words_headlines.txt', 'w')
    for line in headlines:
        new_file.write(line)

    new_file.close()

# Purpose: Determine the average number of characters per headline
  # Parameters: data
  # Return: average number of characters statement
def avg_char(data):
    count = 0
    length = 0
    for line in data:
        length += len(line)
        count += 1
    average = length / count
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'The average character per headline is: {average}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


# Purpose: Output the longest and shortest headline.
  # Parameters: data
  # Return: longest and shortest statement
def find_longest_shortest_lines(data):
    longest = data[0]
    for line in data:
         if len(line) > len(longest):
             longest = line
    shortest = data[0]
    for line in data:
        if len(line) < len(shortest):
            shortest = line
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'The longest headline is: {longest}')
    print(f'The shortest headline is: {shortest}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Purpose: Output the longest and shortest headline.
  # Parameters: data
  # Return: longest and shortest statement

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "Welcome to the Headline Analyzer! The purpose is to take a headline file of your choice \n"
          "and analyze it using one of our analysis options.\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "\n")
    file_name = read_filename()
    data = file_to_list(file_name)
    find_longest_shortest_lines(data)


main()



