from introduction import add

def test_add():
    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    assert add(4, 2) == 6
    assert add(10, 3) == 13