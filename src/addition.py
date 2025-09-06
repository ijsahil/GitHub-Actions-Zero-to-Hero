# app.py
# This is a test commit
def add(a, b, c, d):
    return a + b + c + d

def test_add():
    assert add(1, 2, 3, 4) == 10
    assert add(1, -1, 4 , -2) == 2
