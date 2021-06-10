
from example_python_package_mate import my_name

def test_name():
    input_name = my_name("Mate")
    correct_name = my_name("Mate")
    
    assert input_name == correct_name