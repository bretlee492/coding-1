students = ['Bretlee', 'Harley', 'Jaden']
print(students)
for student in students: 
    print("Hello, " + student.title() + "!" ) 
print(students)
#dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
#dog = dogs[0]
#print= (dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
print(dogs)
dog = dogs[0]
print(dog)
dog = dogs[1]
print(dog)
dog = dogs[-1]
print(dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
dog = dogs[-2]
print(dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
dog = dogs[-3]
print(dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
for dog in dogs:
    print(dog)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
for dog in dogs:
    print('I like ' + dog + "s.")
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
for dog in dogs:
    print('I like' +dog +"s.")
    print('No, i really like ' + dog +'s!\n')
print("\nThat's just how i feel about dogs.")
print(dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + " Dog: " + dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("Place: " + place + " Dog: " + dog.title())
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil'] 
for dog in dogs:
    print(dogs)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
for dog in dogs:
    print('I like ' + dog + "s.")
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
dogs[0] = 'German shorthaired pointer'
print(dogs)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
print(dogs.index('Labrador retreiver'))
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
print(dogs.index('Labrador retreiver'))
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
print('Labrador retreiver' in dogs)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
dogs.append('Labrador retreive')
for dog in dogs:
    print(dog.title() + "s are cool.")
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaneil']
dogs.insert(1, 'German shorthaired pointer')
print(dogs)
# Create an empty list to hold our users.
usernames = []
# Add some users.
usernames.append('Bretlee')
usernames.append('Harley')
usernames.append('Jaden')
# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')
# Create an empty list to hold our users.
usernames = []

# Add some users.
usernames.append('Bretlee')
usernames.append('Harley')
usernames.append('Jaden')

# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')

# Recognize our first user, and welcome our newest user.
print("\nThank you for being our very first user, " + usernames[0].title() + '!')
print("And a warm welcome to our newest user, " + usernames[-1].title() + '!')
students = ['Bretlee', 'Harley', 'Jaden']

# Put students in alphabetical order.
students.sort()

# Display the list in its current order.
print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())

#Put students in reverse alphabetical order.
students.sort(reverse=True)

# Display the list in its current order.
print("\nOur students are now in reverse alphabetical order.")
for student in students:
    print(student.title())
students = ['Bretlee', 'Harley', 'Jaden']

# Display students in alphabetical order, but keep the original order.
print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())

# Display students in reverse alphabetical order, but keep the original order.
print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())

print("\nHere is the list in its original order:")
# Show that the list is still in its original order.
for student in students:
    print(student.title())
students = ['Bretlee', 'Harley', 'Jaden']
students.reverse()
print(students)
numbers = [1, 3, 4, 2]

# sort() puts numbers in increasing order.
numbers.sort()
print(numbers)

# sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)
numbers = [1, 3, 4, 2]

# sorted() preserves the original order of the list:
print(sorted(numbers))
print(numbers)
numbers = [1, 3, 4, 2]

# The reverse() function also works for numerical lists.
numbers.reverse()
print(numbers)
usernames = ['Bretlee', 'Harley', 'Jaden']
user_count = len(usernames)
print(user_count)
# Create an empty list to hold our users.
usernames = []
# Add some users, and report on how many users we have.
usernames.append('Bretlee')
user_count = len(usernames)
print("We have " + str(user_count) + " user!")
usernames.append('Harley')
usernames.append('Jaden')
user_count = len(usernames)
print("We have " + str(user_count) + " users!")
usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)
print("This will work: " + str(user_count))
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
# Remove the first dog from the list.
del dogs[0]
print(dogs)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
# Remove German shorthaired pointer dog from the list.
dogs.remove('German shorthaired pointer')
print(dogs)
letters = ['a', 'b', 'c', 'a', 'b', 'c']
# Remove the letter a from the list.
letters.remove('a')
print(letters)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
last_dog = dogs.pop()
print(last_dog)
print(dogs)
dogs = ['German shorthaired pointer', 'Labrador retreiver', 'English cockerspaniel']
first_dog = dogs.pop(0)
print(first_dog)
print(dogs)
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Grab the first three users in the list.
first_batch = usernames[0:3]
for user in first_batch:
    print(user.title())
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Grab the first three users in the list.
first_batch = usernames[:3]
for user in first_batch:
    print(user.title())
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Grab the first three users in the list.
first_batch = usernames[0:3]
# The original list is unaffected.
for user in usernames:
    print(user.title())
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Grab a batch from the middle of the list.
middle_batch = usernames[1:4]
for user in middle_batch:
    print(user.title())
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Grab all users from the third to the end.
end_batch = usernames[2:]
for user in end_batch:
    print(user.title())
usernames = ['Bretlee', 'Harley', 'Jaden', 'Alex', 'Caleb']
# Make a copy of the list.
copied_usernames = usernames[:]
print("The full copied list:\n\t", copied_usernames)
# Remove the first two users from the copied list.
del copied_usernames[0]
del copied_usernames[0]
print("\nTwo users removed from copied list:\n\t", copied_usernames)
# The original list is unaffected.
print("\nThe original list:\n\t", usernames)
# Print out the first ten numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
# Print the first ten numbers.
for number in range(1,11):
    print(number)
