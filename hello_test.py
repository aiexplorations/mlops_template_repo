from hello import add, add_numpy


def test_add():
    assert 2 == add(1, 1)

def test_add_numpy():
    assert 2 == add_numpy(1,1)
