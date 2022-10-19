def fib(n: int) -> int:
    """Compute the n'th Fibonacci number."""
    match n:
        case 0: return 0
        case 1: return 1
        case _: return fib(n-1) + fib(n-2)