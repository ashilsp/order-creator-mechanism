# ==============================================================================
# OCM PROJECT: SCRIPT - FILAMENT_TENSION.PY
# PARADIGM: Numerical Evaluation of Linear Filament Tension (T_M) 
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("🔄 Initializing Manifold Filament Tension Evaluation Engine...")

def compute_filament_profile():
    """
    Evaluates the total geometric tension T_M along a localized manifold seam 
    by integrating the squared curl of the field vector potential over length L.
    """
    # 1. Parameterize the Seam Domain between Nodes
    L = 10.0  # Normalized distance between stellar node anchors (e.g., parsec scales)
    points = 500
    ell = np.linspace(0, L, points)
    dl = ell[1] - ell[0]
    
    # 2. Assign Spatial Manifold Viscosity profile (peaks near the anchor cores)
    eta_base = 0.05
    eta_M = eta_base * (np.sin(np.pi * ell / L)**2 + 0.2)
    
    # 3. Model the Harmonic Wavefield Curl: (Nabla x Psi_kappa)
    # The field oscillates based on high-frequency nodal family harmonics
    harmonic_freq = 3.0 * np.pi / L
    curl_psi = np.sin(harmonic_freq * ell) * np.exp(-0.1 * ell)
    
    # 4. Integrate Integrand: eta_M * (Nabla x Psi_kappa)^2 * dl
    integrand = eta_M * (curl_psi**2)
    cumulative_tension = np.cumsum(integrand) * dl
    total_T_M = cumulative_tension[-1]
    
    # --- Canvas Generation ---
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), facecolor='#0B0C10', dpi=120)
    
    # Top Panel: Geometric Metric Fields along Filament
    ax1.set_facecolor('#0B0C10')
    ax1.plot(ell, eta_M, color='#A855F7', lw=2, label=r'Viscosity Intensity ($\eta_M$)')
    ax1.plot(ell, curl_psi, color='#06B6D4', lw=1.5, ls='--', label=r'Field Wave Component ($\nabla \times \mathbf{\Psi}_\kappa$)')
    ax1.set_ylabel('Field Amplitudes', fontsize=9)
    ax1.set_title(r"Micro-Structural Fields Across Manifold Seam ($L={}$)".format(L), color='#A855F7', fontsize=10, fontweight='bold')
    ax1.grid(True, color='#1F2833', ls=':', lw=0.5)
    ax1.legend(loc='upper right', facecolor='#0F172A', edgecolor='#1F2833', fontsize=8)
    ax1.set_xticklabels([])
    
    # Bottom Panel: Cumulative Tension Build Up
    ax2.set_facecolor('#0B0C10')
    ax2.plot(ell, cumulative_tension, color='#F59E0B', lw=2.5, label=r'Accumulated Tension ($\mathcal{T}_M$)')
    ax2.fill_between(ell, cumulative_tension, color='#F59E0B', alpha=0.15)
    ax2.set_xlabel('Filament Axis Position Step ($\ell$)', fontsize=9)
    ax2.set_ylabel(r'Tension $\mathcal{T}_M$', fontsize=9)
    ax2.grid(True, color='#1F2833', ls=':', lw=0.5)
    
    # Highlight final integrated yield
    ax2.text(0.5 * L, 0.3 * total_T_M, f"Total Filament Tension:\n{total_T_M:.4f} Energy Units", 
             color='#FFFFFF', weight='bold', bbox=dict(facecolor='#0F172A', edgecolor='#F59E0B', boxstyle='round,pad=0.5'), ha='center')
    
    plt.suptitle("Beads-on-a-String Structural Tension Verification", color='#FFFFFF', fontsize=12, fontweight='bold', y=0.97)
    
    img_out = "ocm_filament_tension_profile.png"
    plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print(f"📸 Tension integration calculation complete (T_M = {total_T_M:.5f}). Downloading plot asset...")
    files.download(img_out)
    print("🎉 Verification asset exported cleanly to workspace context.")

if __name__ == "__main__":
    compute_filament_profile()
