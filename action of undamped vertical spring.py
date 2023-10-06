import matplotlib.pyplot as plt
m = 0.2
k = 10
acceleration_due_to_gravity = 9.81
weight = m * acceleration_due_to_gravity
init_displacement = 0.3
unweighted_length = 1.0
weight_displacement = weight / k
length = unweighted_length + init_displacement
dt = 0.02
duration = 3
t = 0
v = 0
iteration = int(duration / dt)
l1 = []
t1 = []
for i in range(iteration):
    restoring_spring_force = -k * (length - unweighted_length)
    acceleration = (weight_displacement + restoring_spring_force) / m
    v += acceleration * dt
    length += v * dt
    t = i * dt
    l1.append(length)
    t1.append(t)
plt.plot(t1, l1)
plt.xlabel('Time (s)')
plt.ylabel('Length of Spring (m)')
plt.title('Spring Oscillation with Attached Mass')
plt.grid(True)
plt.show()