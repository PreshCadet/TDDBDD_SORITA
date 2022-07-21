import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b 
        
@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is "+ base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is "+ base_calculator.name)
    
    assert True

def test_operations_subtract(base_calculator):
    assert base_calculator.subtract(3,2) == 1
def test_operations_add(base_calculator):
    assert base_calculator.add(3,2) == 5
def test_operations_multiply(base_calculator):
    assert base_calculator.multiply(3,2) == 6