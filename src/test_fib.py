from fib import fib

def test_fib()-> None:
    assert fib(0) == 0
    assert fib(1) == 1
    for i in range(2, 15):
        assert fib(i) == fib(i-1) + fib(i-2)
