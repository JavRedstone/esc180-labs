import myrandom

MAX_CYCLE_LEN = 10000
def find_cycle_len(a, b):
    global MAX_CYCLE_LEN
    myrandom.initialize()
    myrandom.set_a_b(a, b)
    prev = []
    l = 0
    while l <= MAX_CYCLE_LEN:
        val = myrandom.myrandom()
        if len(prev) > 0 and val == prev[0]: # Ideally, if that is the case, check the next len(prev) numbers and do indexing via l - n or l % n
            return l
        prev.append(val)
        l += 1
    return -1

if __name__ == '__main__':
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(myrandom.myrandom())
    print(find_cycle_len(10, 7))
    print(find_cycle_len(438750932854830938457, 287492837491))