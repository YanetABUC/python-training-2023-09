#Fibonacci sequence

def get_fibonacci_of(n):
    if n in [0, 1]:
       return n
    else:
        return get_fibonacci_of(n - 1) + get_fibonacci_of(n - 2)

def get_fibonacci_sequence(n):
    sequence = []

    for i in range(1, n + 1):
        sequence.append(get_fibonacci_of(i))
    
    return sequence

number = int(input("Type a number: "))
fibonacci = get_fibonacci_of(number)
fibonacci_sequence = get_fibonacci_sequence(number)
print(f"Fibonacci[{number}] is {fibonacci}")
print(f"Fibonacci sequence is {fibonacci_sequence}")
