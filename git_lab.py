import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    :param radius: float, the radius of the circle
    :return: float, the area of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    :param celsius: float, temperature in Celsius
    :return: float, temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    :param s: str, the string to check
    :return: bool, True if the string is a palindrome, False otherwise
    """
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    
    :param base: float, the base of the triangle
    :param height: float, the height of the triangle
    :return: float, the area of the triangle
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height

def is_prime(n):
    """
    Check if a number is a prime number.
    
    :param n: int, the number to check
    :return: bool, True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a - b