from example_python_package_mate import multi, my_name

def test_multi_w_small_nums():
    answer = multi(3,3)
    assert answer == 9

def test_multi_w_big_num():
    answer = multi(100,2)
    assert answer == 200


def test_name():
    input_name = my_name("Mate")
    correct_name = my_name("Mate")
    
    assert input_name == correct_name
    