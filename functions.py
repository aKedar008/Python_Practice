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