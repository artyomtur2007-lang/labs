from l5t24 import are_anagrams
def test_anagrams():
    assert are_anagrams('миска','симка') is True
def test_with_upandlow():
    assert are_anagrams('LiSTEN','silENT') is True
def test_no_anagr():
    assert are_anagrams('привет','пока') is False
def test_with_spaces():
    assert are_anagrams('к о т','т о к') is True
def test_empty_strs():
    assert are_anagrams('','  ') is True
def test_nums():
    assert are_anagrams('123','231') is True
def test_one_empty():
    assert are_anagrams('abc','') is False