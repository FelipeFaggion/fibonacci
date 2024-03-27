def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def is_fibonacci(number, fibonacci):
    return number in fibonacci

def main():
    number = int(input("Número a ser pesquisado: "))
    fibonacci = fibonacci_sequence(number)
    if is_fibonacci(number, fibonacci):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()