from l5t22 import find_unique
def test_empty():
    assert find_unique([])==[]
def test_all_unique():
    assert find_unique([1,3,5])==[1,3,5]
def test_with_dubls():
    assert find_unique([1,2,2,3])==[1,3]
def test_only_dubls():
    assert find_unique([1,1,1])==[]
def test_diff_types():
    assert find_unique(['1',1,1,3,'3'])==['1',3,'3']