import math

HARD_STOP = 1e6

def compute_pi(N):
    sum = 0
    for n in range(N):
        sum += (-1)**n / (2 * n + 1)
    return 4 * sum

def n_sig_digs(a, n, is_round):
    val = (a * (10 ** (n - 1))) # Since 3._____,and sig figs are rounded
    if is_round:
        return round(val)
    else:
        return math.floor(val)

def are_equal(a, b, n):
    return n_sig_digs(a, n, False) == n_sig_digs(b, n, True)

def num_terms(n):
    global HARD_STOP

    N = 0
    while N <= HARD_STOP:
        N += 1
        if are_equal(math.pi, compute_pi(N), n):
            print(math.pi, compute_pi(N))
            return N
    return N

print(num_terms(4))