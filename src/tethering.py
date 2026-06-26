# ==============================================================================
# OCM PROJECT: SCRIPT - TETHERING.PY
# PARADIGM: Manifold Drag Tensor (Tau_M) & Phase-Trapping Simulation Engine
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("🔄 Initializing Topological Tethering Validation Engine...")

def simulate_phase_trapping():
    """
    Simulates and compares angular phase-smearing under classical differential 
    shear vs. OCM phase-trapping governed by the Manifold Drag Tensor (Tau_M).
    """
    np.random.seed(101)
    num_test_points = 150
    radii = np.linspace(0.5, 5.0, num_test_points)
    initial_angles = np.zeros(num_test_points)  # Start as a perfectly straight radial arm
    
    # Time parameters (simulate over a few typical galactic rotational periods)
    t_final = 5.0
    dt = 0.05
    steps = int(t_final / dt)
    
    # Mode 1: Classical Differential Shear (v = constant, omega propto 1/r)
    angles_classical = initial_angles.copy()
    v_constant = 1.5
    omega_classical = v_constant / radii
    
    # Mode 2: OCM Phase-Trapping (Tau_M forces angular phase coherence)
    angles_ocm = initial_angles.copy()
    # The Manifold Drag Tensor locks the outer regions to a coherent pattern speed
    omega_pattern = 0.6 
    
    # Propagate through time
    for _ in range(steps):
        # Classical continues to shear unchecked
        angles_classical += omega_classical * dt
        
        # OCM phase-trapping dampens the velocity shear, relaxing to omega_pattern
        # Relaxation scaling tracks the localized metric stiffness
        stiffness_factor = 1.0 - np.exp(-radii / 2.0)
        omega_eff = (1.0 - stiffness_factor) * omega_classical + stiffness_factor * omega_pattern
        angles_ocm += omega_eff * dt

    # --- Plotting the Asset Generation ---
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), facecolor='#0B0C10', dpi=120)
    
    # Left Panel: Classical Phase Smearing
    ax1.set_facecolor('#0B0C10')
    x_class = radii * np.cos(angles_classical)
    y_class = radii * np.sin(angles_classical)
    ax1.scatter(x_class, y_class, c='#EF4444', s=15, alpha=0.8, label='Sheared Stars')
    ax1.plot(x_class, y_class, color='#EF4444', lw=1, alpha=0.4)
    ax1.set_title("Panel A: Classical Differential Shear", color='#EF4444', fontsize=10, fontweight='bold')
    ax1.set_xlim([-5.5, 5.5])
    ax1.set_ylim([-5.5, 5.5])
    ax1.set_aspect('equal')
    ax1.grid(True, color='#1F2833', ls=':', lw=0.5)
    
    # Right Panel: OCM Topological Tethering
    ax2.set_facecolor('#0B0C10')
    x_ocm = radii * np.cos(angles_ocm)
    y_ocm = radii * np.sin(angles_ocm)
    ax2.scatter(x_ocm, y_ocm, c='#06B6D4', s=15, alpha=0.8, label='Tethered Stars')
    ax2.plot(x_ocm, y_ocm, color='#06B6D4', lw=1.5, alpha=0.5)
    ax2.scatter([0], [0], color='#F97316', s=50, label=r'$R_d$ Anchor')  # Core Node
    ax2.set_title("Panel B: OCM Phase-Trapping Permanence", color='#06B6D4', fontsize=10, fontweight='bold')
    ax2.set_xlim([-5.5, 5.5])
    ax2.set_ylim([-5.5, 5.5])
    ax2.set_aspect('equal')
    ax2.grid(True, color='#1F2833', ls=':', lw=0.5)
    ax2.legend(loc='upper right', facecolor='#0F172A', edgecolor='#1F2833', fontsize=8)

    plt.suptitle("Galactic Structural Stabilization Mapped via Manifold Drag", color='#FFFFFF', fontsize=12, fontweight='bold', y=0.98)
    img_name = "ocm_tethering_phase_lock.png"
    plt.savefig(img_name, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print("📸 Analytical tethering plot generated successfully. Downloading...")
    files.download(img_name)

if __name__ == "__main__":
    simulate_phase_trapping()
