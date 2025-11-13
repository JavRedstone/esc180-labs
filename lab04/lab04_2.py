def generate_hats(num_students):
    import random
    hats = []
    for i in range(num_students):
        if random.random() < 0.5:
            hats.append('W')
        else:
            hats.append('B')
    return hats
def count_white_hats(hats):
    '''Return the number of white hats in the list hats.'''
    count = 0
    for hat in hats:
        count += hat == 'W'
    return count
def make_guesses(hats):
    '''Return a list of guesses, one for each hat in hats.
    The guesses should be ’W’ or ’B’.'''

    # For the student hats[i], make a guess based on the number
    # of white hats that they see
    # You can use count_white_hats() to help you figure out the
    # number of white hats that a student sees

    guesses = []
    for i in range(len(hats)):
        num_hats = count_white_hats(hats[0:i] + hats[i+1: len(hats)])
        choice = 'W'
        if num_hats % 2 == 0:
            choice = 'B'
        guesses.append(choice)
    return guesses
def are_all_guesses_correct(hats, guesses):
    '''Return True if all guesses are correct.'''
    return count_white_hats(hats) == count_white_hats(guesses)
if __name__ == "__main__":
    num_students = 12
    hats = generate_hats(num_students)
    print("Hats: ", hats)
    guesses = make_guesses(hats)
    print("Guesses:", guesses)
if are_all_guesses_correct(hats, guesses):
    print("All guesses correct!")
else:
    print("Not all guesses correct.")