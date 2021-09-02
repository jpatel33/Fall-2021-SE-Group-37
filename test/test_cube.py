# test cases
from code import cubeme, squareme, inc

def testcube():
    assert cubeme(-2) == -8
    assert cubeme(2) == 8

def testsquare():
    assert squareme(2) == 4
    assert squareme(-2) == 4

def test_inc():
    assert inc(3) == 4
