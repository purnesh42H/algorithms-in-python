s = 'Test of {module} are {con}'

# base should be < 10
def convert_to_decimal(number, base):
    factor, result = 1, 0
    while number > 0:
        result += number % 10 * factor
        factor *= base
        number = number // 10

    return result

def test_convert_decimal():
    number, base = 1001, 2
    assert convert_to_decimal(number, base) == 9
    print(s.format(module='convert decimal', con = 'passed'))


test_convert_decimal()
