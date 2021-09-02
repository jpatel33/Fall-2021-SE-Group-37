import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code import cubeme, squareme, inc

def testcube():
    assert cubeme(-2) == -8
    assert cubeme(2) == 8

def testsquare():
    assert squareme(2) == 4
    assert squareme(-2) == 4

def test_inc():
    assert inc(3) == 4
