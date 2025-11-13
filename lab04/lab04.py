import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS, MIN_A, MAX_A, NUM_A = 100, 0, 100, 10000

def generate_data_noisy(a, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(a * x) + 0.1 * np.random.randn(num_points)
    return y
def generate_data(a, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(a * x)
    return y
def sum_squared_differences(y1, y2):
    s = 0
    for i in range(len(y1)):
        s = s + (y1[i] - y2[i]) ** 2
    return s

if __name__ == "__main__":
    secret_a = 2.5
    y = generate_data_noisy(secret_a, NUM_POINTS)

    min_sqd = 1e5
    best_fit = None
    best_a = 0
    # There is a better way to do this (this is really slow)
    for a in np.linspace(MIN_A, MAX_A, NUM_A):
        fit = generate_data(a, NUM_POINTS)
        sqd = sum_squared_differences(fit, y)
        if sqd < min_sqd:
            min_sqd = sqd
            best_fit = fit
            best_a = a
    print(min_sqd, best_a)

    x = np.linspace(0, 2 * np.pi, NUM_POINTS)

    plt.plot(x, y,label='noisy')
    plt.plot(x, best_fit,label='best fit')
    plt.title("Noisy Data Fit")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()