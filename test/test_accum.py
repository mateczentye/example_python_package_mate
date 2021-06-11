### Tests for accumulator class ###

import pytest
from example_python_package_mate.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

@pytest.mark.accumulator
def test_accum_init(accum):
    assert accum.count == 0

@pytest.mark.accumulator
def test_accum_add_one(accum):
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accum_add_three(accum):
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accum_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accum_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute"):
        accum.count = 10