 def find_primes(numbers):
    primes = []

    for num in numbers:
        if num < 2:
            continue

        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes
