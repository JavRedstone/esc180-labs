# P1
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# P2 #1
def sum_digits(n):
    if n % 10 == n:
        return n
    return n % 10 + sum_digits(n // 10)

# P2 #2
def times(a, b):
    if b == 0:
        return 0
    return times(a, b - 1) + a

# P3
def linear_search(L, e):
    if L[0] == e:
        return 0
    return linear_search(L[1:], e) + 1

# P4
def interleave(L1, L2):
    if len(L1) == 1 and len(L2) == 1:
        return L1 + L2
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

# P5
def reverse_rec(L):
    reverse_self(L, 0)

def reverse_self(L, i):
    L[i], L[-1 - i] = L[-1 - i], L[i]
    if i == len(L) // 2:
        return
    return reverse_self(L, i + 1)

def reverse_rec_2(L):
    if len(L) <= 1:
        return
    f = L.pop(0)
    b = L.pop(-1)
    reverse_rec_2(L)
    L.insert(0, b)
    L.append(f)

# P6
def zigzag(L):
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end=" ")
    else:
        zigzag(L[1:-1])
        print(L[-1], L[0], end=" ")

# P7
def split_list(L, sep):
    split = []
    curr = []
    for e in L:
        if e in sep:
            if len(curr) > 0:
                split.append(curr[:])
                curr = []
        else:
            curr.append(e)
    if len(curr) > 0:
        split.append(curr[:])
    return split

if __name__ == "__main__":
    # P1
    print(power(2, 3))

    # P2 #1
    print(sum_digits(123))

    # P2 #2
    print(times(3, 4))

    # P3
    print(linear_search([1, 5, 2, 8, 3], 2))

    # P4
    print(interleave([1, 2, 3], [7, 8, 9]))

    # P5
    L = [1, 4, 2, 5, 6]
    reverse_rec(L)
    print(L)
    L = [1, 4, 2, 5, 6]
    reverse_rec_2(L)
    print(L)

    # P6
    L = [1, 4, 2, 5, 6]
    zigzag(L)
    print()

    # P7
    print(split_list([1, 2, 6, 4, 5, 3, 7], [3, 6]))