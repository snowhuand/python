# In memory space, it creates an object with the name of
# function
# creating docstring: documentation about your code
#                     called by function_name.__doc__
# Annotation is an arbitrary piece of information that can be associated with a
#           parameter(: type) or return value (->)
#           call by: function_name.__annotation__
# Other attributes:
#        - __name__
#        - __dict__
# Passing of arguments:
#       - mutable: it changes from source
#       - immutable: it doesnt change the source value (string)
def subject(subject_code:str="CP1000", subject_name:str="Introduction")-> str:
    """
    This is  function that construct subject related details.
    :param subject_code: The code associated with the subject, eg. CP1401
    :param subject_name: The full name of the subject
    :return: string equivalent
    """
    string_msg = "This subject {} refers to {}".format(subject_code, subject_name)
    return string_msg, "ipio"

print(subject("CP1404", "Programming I"))
print(subject.__doc__)
print(subject.__annotations__)
print(subject.__name__)
print(subject.__dict__)

(x, y) = subject()
tup = subject()
"""
# Immutable string
my_str = "abc"
#my_str[1] = "zz"

# Mutable list
my_list = [1, 2, 3]
my_list[1] = 100
print(my_list)

When def is evaluated, it is done only once.
The associationis preserved btw invocation.

"""