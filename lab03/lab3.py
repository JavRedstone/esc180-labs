def compute_pi():
    sum = 0
    for n in range(1001):
        sum += (-1)**n / (2 * n + 1)
    return 4 * sum

def compute_pi_2():
    sum = 0
    n = 0
    while n <= 1000:
        sum += (-1)**n / (2 * n + 1)
        n += 1
    return 4 * sum

if __name__ == "__main__":
    print(compute_pi())
    print(compute_pi_2())