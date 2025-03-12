import random

def hill_climbing(f, x_start, step_size=0.1, max_iterations=100):
    x = x_start
    for _ in range(max_iterations):
        neighbors = [x + step_size, x - step_size]
        next_x = max(neighbors, key=f)
        if f(next_x) <= f(x):
            break
        x = next_x
    return x, f(x)

def objective_function(x):
    return -x**2 + 4*x

best_x, best_value = hill_climbing(objective_function, random.uniform(-10, 10))
print(f"Best solution: x = {best_x}, f(x) = {best_value}")