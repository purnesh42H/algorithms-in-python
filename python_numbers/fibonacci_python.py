def fibonacci_sequence_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_sequence_recursive(n-2) + fibonacci_sequence_recursive(n-1)

def fibonacci_sequence_dp(n):
    result = [0, 1]
    if n > 2:
        for i in range(2, n+1):
            result.append(result[-1] + result[-2])
            
    return result[-1]

def fibonacci_single_space(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b

def test_fibonacci():
    n = 4
    assert fibonacci_sequence_recursive(n) == 3
    assert fibonacci_sequence_dp(n) == 3
    print(fibonacci_single_space(n))


test_fibonacci()
