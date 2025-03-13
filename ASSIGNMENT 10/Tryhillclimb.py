import random

def local_search(f, x_start, step_size=0.1, max_iterations=100):
    """
    Local search optimization using Hill Climbing.
    
    Parameters:
        f (function): The objective function to optimize.
        x_start (float): Initial guess for the solution.
        step_size (float): Step size for neighbor exploration.
        max_iterations (int): Maximum number of iterations.
    
    Returns:
        tuple: (best_x, best_f_x) where best_x is the optimal solution found, and best_f_x is its function value.
    """
    x = x_start  # Start with an initial value
    for _ in range(max_iterations):
        neighbors = [x + step_size, x - step_size]  # Generate neighboring solutions
        next_x = max(neighbors, key=f)  # Select the best neighboring solution
        if f(next_x) <= f(x):  # Stop if no improvement
            break
        x = next_x  # Move to the new best solution
    return x, f(x)

# Example: Maximizing f(x) = -x^2 + 4x
def objective_function(x):
    return -x**2 + 4*x

# Run Local Search with a random starting point
initial_x = random.uniform(-10, 10)  # Start from a random position
best_x, best_value = local_search(objective_function, initial_x)

print(f"Best solution: x = {best_x}, f(x) = {best_value}")
