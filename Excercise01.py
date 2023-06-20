"""
Variables and Types

Complete this script's TODOs

Fill in the blank: if you encounter 4 underscores, replace each ____ placeholder with the right code instructions.
Beware to only replace the ____ placeholder
Example:
    # TODO: assign a string to a variable var
    ____ = "____"
    # ____ = "____" becomes:
    var = "a string"

Freeform Coding: if you encounter 4 dots, try to code freely over multiple lines to meet the TODO's requirements.
You can code freely and apply your art and knowledge
Example:
    # TODO: Create a lambda function multiplying two parameters
    ....
    # .... becomes:
    lambda a,b: a * b

Questions: Answer the question as best as you can.
Example
    # Question: What is a variable
    #::
    # becomes:
    #:: A variable is a name for a value stored and accessible in a typed format like int, float, str, list,
    dict and others
"""
#
# Numbers
#

# TODO: assign an integer value to a variable called number
____ = ____

# TODO: assign a floating point number to a variable called floating_number
____ = ____

# TODO: print the integer and the float variable to the screen each on a seperate line
____(____)
print(____)

# TODO: print the type of the variable number to the screen
____(type(____))

# TODO: and how would you print the variable of the floating number to the screen?
____(____(____))

# TODO: add the numbers and floating_numbers together, store the result in a variable called total
____ ____ number ____ floating_number

# TODO: print the total to the screen and the type of the total
print(____)
print(____(total))

# Question: Why is the type of the variable total a float and not an int?
#::

# TODO print the variable total as if it would be of an integer type
____(int(____))

# TODO: complete the following function add so that it returns the addition of the two parameters a and b
def add(____, ____):
    t = ____ + ____
    ____ t

# Question: How could you rewrite the add() function's body and reduce it to one line-of-code?
#::

# TODO: Write a subtract function analogous to the add() function above
....

# TODO: Use only your add() and subtract() functions above to fullfill the following equation:
# result = ((1+6)-2)+(7+(3-5))
result = add( ____( ____(1,6), 2), add(7, ____(3, 5)))

# TODO: print the variable result to the screen, but as if it would be a float
____(float(____))

# TODO: if the variable result is equal to 10, print the message "Correct" otherwise print "Wrong"
____ result ____ 10:
    print(____)
____:
    print(____)

# TODO: Print for each of the following variables it's type and value:
a_int = 1
a_float = 3.3
a_string = "equals to"
a_bool = True
a_list = [1,3.3,"equals_to"]
a_function_object = add
a_tuple = (1,3.3,"equals_to")
a_dict = {"a":1, "b":3.3, "text":"equals_to"}
a_set = {1,2,3,3,4}

....

# TODO: complete the following f-string to interpolate variables into a string which gets printed out to the screen
print(f"{a_function_object.__name__.upper()} {____} to {a_float} {____} {a_function_object(____, ____)}!")