# Print the first ten odd numbers.
for number in range(1,21,2):
    print(number)
# Create a list of the first ten numbers.
numbers = list(range(1,11))
print(numbers)
# Store the first million numbers in a list.
numbers = list(range(1,1000001))
# Show the length of the list:
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")
# Show the last ten numbers:
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)
ages = [23, 16, 14, 28, 19, 11, 38]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + " years worth of life experience.")
# Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []
# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    new_square = number**2
    squares.append(new_square)
# Show that our list is correct.
for square in squares:
    print(square)
# Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []
# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    squares.append(number**2) 
# Show that our list is correct.
for square in squares:
    print(square)
# Store the first ten square numbers in a list.
squares = [number**2 for number in range(1,11)]
# Show that our list is correct.
for square in squares:
    print(square)
# Make an empty list that will hold the even numbers.
evens = []
# Loop through the numbers 1-10, double each one, and add it to our list.
for number in range(1,11):
    evens.append(number*2)
# Show that our list is correct:
for even in evens:
    print(even)
# Make a list of the first ten even numbers.
evens = [number*2 for number in range(1,11)]
for even in evens:
    print(even)
# Consider some students.
students = ['Bretlee', 'Harley', 'Jaden']
# Let's turn them into great students.
great_students = []
for student in students:
    great_students.append(student.title() + " the great!")
# Let's greet each great student.
for great_student in great_students:
    print("Hello, " + great_student)
# Consider some students.
students = ['Bretlee', 'Harley', 'Jaden']
# Let's turn them into great students.
great_students = [student.title() + " the great!" for student in students]
# Let's greet each great student.
for great_student in great_students:
    print("Hello, " + great_student)
message = "Hello!"
for letter in message:
    print(letter)
message = "Hello world!"
message_list = list(message)
print(message_list)
message = "Hello World!"
first_char = message[0]
last_char = message[-1]
print(first_char, last_char)
message = "Hello World!"
first_three = message[:3]
last_three = message[-3:]
print(first_three, last_three)
message = "I like cats and dogs."
dog_present = 'dog' in message
print(dog_present)
message = "I like cats and dogs."
dog_index = message.find('dog')
print(dog_index)
message = "I like cats and dogs, but I'd much rather own a dog."
dog_index = message.find('dog')
print(dog_index)
message = "I like cats and dogs, but I'd much rather own a dog."
last_dog_index = message.rfind('dog')
print(last_dog_index)
message = "I like cats and dogs, but I'd much rather own a dog."
message = message.replace('dog', 'snake')
print(message)
message = "I like cats and dogs, but I'd much rather own a dog."
number_dogs = message.count('dog')
print(number_dogs)
message = "I like cats and dogs, but I'd much rather own a dog."
words = message.split(' ')
print(words)
animals = "dog, cat, tiger, mouse, liger, bear"
# Rewrite the string as a list, and store it in the same variable
animals = animals.split(',')
print(animals)
colors = ('red', 'green', 'blue')
print("The first color is: " + colors[0])
print("\nThe available colors are:")
for color in colors:
    print("- " + color)
colors = ('red', 'green', 'blue')
animal = 'dog'
print("I have a " + animal + ".")
animals = ['dog', 'cat', 'bear']
for animal in animals:
    print("I have a " + animal + ".")
animal = 'dog'
print("I have a %s." % animal)
animals = ['dog', 'cat', 'bear']
for animal in animals:
    print("I have a %s." % animal)
animals = ['dog', 'cat', 'bear']
print("I have a %s, a %s, and a %s." % (animals[0], animals[1], animals[2]))
number = 23
print("My favorite number is " + str(number) + ".")
number = 23
print("My favorite number is %d." % number)
numbers = [7, 23, 42]
print("My favorite numbers are %d, %d, and %d." % (numbers[0], numbers[1], numbers[2]))
numbers = [7, 23, 42]
print("My favorite numbers are " + str(numbers[0]) + ", " + str(numbers[1]) + ", and " + str(numbers[2]) + ".")
names = ['Bretlee', 'Harley']
numbers = [23, 2]
print("%s's favorite number is %d, and %s's favorite number is %d." % (names[0].title(), numbers[0], names[1].title(), numbers[1]))
words = ['bretlee', 'harley', 'jaden', ]
print(words)
w =  ['bretlee', 'harley', 'jaden', ]
print(w)
d = ['my name', 'my freinds name', 'my other freinds name', ]
print(d)
# The player's power starts out at 75.
power = 75

# The player is allowed to keep playing as long as their power is over 0.
while power > 0:
    print("You are still playing, because your power is %d." % power)
    # Your game code would go here, which includes challenges that make it
    #   possible to lose power.
    # We can represent that by just taking away from the power.
    power = power - 1
    
print("\nOh no, your power dropped to 0! Game Over.")