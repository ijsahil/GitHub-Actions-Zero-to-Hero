# app.py
# This is a test commit
def add(a, b, c, d, e):
    return a + b + c + d + e
 
def test_add():
    assert add(1, 2, 3, 4, 2) == 12
    assert add(1, -1, 4 , -2, 1) == 3
