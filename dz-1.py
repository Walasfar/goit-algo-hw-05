def caching_fibonacci():
    # Save result here
    cache = {}
    
    def fibonacci(n):
        if n <= 1:
            return n
        # If number in cache
        elif n in cache:
            return cache[n]
        # Add number in cache and return it
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        
    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
