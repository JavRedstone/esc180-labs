# P1 a)
def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """

    str_dict = ""
    for key, value in d.items():
        str_dict += f"{key}, {value}\n"
    if len(str_dict) != 0:
        return str_dict[:-1] # \n is one character, not two
    return str_dict

# P1 b)
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""

    # Keys must be unique, therefore we can sort the keys first, and find the corresponding values
    new_dict = {}
    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        new_dict[key] = d[key]
    return dict_to_str(new_dict)

# P2
def luckiest_kid(halloween_haul):
    haul_count = {}
    lucky_kid = ""
    max_candies = 0
    for house, haul in halloween_haul.items():
        for kid, candies in haul.items():
            if kid in haul_count.keys():
                haul_count[kid] += len(candies)
            else:
                haul_count[kid] = len(candies)
            if haul_count[kid] > max_candies:
                max_candies = haul_count[kid]
                lucky_kid = kid
    return lucky_kid

# P3
def is_existing(board, y, x):
    return y >= 0 and x >= 0 and y < len(board) and x < len(board[0])

def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    # The real function is returning whether they're open or semi-open or closed, and is using y_end, x_end
    prev_y, prev_x = y_start - dy, x_start - dx
    next_y, next_x = y_start + length * dy, x_start + length * dx
    prev_is_col = is_existing(board, prev_y, prev_x) and board[prev_y][prev_x] == col
    next_is_col = is_existing(board, next_y, next_x) and board[next_y][next_x] == col
    return not (prev_is_col or next_is_col)


if __name__ == "__main__":
    # P1 a)
    dict = {1:2, 0:3, 10:5}
    print("P1 a) ==============================")
    "1, 2\n0, 3\n10, 5"
    print(dict_to_str(dict))

    # P1 b)
    print("P1 a) ==============================")
    print(dict_to_str_sorted(dict))

    # P2
    print("P2 ==============================")
    halloween_haul = {
        "house1": {
            "Annie": ["snickers", "mars"],
            "Johnny": ["snickers"]
        },
        "house2": {
            "Annie": ["coffee crisp", "mars"],
            "Jackie": ["coffee crisp"]
        }
    }
    print(luckiest_kid(halloween_haul))
