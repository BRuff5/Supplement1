def add(num1, num2):
    """Adds two numbers and returns the result.
    
    Args:
        num1: the first summand.
        num2: the second summand.
    
    Returns:
        The sum of the two numbers   
        return num1 + num2
    """
def count(string):
    return len(string)

def test_should_return_four_for_two_and_two():
    assert add(2, 2) == 4
    
def test_should_return_length_five_for_hello():
    assert count("hello") == 5