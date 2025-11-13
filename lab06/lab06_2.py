# QUESTION 4
NUM_ITER = 4000
ADJUSTMENT_FACTOR = 0.1
# QUESTION 4 a) E is the negation of sum of the energies term1, term2, and term3, so when you have a positive x0*x1 and w01 increases, then term1 will increase, so the sum will become more negative (energy decreases). This applies to term2 and term3 as well in the exact same manner.
def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:",
                E(x0, x1, x2, w01, w02, w12))


# QUESTION 4b)
def new_min_adjust(x0, x1, x2, w01, w02, w12):
    global ADJUSTMENT_FACTOR

    # Adjust w01
    if x0 * x1 > 0:
        w01 += ADJUSTMENT_FACTOR
    else:
        w01 -= ADJUSTMENT_FACTOR

    # Adjust w02
    if x0 * x2 > 0:
        w02 += ADJUSTMENT_FACTOR
    else:
        w02 -= ADJUSTMENT_FACTOR

    # Adjust w12
    if x1 * x2 > 0:
        w12 += ADJUSTMENT_FACTOR
    else:
        w12 -= ADJUSTMENT_FACTOR

    return w01, w02, w12

def get_minimum_energy(w01, w02, w12):
    min_e = 1e6
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                e = E(x0, x1, x2, w01, w02, w12)
                if e < min_e:
                    min_e = e
    return min_e

# QUESTION 4c)
def repeat_new_min_adjust(num_iter, x0, x1, x2, w01, w02, w12):
    for i in range(num_iter):
        print(f"Iteration {i + 1}: ===============")
        w01, w02, w12 = new_min_adjust(x0, x1, x2, w01, w02, w12)
        print_all_energies(w01, w02, w12)
        min_e = get_minimum_energy(w01, w02, w12)
        if E(x0, x1, x2, w01, w02, w12) == min_e:
            break
        print(f"MINIMUM ENERGY: {min_e}")
    # return w01, w02, w12
    return [w01, w02, w12]

if __name__ == '__main__':
    w01 = 2
    w02 = -1
    w12 = 1
    x0, x1, x2 = -1, 1, 1
    print_all_energies(w01, w02, w12)
    # QUESTION 4b)
    print("QUESTION 4b) --------------------")
    w01, w02, w03 = new_min_adjust(x0, x1, x2, w01, w02, w12)
    print_all_energies(w01, w02, w12)
    # QUESTION 4c), d), e), f)
    print("QUESTION 4c), d), e), f) --------------------")
    w01 = 2
    w02 = -1
    w12 = 1
    # w01, w02, w12 = repeat_new_min_adjust(NUM_ITER, x0, x1, x2, w01, w02, w12)
    w01, w02, w12 = repeat_new_min_adjust(NUM_ITER, x0, x1, x2, w01, w02, w12)
    print(f"Weights: {w01}, {w02}, {w03}")
