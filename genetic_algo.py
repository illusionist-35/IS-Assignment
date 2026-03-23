import random

# Fitness function
def fitness(x):
    return x * x

# Create initial population (random integers 0–31)
population = [random.randint(0, 31) for _ in range(6)]

for generation in range(10):
    # Evaluate fitness
    population = sorted(population, key=fitness, reverse=True)
    
    # Select top 2
    parents = population[:2]
    
    # Crossover and mutation to create new population
    new_population = parents.copy()
    while len(new_population) < 6:
        p1, p2 = random.choice(parents), random.choice(parents)
        child = (p1 + p2) // 2  # simple crossover
        
        # Mutation
        if random.random() < 0.1:
            child = random.randint(0, 31)
        
        new_population.append(child)
    
    population = new_population

# Best solution
best = max(population, key=fitness)
print("Best solution:", best)
print("Best fitness:", fitness(best))