class Error(Exception):
    pass


"""
Error class extended the base class Exception in Python. 
This is a necessary step for optimization. 
"""


class InputError(Error):
    """
    Exception raised for errors in input:
    Attribute:
        expressions: -- input expression in which error occurred.
        message: -- Explanation of the Error.
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError:
    """
    Exception raised in transition of state
    Attribute:
        previous -- State @beginning of the transition.
        next -- State intended to be transitioned.
        message -- Explaination, why specific transition is not allowed.
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

"""
Most exceptions - user defined, are defined with names that end with "Error" & is similar to standard exceptions. 
Many standard moduled define their own exceptions to report errors that may occur in the function they define. s
"""