import pytest
@pytest.mark.smoke
def test_sample_one():
    assert 6>1
@pytest.mark.xfail
def test_sample1():
    assert 4 <= 3
@pytest.mark.skip
def test_sample_one():
    print("Hai")
    x=6
    y=6
    assert x==y
@pytest.mark.regression
def test_sample():
    print("Hello")
    assert 1+1 == 2 
@pytest.mark.test1
def test_sample2():
    print("Python")
    x = 'aa'
    y = 'aa'
    assert x==y 
    #x.__eq__(y)
@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_addition(test_input,expected):
    assert test_input+2==expected