#Generate fibonacci series in python
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# Replace 'n' with the number of terms you want in the sequence
n = 20  # You can change this value to generate a different number of terms
result = generate_fibonacci(n)
print(result)