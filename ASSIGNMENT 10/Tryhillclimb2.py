def generate_neighbors(x):
    return [x + 0.1, x - 0.1]
def hill_climbing(f, x0):
    x = x0 
    while True:
        neighbors = generate_neighbors(x)
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):
            return x
        x = best_neighbor
best_neighbor = hill_climbing(lambda x: -x**2 + 4*x, 0.0)
print(f"Best solution: x = {best_neighbor}, f(x) = {-best_neighbor**2 + 4*best_neighbor}")
