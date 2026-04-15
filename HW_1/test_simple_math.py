from simple_math import SimpleMath
import pytest

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square(simple_math):
    assert simple_math.square(2) == 4

def test_cube(simple_math):
    assert simple_math.cube(-3) == -27
