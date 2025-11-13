def gcd(n, m):
    """Return the greatest common divisor of n and m.
    Use exhaustive search, trying divisors from 1 up to the maximum possible."""
    greatest_cd = 1
    for cd in range(1, min(n, m) + 1):
        if n % cd == 0 and m % cd == 0:
            greatest_cd = cd
    return greatest_cd

def gcd_efficient(n, m):
    cd = min(n, m)
    while cd > 1:
        if n % cd == 0 and m % cd == 0:
            return cd
        cd -= 1
    return 1

if __name__ == "__main__":
    print(gcd(12, 120))
    print(gcd(12, 120))