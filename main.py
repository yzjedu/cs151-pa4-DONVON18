# Programmers:  Donovan,
# Course:  CS151,
# Due Date: november 21h
# Lab Assignment: PA 04
# Problem Statement: You are creating a program to analyze headlines from the Australian Broadcasting Company (ABC).
# Credits: CS151

# imports module
import os

# Purpose:  reading file
  # Parameters: none
  # Return: file
def read_filename():
    # Prompt user for the filename to read
    name = input("'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'"
                 "What is the name the name of a headline file they would like to analyze? \n"
                 "'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(name):
        print("'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'"
              "That file does not exist. Please try again.")
        name = input("what is the name of a headline file they would like to analyze? \n"
                     "'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'")

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
    # introduces the programs so user knows how to interact
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          'This program is to find how many headlines have a specific word in it\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '\n')
    # gets the word that the user wants to find and initalizes the count variable
    word = input("what word do you want to find? ")
    count = 0

    # adds to the count every time the word is found
    for line in data:
        if word in line:
            count += 1

    # displays the word
    print(f'The word {word} occurs {count} times in total.')

# Purpose: Determine how many headlines have a particular word
  # Parameters: data
  # Return: new file
def lines_with_word(data):
    #introduces the program and explains to user how to interact
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          'This program is to create a file with headlines that have a specific word in it abd save it to a\n'
          'file called words_headlines.txt\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '\n')

    # gets the word the user wants to find
    word = input("what word do you want to find? ")

    # opens and empty list to put every head line that meets the requirements
    headlines = []

    # for every line in the data if the word is in it it ias added to the list
    for line in data:
        if word in line:
            headlines.append(line)

    # Opens a file to put the headline list in
    new_file = open('words_headlines.txt', 'w')

    # writes each element in the headline list
    for line in headlines:
        new_file.write(line)

    #closes the file and tells the user where to find the data
    new_file.close()
    print('Look inside words_headlines.txt')

# Purpose: Determine the average number of characters per headline
  # Parameters: data
  # Return: average number of characters statement
def avg_char(data):
    # initializes the variables
    count = 0
    length = 0

    # gets the length of every line, adds them together, and counts every line
    for line in data:
        length += len(line)
        count += 1
    # divides the length and count to get the average and then displays the average
    average = length / count
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'The average character per headline is: {average}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


# Purpose: Output the longest and shortest headline.
  # Parameters: data
  # Return: longest and shortest statement
def find_longest_shortest_lines(data):
    # sets the longest list to the first line of data
    longest = data[0]

    # compares each lines length to see which one is the longest
    for line in data:
         if len(line) > len(longest):
             longest = line

    # sets the shortest list to the first line of data
    shortest = data[0]

    # compares each lines length to see which one is the shortest
    for line in data:
        if len(line) < len(shortest):
            shortest = line

    # outputs the value
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'The longest headline is: {longest}')
    print(f'The shortest headline is: {shortest}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Purpose: displays the options
  # Parameters:
  # Return: optiop
def option_display():
    #displays the options
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "Please choose an option  from the menu\n"
          "\t A -- To determine how many headlines have a particular word in it, for a single file\n"
          "\t B -- To write headlines containing a specific word to a new file.\n"
          "\t C -- To determine the average number of characters per headline\n"
          "\t D -- To find the longest shortest headline\n"
          "\t E -- To read in a new headline document\n"
          "\t Q -- To quit the program\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "\n")
    #asks for the options until it gets a valid answer
    option = input("What would you like to do? ").upper().strip()
    while option not in ['A', 'B', 'C', 'D', 'E', 'Q']:
        option = input("Invalid answer please try again. ").upper().strip()

    return option

def main():
    #introductions welcome message
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "Welcome to the Headline Analyzer! The purpose is to take a headline file of your choice \n"
          "and analyze it using one of our analysis options.\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    #sets options so that we can enter and leave the loop
    option = 'z'
    #sets filename and puts it into a table
    file_name = read_filename()
    data = file_to_list(file_name)

    # repeats until user quits
    while option != 'Q':
        #displays the options
        option = option_display()

        #paths for each choice
        if option == 'A':
            word_amount(data)
        elif option == 'B':
            lines_with_word(data)
        elif option == 'C':
            avg_char(data)
        elif option == 'D':
            find_longest_shortest_lines(data)
        elif option == 'E':
            filename = read_filename()
            data = file_to_list(file_name)

    #outputs thank you statement
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          'Thank you for using this program thank you!\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

main()



