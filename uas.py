import numpy as np
import matplotlib.pyplot as plt

mass = 5.0  
force = 10.0  
time_step = 1.0  
total_time = 10.0  

num_steps = int(total_time / time_step)

time = np.zeros(num_steps + 1)
velocity = np.zeros(num_steps + 1)
position = np.zeros(num_steps + 1)

velocity[0] = 0.0  
position[0] = 0.0  

for i in range(num_steps):
    acceleration = force / mass
    velocity[i + 1] = velocity[i] + acceleration * time_step
    position[i + 1] = position[i] + velocity[i] * time_step
    time[i + 1] = time[i] + time_step

print("Time (s) | Velocity (m/s) | Position (m)")
for i in range(num_steps + 1):
    print(f"{time[i]:8.2f} | {velocity[i]:13.2f} | {position[i]:10.2f}")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(time, velocity, marker='o')
plt.title('Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.subplot(1, 2, 2)
plt.plot(time, position, marker='o')
plt.title('Position vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')

plt.tight_layout()
plt.show()
