def primeFactors(n: int) -> None:
    c: int = 2
    prime_factors = ''
    while n > 1:
        if n % c == 0:
            if n / c > 2:
                prime_factors += str(c) + '*'
            else:
                prime_factors += str(c)
            n = n / c
        else:
            c = c + 1
    return prime_factors


if __name__ == "__main__":
    n: int = int(input("Enter your number : "))
    prime_number_factors = primeFactors(n)
    print(f"result : {prime_number_factors}")
