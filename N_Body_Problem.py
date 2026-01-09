import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 1.0
dt = 0.01
N = 1000
softening = 0.1

np.random.seed(42)

r = np.random.rayleigh(1.0, N)
theta = np.random.uniform(0, 2*np.pi, N)
phi = np.arccos(np.random.uniform(-1, 1, N))

x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

positions = np.column_stack((x, y, z))

velocities = np.zeros((N, 3))
for i in range(N):
    r_vec = positions[i]
    r_mag = np.linalg.norm(r_vec)
    if r_mag > 0:
        v_circ = 0.5 * np.sqrt(G * N / r_mag)
        perp = np.cross(r_vec, [0, 0, 1])
        if np.linalg.norm(perp) < 1e-8:
            perp = np.cross(r_vec, [0, 1, 0])
        perp /= np.linalg.norm(perp)
        velocities[i] = v_circ * perp

velocities += np.random.normal(0, 0.1, (N, 3))

masses = np.ones(N)

def compute_accelerations(pos):
    acc = np.zeros_like(pos)
    for i in range(N):
        r = pos - pos[i]
        dist2 = np.sum(r**2, axis=1) + softening**2
        inv_dist3 = dist2 ** (-1.5)
        inv_dist3[i] = 0.0 
        acc[i] = G * np.sum(masses[:, None] * r * inv_dist3[:, None], axis=0)
    return acc


fig = plt.figure(figsize=(10, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

scat = ax.scatter(
    positions[:, 0],
    positions[:, 1],
    positions[:, 2],
    c='white',
    s=1,
    alpha=0.6
)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_box_aspect([1, 1, 1])
ax.set_axis_off()

ax.text2D(
    0.5, 0.95,
    'N-Body Gravitational Simulation',
    transform=ax.transAxes,
    color='white',
    fontsize=14,
    ha='center'
)

def update(frame):
    global positions, velocities
    acc = compute_accelerations(positions)
    velocities += acc * dt
    positions += velocities * dt

    scat._offsets3d = (
        positions[:, 0],
        positions[:, 1],
        positions[:, 2]
    )
    ax.view_init(elev=20, azim=frame * 0.3)
    return scat,

ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=False)

plt.tight_layout()
plt.show()
