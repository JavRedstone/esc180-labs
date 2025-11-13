# QUESTION 1
L = [["CIV", 92],
    ["180", 98],
    ["103", 99],
    ["194", 95]]
print("QUESTION 1 --------------------")
print(L[2][1])

# QUESTION 2
def get_nums(L):
    res = []
    for l in L:
        res.append(l[1])
    return res
print("QUESTION 2 --------------------")
print(get_nums(L))

# QUESTION 3
def lookup(L, num):
    for l in L:
        if l[1] == num:
            return l[0]
    return None
print("QUESTION 3 --------------------")
print(lookup(L, 99))