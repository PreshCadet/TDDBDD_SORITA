import pytest

class Calculator:
    def add(self, a,b):
        return a+b
        
        
calc = Calculator()

def test_add_case1():
    assert(calc.add(1,1)) == 2
def test_add_case2():
    assert(calc.add(1.0,2.5)) == 3.5
def test_add_case3():
    assert(calc.add(0,0)) == 0
def test_add_case4():
    assert(calc.add(-5,-6)) == -11
