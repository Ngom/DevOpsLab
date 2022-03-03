from first_function import *

# define test function
def test_answer():
    """ test with assert """
    assert func(3) == 4, 'Do not behave as expected !!!'

def test_fibonacci():
    ''' test with assert '''
    assert fibonacci(5) == 8, "Review your code"
