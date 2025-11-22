from l5t25 import combine_dicts
def test_combining():
    d1={'q':1}
    d2={'w':2}
    assert combine_dicts(d1,d2)=={'q':1,'w':2}
def test_sim_key():
    d1={'q':1,'w':2}
    d2={'w':3,'e':5}
    assert combine_dicts(d1,d2)=={'q':1,'w':3,'e':5}
def test_one_empty():
    d1={'q':1,'w':2}
    d2={}
    assert combine_dicts(d1,d2)=={'q':1,'w':2}
def test_two_empty():
    d1={}
    d2={}
    assert combine_dicts(d1,d2)=={}