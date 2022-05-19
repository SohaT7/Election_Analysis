print("Hello World")


# If Statements:
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


# If-Else Statements:
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


# Nested If-Else Statements:
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# If-elif-else Statements:
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


# Membership Operators:
## in:
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
## not in:
counties = ["Arapahoe","Denver","Jefferson"] 
if "El Paso" not in counties: 
    print("True") else: print("False")


# Logical Operators:
## and:
x = 5 
y = 5
if x == 5 and y == 5:
    print("True") 
else: 
    print("False")
## or:
x = 5 
y = 5
if x == 3 or y == 5:
    print("True")
else: 
    print("False")
## not:
x = 5 
y = 5
if not(x > y):
    print("True") 
else: 
    print("False")


# Logical Operators:
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


# While Loops:
x = 0
while x <= 5:
    print(x)
    x = x + 1


# For Loops:
for county in counties:
    print(county)


# The range() function, to iterate through a list:
for num in range(5):
    print(num)
# The range() fn. works in place of:
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


# Indexing to iterate through a list:
for i in range(len(counties)):
    print(counties[i])


# Iterating through a dictionary:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

## Get the keys of a dictioanry:
for county in counties_dict:
    print(county)
### Or, as follows:
for county in counties_dict.keys():
    print(county)

## Get the values of a dictionary:
for voters in counties_dict.values():
    print(voters)
###, Or, as follows:
for county in counties_dict:
    print(counties_dict[county])
### Or, as follows:
for county in counties_dict:
    print(counties_dict.get(county))

## Get the key-value pairs of a dictionary:
for county, voters in counties_dict.items():
    print(county, voters)


# Iterating through a list of dictionaries:

## Get each dictionary in a list of dictionaries:
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

### Using the range() fn. to iterate over the list of dictionaries and print the counties:
for i in range(len(voting_data)):
      print(voting_data[i]['county'])

## Get the values from a list of dictionaries:
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

### Printing only the county name from each dictionary:
for county_dict in voting_data:
    print(county_dict['county'])


# Printing:
## Converting a string with integer values into a string
## using concatenation with a + sign:
print("Your interest for the year is $" + str(interest)) 
## In place of concatenation can be used formatted or f-strings:
### In the f-string, curly braces are used to add variables or expressions to the f-string.
### With concatenation:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
### With f-strings:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


# Using f-strings with dictionaries:
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
## With concatenation:
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
## With f-strings:
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings:
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


# Format floating-point decimals:

## General formatting of a number in an f-string:
### f'{value:{width}.{precision}}'
### In the format, the width specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.
### The precision indicates the number of decimal places to format the value. For example, to format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format".
### When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.
### f'{value:{width},.{precision}}'

## Let's add a thousands separator to the output for the candidate votes and total votes and then format the percentage of votes to two decimal places. 
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")


# Dependencies:
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
## In the above, the now variable is set equal to datetime.datetime.now(), where:
### (1.) The first datetime is the datetime module, (first doll).
### (2.) The second datetime is the datetime class (second doll).
### (3.) Then we use the datetime attribute, now(), (third doll) on the datetime class, i.e., datetime.now(), to get the current time.

## To reduce the confusion on importing a module with the same name as a class we can use an abbreviated alias dt for the datetime module.
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Opening a file:
## The general format for opening a file is, file_variable = open(filename, mode).
## Let's break down what each component is doing in the general format.
## ## file_variable is the name of the variable that will reference the file object.
## filename is a string specifying the name of the file.
## mode is a string specifying the mode for reading or writing the file object. The possible modes are:
## "r": Open a file to be read.
## "w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
## "x": Open a file for exclusive creation. If the file does not exist, it will not create one.
## "a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
## "+": Open a file for reading and writing.

## The os module allows us to interact with our operating system. We can see all the different attributes and methods that the os module uses by importing the module and typing print(dir(os)) in the Python interpreter.
## >>> import os
## >>> dir(os)
## The join() function joins our file path components together when they are provided as separate strings; then, it returns a direct path with the appropriate operating system separator, forward slash for macOS or backward slash for Windows.


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes.


# -----------------------------------------------------------------------------------------------

# Opening a file when a direct path is given:

# Assign a variable for the file to load and the path:
## file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file:
## election_data = open(file_to_load, 'r')
# To do: perform analysis
# Close the file:
## election_data.close()

# Or, alternatively to open() and close(), you can use with() to open a file:

## with open(file_to_load) as election_data:
     ## To do: perform analysis.
     ## print(election_data)


# -----------------------------------------------------------------------------------------------


# Opening a file when a direct path is not given:

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file using with():
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# -----------------------------------------------------------------------------------------------

# Write to a file, using the open() and close() functions:

# Create a filename variable to a direct or indirect path to the file:
# (Create a folder called 'analysis' and then can run the following.)
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()


# -----------------------------------------------------------------------------------------------

# Write to a file, using the with() function instead:

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")


# ----------------------------------------------------------------------------------------------

# Writing county names to a file, using the with() function:

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file separately:
     ## txt_file.write("Arapahoe, ")
     ## txt_file.write("Denver, ")
     ## txt_file.write("Jefferson")
     # Or, write them all in one line:
     # Write three counties to the file.
     ## txt_file.write("Arapahoe, Denver, Jefferson")
     # To add each to a new line, use the newline escape sequence (\n):
     txt_file.write("Arapahoe\nDenver\nJefferson")


# ----------------------------------------------------------------------------------------------




