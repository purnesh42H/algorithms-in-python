def gcd(x, y):
    result = 0
    while y != 0:
        result = y
        x, y = y, x % y

    return result

def test_gcd():
    a, b = 15, 10
    assert gcd(a, b) == 5

test_gcd()
