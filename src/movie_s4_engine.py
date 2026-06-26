# ==============================================================================
# OCM SUPPLEMENTAL PROJECT: MOVIE S4 — GALACTIC ROTATION AND MANIFOLD VISCOSITY
# PARADIGM: Geometric Mechanical Tethering vs. Particle Dark Matter Halos
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from google.colab import files
import time

print("🔄 Initializing OCM Movie S4 Galactic Kinematics Simulator...")
!apt-get install -y ffmpeg

# --- 1. CONFIGURATION & DISK ORBITAL PROPERTIES ---
np.random.seed(42)
num_stars = 400
frames_total = 200

# Orbit allocations within standard galactic disk constraints
star_radii = np.random.uniform(0.6, 6.0, num_stars)
star_angles = np.random.uniform(0, 2*np.pi, num_stars)

# Apply OCM velocity curves to build stable initial conditions
G_m = 2.0
core_mass = 1.5
eta_m_coef = 0.04
omega_core = 0.7

v_squared = (G_m * core_mass) / star_radii + (eta_m_coef * omega_core * (star_radii**2))
star_speeds = np.sqrt(v_squared)

# Allocate tracking arrays
history_x = np.zeros((frames_total, num_stars))
history_y = np.zeros((frames_total, num_stars))

for f in range(frames_total):
    dt_step = 0.04
    # Propagate angles forward using custom flat velocity profiles
    star_angles += (star_speeds / star_radii) * dt_step
    history_x[f] = star_radii * np.cos(star_angles)
    history_y[f] = star_radii * np.sin(star_angles)

# --- 2. MULTI-PANEL DIAGNOSTIC CANVAS DESIGN ---
plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), facecolor='#0B0C10', dpi=110)
fig.subplots_adjust(left=0.06, right=0.94, bottom=0.12, top=0.88, wspace=0.2)

# Panel A Handles: Particle Kinematics Trackers
ax1.set_facecolor('#0B0C10')
ax1.set_xlim([-6.5, 6.5])
ax1.set_ylim([-6.5, 6.5])
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("Panel A: Baryonic Particle Kinematics ($v(r)$ Plateau)", color='#FF8C00', fontsize=11, fontweight='bold', pad=12)
star_scatter = ax1.scatter([], [], color='#00FFFF', s=6, alpha=0.7, zorder=3)
ax1.scatter([0], [0], color='#F97316', s=90, edgecolors='#FFFFFF', zorder=4) # Core node R_d anchor

# Panel B Handles: Underline Manifold Stress Topography
ax2.set_facecolor('#0B0C10')
ax2.set_xlim([-6.5, 6.5])
ax2.set_ylim([-6.5, 6.5])
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title(r"Panel B: Spacetime Metric Stress Topology ($\tau_M$)", color='#A855F7', fontsize=11, fontweight='bold', pad=12)

grid_pts = np.linspace(-6.5, 6.5, 100)
X_g, Y_g = np.meshgrid(grid_pts, grid_pts)
R_g = np.sqrt(X_g**2 + Y_g**2) + 0.1
# Stiffening matrix background footprint
stress_field = eta_m_coef * omega_core * (R_g**1.5)
stress_contour = ax2.imshow(stress_field, cmap='magma', extent=[-6.5, 6.5, -6.5, 6.5], origin='lower', alpha=0.85)

fig.text(0.5, 0.04, r"Supplemental Movie S4: Multi-scale rotation tracking showing flat velocity plateaus caused by mechanical manifold stiffening.", 
         ha='center', fontsize=10, style='italic', color='#8A95A5')

# --- 3. RENDERING STEP ANIMATION ENGINE ---
def update_frames(frame):
    # Map coordinates across the step array
    star_scatter.set_offsets(np.c_[history_x[frame], history_y[frame]])
    
    # Introduce localized dynamic metric pulsation to show rotating field lines
    pulsed_stress = stress_field * (1.0 + 0.05 * np.sin(frame * 0.15))
    stress_contour.set_data(pulsed_stress)
    return [star_scatter, stress_contour]

# Save snapshot image at frame 100 for code verification
print("📸 Compiling 300 DPI structural snapshot at mid-rotation run...")
update_frames(100)
img_out = "ocm_rotation_curve_stiffening_snapshot.png"
plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')

# Run encoding compilation
print("🎬 Encoding 200-frame macro-galactic dynamics video (MP4, 25 FPS)...")
ani = FuncAnimation(fig, update_frames, frames=frames_total, interval=40, blit=False)
plt.close(fig)

writer = FFMpegWriter(fps=25, metadata=dict(artist='OCM Astrophysics Group'), bitrate=2500)
vid_out = "ocm_supplemental_movie4.mp4"
ani.save(vid_out, writer=writer, dpi=110)
print("✅ Movie S4 asset processing complete.")

# Trigger automated file delivery downpipes
print("\n📥 Commencing asset distribution processes...")
time.sleep(1)
files.download(img_out)
time.sleep(2)
files.download(vid_out)
print("🎉 Compilation chain completed successfully!")
