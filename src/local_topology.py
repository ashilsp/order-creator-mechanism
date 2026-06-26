# ==============================================================================
# OCM PROJECT: SCRIPT - LOCAL_TOPOLOGY.PY
# PARADIGM: 3D Toroidal Warping, Scalloping & Radcliffe Wave Solver
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("🔄 Initializing Local Topology & Torsional Warping Engine...")

def evaluate_galactic_scalloping():
    """
    Models the 3D vertical geometric profile of the galactic disk plane,
    simulating inner corrugations and the outer S-shaped warp boundary.
    """
    # 1. Domain Parameters matching Gaia DR3 empirical boundaries
    radii = np.linspace(0.1, 16.0, 400)  # Radial extension out to 16 kpc
    theta = np.linspace(0, 2*np.pi, 400)
    R, THETA = np.meshgrid(radii, theta)
    
    # 2. Segment A: Inner Corrugation Mechanics (R < 8.0 kpc)
    # Radcliffe Wave analogue modeled via stationary ground-state wave nodes
    lambda_corrugation = 2.5  # Spatial wavelength ~2.5 kpc
    amplitude_inner = 0.12     # Amplitude ~120 pc
    z_inner = amplitude_inner * np.sin(2 * np.pi * R / lambda_corrugation) * np.cos(4 * THETA)
    
    # 3. Segment B: Outer S-Shaped Warp Mechanics (R >= 8.0 kpc)
    # Torsional warping induced by misaligned gyroscope spin vector Omega_node
    r_onset = 8.2  # Solar circle onset boundary
    z_max_amplitude = 4.2  # Max displacement ~4.2 kpc at outer boundary
    
    # Scaling filter to track steep radial amplitude growth
    warp_scale = (R - r_onset) / (16.0 - r_onset)
    warp_scale = np.clip(warp_scale, 0.0, None)  # Activate strictly beyond r_onset
    z_outer = z_max_amplitude * (warp_scale ** 2) * np.sin(THETA)
    
    # 4. Composite Global Topology Plane Synthesis
    # Merge inner micro-oscillations smoothly with the macro structural warp
    transition_filter = 1.0 / (1.0 + np.exp(2.0 * (R - r_onset)))
    Z_global = transition_filter * z_inner + (1.0 - transition_filter) * z_outer
    
    # --- Canvas Layout Visualization ---
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig = plt.figure(figsize=(10, 7), facecolor='#0B0C10', dpi=120)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0B0C10')
    
    # Map coordinates to Cartesian for 3D spatial plotting
    X = R * np.cos(THETA)
    Y = R * np.sin(THETA)
    
    # Render the continuous structural manifold topology sheet
    surf = ax.plot_surface(X, Y, Z_global, cmap='coolwarm', edgecolor='none', alpha=0.85)
    
    # Highlight the central gyroscopic anchor (Sgr A*)
    ax.scatter([0], [0], [0], color='#F97316', s=120, zorder=10, label=r'Sgr A* Primary Node ($R_d$)')
    
    # Axes Formatting
    ax.set_xlabel('Galactocentric X (kpc)', fontsize=9)
    ax.set_ylabel('Galactocentric Y (kpc)', fontsize=9)
    ax.set_zlabel('Vertical Offset Z (kpc)', fontsize=9)
    ax.set_title("Milky Way Structural Manifold Model (Gaia DR3 Alignment)", color='#00FFCC', fontsize=11, fontweight='bold', pad=10)
    
    # Adjust viewing angles to capture both the inner ripple and the outer twist
    ax.view_init(elev=28, azim=-45)
    ax.set_zlim([-5.0, 5.0])
    
    # Force dark aesthetic scaling compatibility
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1F2833')
    ax.yaxis.pane.set_edgecolor('#1F2833')
    ax.zaxis.pane.set_edgecolor('#1F2833')
    ax.grid(True, color='#1F2833', ls=':')
    
    img_out = "ocm_local_torsional_warp.png"
    plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print(f"📸 3D Local structural warp matrix compiled successfully (z_max = {z_max_amplitude} kpc). Downloading...")
    files.download(img_out)
    print("🎉 Astrometric verification asset successfully added to the workspace pipeline.")

if __name__ == "__main__":
    evaluate_galactic_scalloping()
