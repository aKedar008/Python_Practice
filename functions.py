# Functions = functions, which are named blocks of code
# that are designed to do one specific job.
# When you want to perform a particular task
# that you’ve defined in a function, you call the function
# responsible for it.

def greet_user():
    """Display a simple greeting"""
    print("Hello User")

greet_user()


def display_message():
    """Letting everyone know i am learning python functions"""
    print ("I am learning to code in python")

display_message()

# passing information to a function 

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('akedar008')

# An argument is a piece of information that’s passed from a function call to a function.
# In this case the argument 'akedar008' was passed to the function greet_user(), and the value was assigned to the parameter username.

def display_message():
    print("Learning Python")
display_message()

def favourite_book(name):
    """Enter Your Favourite book name"""
    print(f"My favorite book is, {name.title()}")

favourite_book('Atomic habits')

# As a function defination can have multiple paprameter we can pass arguement in mumber of ways 
#  positional arguements::
#  when you call a function python must match each argument in the function call with parameter in the function defination

def describe_pet(animal_type,pet_name):
    """Displaying the information abot the pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('Dog','MoMo')

#This is Keyword arguement, helps not to mess up the arguements and the parameters.
describe_pet(animal_type = 'Horse', pet_name='Thunder')

# Default value's here we assign the default parameter for reccuring tasks if the parameter isin't gonna change we can use defaul values there 

def my_pet (pet_name1,animal_type1 ='Dog'):
    print(f"\nI have a {animal_type1}.")
    print(f"My {animal_type1}'s name is {pet_name1.title()}")

my_pet('MoMo')
#if arugement is passed it will ignore the value passed in the parameter

#another example 
def make_tshirt(text_message,size):
    print(f"\nSize Entered: {size}.")
    print(f"Message on tshirt: {text_message}.")

make_tshirt(40,"Git Commit")
make_tshirt(text_message="Merge the request",size=41)

#Returning a simple value

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return (full_name.title())

musician = get_formatted_name("arijit","singh")
print(musician)

#making an arguement optional
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return (full_name.title())

musician = get_formatted_name("arijit","singh")
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Returning a dictonary 
def build_person(first_name,last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}

    if (age):
        person['age'] = age
        return person
    
musician = build_person('jimi','hendrix', age=27)
print(musician)


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
while True:
 print("\nPlease tell me your name:")
 print("(enter 'q' at any time to quit)")

 f_name = input("First name: ")
 if f_name == 'q':
    break

 l_name = input("Last name: ")
 if l_name == 'q':
    break

 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")

 

# 8.7 task make_album

def make_album(artist,title,no_of_songs = None):
    art = {'Name':artist, 'Title':title}
    if no_of_songs:
        art['no_of_songs'] = no_of_songs
        
    return art
    
album = make_album('A','album1')
print(album)
album = make_album('B','album2')
print(album)
album = make_album('A','album3',5)
print(album)

# passing a list in a funtion:

def greet_users(names):
    messages = []
    for name in names:
        msg = f"Hello, {name.title()}!"
        messages.append(msg)
    return messages

username = ['hannah','ty','jake']
result = greet_users(username)
print(result)

# modifying a list in a function
#1st lets do this without using function

unprinted_design = ['mobile cover', 'robot pendant', 'cars']
completed_model = []

while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"{current_design} is getting printed")

    completed_model.append(current_design)
print(f"\nfollowing are the completed models:")
for i in completed_model:
    print(i)

# 2nd lets create 2 function that will do our check our printing and other will show complted design
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_design = []

def print_model(unprinted_design, completed_design):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"printing model: {current_design}")
        completed_design.append(current_design)
    
def show_completed_models(completed_design):
    print(f"\nFollowing Designs are printed:")
    for i in completed_design:
        print(i)

print_model(unprinted_design, completed_design)
show_completed_models(completed_design)

