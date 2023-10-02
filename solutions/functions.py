import math

def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    return number*number


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    l = ""
    leng = len(s) - 1
    while (leng >=0):
        l += s[leng]
        leng = leng - 1
    return l


def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    if n % 2 == 0:
        return "Even"
    if n % 2 != 0:
        return "Odd"


def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    l = ""
    leng = len(s) - 1
    while (leng >=0):
        l += s[leng]
        leng = leng - 1
    return s == l 


def calculate_area(shape, *args):
    """
    This function calculates and returns the area of the specified shape based on the provided arguments.
    The type of shape and its corresponding parameters are passed as arguments.
    
    Supported shapes and their parameters:
    - "circle": radius
    - "rectangle": length, width
    - "triangle": base, height
    
    :param shape: str, the type of the shape for which the area is to be calculated.
    :param args: tuple, the parameters required to calculate the area of the specified shape.
    :return: float, the area of the specified shape.
    
    :raises ValueError: If an unsupported shape is provided or if the number of parameters 
    for the shape is incorrect.
    """
    pass  # Implement your solution here

    if shape == "circle":
        if len(args) == 1:
            return args[0]*args[0]*math.pi
    if shape == "rectangle":
        length, width = args
        return length * width
    if shape == "triangle":
        base, height = args
        return int((base*height) / 2)