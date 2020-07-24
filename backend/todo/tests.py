from django.test import TestCase

# Create your tests here.
# program to do aAddition of two input numbers
def add(first_number =0, second_number =0,):
    first_number = int ( input ("Enter first number") )  # type: int
    second_number = int ( input ("Enter second number") )
    sum1 = first_number + second_number
    return sum1
add( )
print("Addition of two number is: ", sum1)