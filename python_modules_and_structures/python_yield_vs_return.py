'''
The difference between yield and return is that the former returns each
value to the caller and then only returns to the caller when all values to
return have been exhausted, and the latter causes the method to exit and
return control to the caller.
One great feature in Python is how it handles iterability. An iterator is a
container object that implements the iterator protocol and is based on two
methods: next, which returns the next item in the container, and iter
which returns the iterator itself. Since all methods in Python are virtual,
we are free to modify how to iterability works in our functions (and classes)
the way we like.
The yield paradigm becomes important in the context of generators,
which are a powerful tool for creating iterators. Generators are like regular
functions but instead of returning a final value in the end, they use the
yield statement to return data during execution. In other words, values
are extracted from the iterator one at time by calling its next () method
and at each of these calls, the yield expression’s value is returned. This
happens until the final call, when a StopIteration is raised:
'''

# fibonnaci function
def fibonacci_return(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b

    return a

# fibonacci generator
def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(2, n+2):
        yield a
        a, b = b, a + b

def test_fibonacci():
    assert fibonacci_return(7) == 8
    fib = fibonacci_generator(7).__iter__()
    
    assert next(fib) == 0
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5
    assert next(fib) == 8
    print('{module} tests are {con}'.format(module='fibonacci', con='passed'))
    
    

test_fibonacci()

        
