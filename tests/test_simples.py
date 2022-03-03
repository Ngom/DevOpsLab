from src.simple_functions import * # src.
 
# define add test function
def test_add():
    """ test with assert """
    assert add(3, 5) == 8, 'Do not behave correstly !!'

# define prod test function
def test_prod():
    """ test with assert """
    assert prod(3, 5) == 15, 'Not behaving correstly !!'

# define power test function
def test_power():
    """ test with assert """
    assert power(5, 2) == 25, 'It does not behave correstly !!'

def test_factorial():
    """ test the recursive factorial function"""
    assert factorial(5) == 120, 'No, check your function or its args'
    assert factorial(3) == 6, 'No, check your function or its args'
    assert factorial(10) == 3628800, 'No, check your function or its args'

# tape these command to connect src and tests before execiting.
# Do it just once !
# $ export PYTHONPATH="$PWD/src"
# $ echo $PYTHONPATH
