# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

### Purpose: reading file 
    ### Name: read_file_to_list
    ### Parameters: file
    ### Return: table 
    ### Algorithm: 
1. create an empty table
2. try
   1. open the file for reading
   2. for every line in the file
      1. the row is split by every ','
      2. typecast row index 2 to an int
      3. typecast row index 4 to an int
      4. append the table
   3. except if the file isn't found
      1. output the file doesn't exist
3. return the table


### Purpose: reading file to lists
    ### Name: file_to_list
    ### Parameters: file name
    ### Return: data
    ### Algorithm:
   1. open file
   2. readlines in file and set to data
   3. close the file
   4. return data


### Purpose: Determine how many headlines have a particular word in it, for a single file
    ### Name: word_amount
    ### Parameters: file name
    ### Return: data
    ### Algorithm:
User gets to choose the name of the word and the new file .
1. print purpose
2. prompt for word
3. count = 0
3. For every line in the data
   1. if the word is in the line
      1. count += 1


### Purpose: Write headlines containing a specific word to a new file.
    ### Name: lines_with_word
    ### Parameters: data
    ### Return: new file with a specific word
    ### Algorithm:
1. print purpose
2. prompt for word
3. open the empty list headlines
4. for every line in data
   1. if the word is in the line
   2. add it to the headlines list
5. open a new file for writing 
6. for every line in headlines 
   1. write it into the new file
7. close the new file 



### Purpose: Determine the average number of characters per headline
    ### Name: avg_char
    ### Parameters: data
    ### Return: the average number of character
    ### Algorithm:
1. count is 0
2. length is 0
3. for every line in data
   1. length += the character length of the line
   2. count += 1
4. average = length / count
5. print average statement


### Purpose: Output the longest and shortest headline.
    ### Name: file_to_list
    ### Parameters: file name
    ### Return: data
    ### Algorithm:
1. longest is data[0]
2. for every line in data 
   1. if the length of the line is longer than len(longest)
      1. longest is line
3. shortest = data[0]
4. for every line in data
   1. if length of the line is shorter than len(shortest)
      1. shortest is line
5. print longest shortest statement


### Purpose: option display
    ### Name: display
    ### Parameters: 
    ### Return: option
    ### Algorithm:
1. Introduce the options and how to choose them and then prompt the user to choose
2. takes the file name and store it in the


### Purpose: Main
    ### Name: Main
    ### Parameters: 
    ### Return: 
    ### Algorithm:
1. introduce code
2. Option is z
3. while option is not E
   1. prompt for option
If the user chooses this option, it overwrites the data you had been storing
(e.g. old file is no longer stored in program after new file is read in)
The user gets to keep choosing what they want to do until they choose to quit.