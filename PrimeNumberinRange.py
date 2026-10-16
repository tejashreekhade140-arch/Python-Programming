def primesInRange(start: int, end: int) -> list[int]:
    primes = []

    for num in range(max(2, start), end + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    print(primes)


primesInRange(10, 20)