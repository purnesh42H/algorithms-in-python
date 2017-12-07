s = 'Test of {module} are {con}'

# base should be < 10
def convert_from_decimal(number, base):
    factor, result = 1, 0
    while number > 0:
        result += number % base * factor
        factor *= 10
        number = number // base

    return result

def convert_from_decimal_any_base(number, base):
    string = '0123456789ABCDEF'
    if number < base:
        return string[number]
    else:
        return convert_from_decimal_any_base(number // base, base) + string[number%base]

def test_convert_decimal():
    number, base = 9, 2
    assert convert_from_decimal(number, base) == 1001
    assert convert_from_decimal_any_base(number, base) == '1001'
    print(s.format(module='convert from decimal', con = 'passed'))


test_convert_decimal()
