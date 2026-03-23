import random

# Objective function
def f(x):
    return x**2

# Initialize particles
particles = [random.uniform(-10, 10) for _ in range(5)]
velocities = [0 for _ in range(5)]

pbest = particles.copy()
gbest = min(particles, key=f)

# PSO parameters
w = 0.5   # inertia
c1 = 1.5  # cognitive
c2 = 1.5  # social

for _ in range(20):
    for i in range(len(particles)):
        r1, r2 = random.random(), random.random()
        
        # Update velocity
        velocities[i] = (w * velocities[i] +
                         c1 * r1 * (pbest[i] - particles[i]) +
                         c2 * r2 * (gbest - particles[i]))
        
        # Update position
        particles[i] += velocities[i]
        
        # Update personal best
        if f(particles[i]) < f(pbest[i]):
            pbest[i] = particles[i]
    
    # Update global best
    gbest = min(particles, key=f)

print("Best solution:", gbest)
print("Best value:", f(gbest))