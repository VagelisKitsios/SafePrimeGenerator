import sys
from random import getrandbits
from sympy import primerange
from gmpy2 import is_strong_bpsw_prp as isprime


def safe_prime_generator(bits: int):
    primes = list(primerange(5, bits))

    def valid_pair_test(x: int) -> bool:
        for k in primes:
            a = x % k
            if not a or a == (k-1)//2:
                return False
        return True

    n = getrandbits(bits-1)   # generate a random 2048-bit number
    if n.bit_length() < bits-1:
        n += 2**(bits-2)
    n -= (n % 12) + 1   # a safe prime must be of the form p = 12k - 1
    n2 = n - 12
    while True:
        # if the pair (n, 2n + 1) is a possible Germain/Safe-prime pair
        if valid_pair_test(n):
            if isprime(n) and isprime(n*2 + 1):  # if n and 2n + 1 are both prime return 2n + 1
                return n*2 + 1
        n += 12

        if valid_pair_test(n2):
            if isprime(n) and isprime(n2*2 + 1):
                return n2*2 + 1
        n2 -= 12

def main(args):
    N = int(args[0])
    P = safe_prime_generator(N)
    print(P)

if __name__ == "__main__":
    main(sys.argv[1:])
