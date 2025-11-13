def drink_coffee():
    global current_time, last_coffee_time, last_coffee_time2, too_much_coffee

    if current_time - last_coffee_time2 <= 120: # Assuming that it is inclusive
        too_much_coffee = True

    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time

    print(knols, current_time, last_coffee_time, last_coffee_time2, too_much_coffee)

def study(minutes):
    global knols, current_time, too_much_coffee
    if not too_much_coffee:
        if last_coffee_time == current_time:
            knols += 10 * minutes
        else:
            knols += 5 * minutes
    current_time += minutes

    print(knols, current_time, last_coffee_time, last_coffee_time2, too_much_coffee)

def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols

    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -1000
    last_coffee_time2 = -1000

if __name__ == "__main__":
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(10) # knols = 500
    drink_coffee() # knols = 500
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600