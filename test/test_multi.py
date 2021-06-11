import pytest
from example_python_package_mate import multi, my_name


@pytest.mark.multi
def test_multi_w_small_nums():
    answer = multi(3,3)
    assert answer == 9

@pytest.mark.multi
def test_multi_w_big_num():
    answer = multi(100,2)
    assert answer == 200

@pytest.mark.name
def test_name():
    input_name = my_name("Mate")
    correct_name = my_name("Mate")
    
    assert input_name == correct_name


products = [(2,3,6),(-1,55,-55),(3,-4,-12),(1,100,100)]    
@pytest.mark.multi
@pytest.mark.parametrize('a, b, product',products)
def test_multi_param(a,b,product):
    assert a * b == product
