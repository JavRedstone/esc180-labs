second_previous_value = 0
previous_value = 0
current_value = 0
mem = 0

def display_current_value():
    print(current_value)

def update_previous():
    global second_previous_value, previous_value, current_value
    second_previous_value = previous_value
    previous_value = current_value

def add(to_add):
    global current_value
    update_previous()
    current_value += to_add

def mult(to_mult):
    global current_value
    update_previous()
    current_value *= to_mult

def div(to_div):
    global current_value
    update_previous()
    current_value /= to_div

def memory():
    global current_value, memory
    update_previous()
    memory = current_value

def memory_plus():
    global current_value, memory
    update_previous()
    memory += current_value

def memory_minus():
    global current_value, memory
    update_previous()
    memory -= current_value

def memory_recall():
    global current_value, memory
    update_previous()
    current_value = memory

def undo():
    global current_value, previous_value
    previous_value, current_value = current_value, previous_value

def undo2():
    global current_value, second_previous_value
    second_previous_value, current_value = previous_value, second_previous_value


if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent value:", current_value)
    print("Testing `add(x)`")
    display_current_value()
    add(5)
    display_current_value()
    add(10)
    display_current_value()

    print("Testing `mult(x)`")
    display_current_value()
    mult(3)
    display_current_value()
    mult(2)
    display_current_value()

    print("Testing `div(x)`")
    display_current_value()
    div(3)
    display_current_value()
    # div(0) # Causes `ZeroDivisionError`
    # display_current_value()

    print("Testing `memory()` and `recall()`")
    memory()
    display_current_value()
    mult(4)
    display_current_value()
    memory_recall()
    display_current_value()

    """
    Memory + and - don't really fit this calculator, but they are implemented above
    """

    print("Testing `undo()`")
    current_value = 25
    display_current_value()
    add(5)
    display_current_value()
    mult(2)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    print("Testing `undo2()`")
    current_value = 0
    display_current_value()
    add(1)
    display_current_value()
    mult(2)
    display_current_value()
    undo()
    display_current_value()
    add(5)
    display_current_value()
    undo2()
    display_current_value()