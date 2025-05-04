import numpy as np
def objective_function(x):
    return x**2
def clonal_selection_algorithm(population_size, num_clones, mutation_rate, num_generations, search_space):
    # Initialize population
    population = np.random.uniform(search_space[0], search_space[1], population_size)
    
    for generation in range(num_generations):
        # Evaluate fitness
        fitness = np.array([objective_function(x) for x in population])
        
        # Select best antibodies
        sorted_indices = np.argsort(fitness)
        selected_antibodies = population[sorted_indices[:num_clones]]
        
        # Clone and mutate
        clones = np.repeat(selected_antibodies, num_clones)
        mutations = np.random.normal(0, mutation_rate, clones.shape)
        clones = clones + mutations
        clones = np.clip(clones, search_space[0], search_space[1])  # Ensure clones stay within search space
        
        # Replace population
        population = np.concatenate((clones, np.random.uniform(search_space[0], search_space[1], population_size - num_clones)))
        
        # Track best solution
        best_fitness = np.min(fitness)
        best_solution = population[np.argmin(fitness)]
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Solution = {best_solution}")
    
    return best_solution, best_fitness

population_size = 20
num_clones = 5
mutation_rate = 0.1
num_generations = 50
search_space = (-10, 10)  # Define the search space for x

best_solution, best_fitness = clonal_selection_algorithm(population_size, num_clones, mutation_rate, num_generations, search_space)
print("\nFinal Result:")
print(f"Best Solution: {best_solution}")
print(f"Best Fitness: {best_fitness}")