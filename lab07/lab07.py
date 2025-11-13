import numpy as np

# P1
def print_matrix(M, annotations = False):
    if annotations:
        print("The matrix is currently:")
    print(np.array(M))

def print_separator():
    print("------------------")

# P2
def get_lead_ind(row):
    for i in range(len(row)):
        e = row[i]
        if e != 0:
            return i
    return -1

# P3
def get_row_to_swap(M, start_i):
    start_lead_i = get_lead_ind(M[start_i])
    min_lead_i = len(M[0])
    swap_i = start_i
    for i in range(start_i, len(M)):
        lead_i = get_lead_ind(M[i])
        if lead_i < min_lead_i:
            min_lead_i = lead_i
            swap_i = i
    return swap_i

# P4
def add_rows_coefs(r1, c1, r2, c2):
    return (np.array(r1) * c1 + np.array(r2) * c2).tolist()

# P5
def eliminate(M, row_to_sub, best_lead_ind, below = True):
    for i in range(row_to_sub + 1, len(M), 1):
        lead_i = get_lead_ind(M[i])
        if lead_i == best_lead_ind:
            M[i] = add_rows_coefs(M[row_to_sub], -M[i][lead_i] / M[row_to_sub][best_lead_ind], M[i], 1)
    return M

# P6
def forward_step(M, augmented = False):
    print_separator()
    print("Now performing the forward step")
    print_matrix(M, True)
    for i in range(len(M)):
        print_separator()
        print(f"Now looking at row {i}")
        swap_i = get_row_to_swap(M, i)
        lead_i = get_lead_ind(M[swap_i])
        if lead_i != -1:
            M[swap_i], M[i] = M[i], M[swap_i]
            print(f"Swapping rows {i} and {swap_i} so that entry {lead_i} in the current row is non-zero")
            print_matrix(M, True)
            print(f"Adding row {i} to rows below it to eliminate coefficients in column {lead_i}")
            eliminate(M, i, lead_i)
            print_matrix(M, True)
    print("Done with the forward step")
    print_separator()
    print_matrix(M, True)
    return M

# P7

def reduce(M, row_to_sub):
    lead_i = get_lead_ind(M[row_to_sub])
    for i in range(row_to_sub - 1, -1, -1):
        if M[i][lead_i] != 0:
            M[i] = add_rows_coefs(M[row_to_sub], -M[i][lead_i] / M[row_to_sub][lead_i], M[i], 1)
    return M

def backward_step(M, augmented = False):
    print_separator()
    print("Now performing the backward step")
    print_matrix(M, True)
    for i in range(len(M) - 1, -1, -1):
        print_separator()
        lead_i = get_lead_ind(M[i])
        if lead_i != -1:
            print(f"Adding row {i} to rows above it to eliminate coefficients in column {lead_i}")
            reduce(M, i)
            print_matrix(M, True)
        print_separator()
    print("Now dividing each row by the leading coefficient")
    for i in range(len(M)):
        row = M[i]
        lead_i = get_lead_ind(row)
        if lead_i != -1:
            lead_entry = row[lead_i]
            M[i] = add_rows_coefs(row, 1/lead_entry, row, 0)
    print("Done with the backward step")
    print_separator()
    print_matrix(M, True)
    return M

# P8
def get_b(M, x):
    return np.matmul(np.array(M), np.array(x))

def solve(M, b):
    for i in range(len(M)):
        M[i].append(b[i])
    forward_step(M, True)
    backward_step(M, True)
    x = [0] * (len(M[0]) - 1)
    for i in range(len(M)):
        lead_i = get_lead_ind(M[i])
        if lead_i != -1:
            # Assume all free variables take on the value of 1 (unless they have no coefficient, in which case they take on the value of 0)
            x_value = M[i][-1]
            for j in range(lead_i + 1, len(M[i]) - 1):
                e = M[i][j]
                if e != 0:
                    x_value -= e
                    x[j] = 1
            x[lead_i] = x_value
    return x

if __name__ == '__main__':
    # P1
    M = [
        [5, 6, 7, 8],
        [0, 0, 0, 1],
        [0, 0, 5, 2],
        [0, 1, 0, 0]
    ]
    print("P1 =================")
    print_matrix(M)

    # P2
    print("P2 =================")
    print(get_lead_ind(M[0]))

    # P3
    print("P3 =================")
    print(get_row_to_swap(M, 1))

    # P4
    print("P4 =================")
    print(add_rows_coefs(M[3], 2, M[1], 4))

    # P5
    M2 = [
        [5, 6, 7, 8],
        [0, 0, 1, 1],
        [0, 0, 5, 2],
        [0, 0, 7, 0]
    ]
    print("P5 =================")
    eliminate(M2, 1, 2)
    print_matrix(M2)

    # P6
    M3 = [
        [ 0, 0, 1, 0, 2 ],
        [ 1, 0, 2, 3, 4 ],
        [ 3, 0, 4, 2, 1 ],
        [ 1, 0, 1, 1, 2 ]
    ]
    float_M3 = np.array(M3).astype(float).tolist()
    print("P6 =================")
    forward_step(float_M3)

    # P7
    print("P7 =================")
    backward_step(float_M3)

    M4 = [
        [ 1, -2, 3, 22],
        [ 3, 10, 1, 314 ],
        [ 1, 5, 3, 92 ]
    ]
    float_M4 = np.array(M4).astype(float).tolist()
    forward_step(float_M4)
    backward_step(float_M4)

    # P8
    M5 = [
        [ 0, 0, 1, 0, 2 ],
        [ 1, 0, 2, 3, 4 ],
        [ 3, 0, 4, 2, 1 ],
        [ 1, 0, 1, 1, 2 ]
    ]
    x5 = [ 1, 2, 3, 4, 5 ]
    b5 = get_b(M5, x5)
    print("P8 Example 1 =================")
    x5_solved = solve(M5, b5)
    print('Matrix M')
    print_matrix(M5)
    print('Vector x (Truth)')
    print_matrix(x5)
    print('Vector b')
    print_matrix(b5)
    print('Vector x (Solved)')
    print_matrix(x5_solved)
    print('Vector b (Solved)')
    M5 = [
        [ 0, 0, 1, 0, 2 ],
        [ 1, 0, 2, 3, 4 ],
        [ 3, 0, 4, 2, 1 ],
        [ 1, 0, 1, 1, 2 ]
    ]
    print_matrix(get_b(M5, x5_solved))

    M6 = [
        [ 1, -2, 3, 22],
        [ 3, 10, 1, 314 ],
        [ 1, 5, 3, 92 ]
    ]
    x6 = [ 1, 2, 3, 4 ]
    b6 = get_b(M6, x6)
    print("P8 Example 2 =================")
    x6_solved = solve(M6, b6)
    print('Matrix M')
    print_matrix(M6)
    print('Vector x (Truth)')
    print_matrix(x6)
    print('Vector b')
    print_matrix(b6)
    print('Vector x (Solved)')
    print_matrix(x6_solved)
    print('Vector b (Solved)')
    M6 = [
        [ 1, -2, 3, 22],
        [ 3, 10, 1, 314 ],
        [ 1, 5, 3, 92 ]
    ]
    print_matrix(get_b(M6, x6_solved))

