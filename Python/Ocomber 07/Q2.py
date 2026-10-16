def find_primes(numbers):
    primes = [344,4,3454,54,445,5,]

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
