def fibonacci_sequence(limit):
    fib = [0, 1]
    while fib[-1] <= limit:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

def is_in_fibonacci(number):
    fib = fibonacci_sequence(number)
    if number in fib:
        return True, fib
    return False, fib

number_to_check = 34

belongs, sequence = is_in_fibonacci(number_to_check)

print(f"Sequência de Fibonacci até {number_to_check}:")
print(sequence)

if belongs:
    print(f"O número {number_to_check} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number_to_check} NÃO pertence à sequência de Fibonacci.")