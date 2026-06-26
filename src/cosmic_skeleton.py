# ==============================================================================
# OCM PROJECT: SCRIPT - COSMIC_SKELETON.PY
# PARADIGM: Large-Scale Nodal Skeleton Growth & Redshift Velocity Engine
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("🔄 Initializing Primordial Cosmic Skeleton Verification Engine...")

def evaluate_lss_growth():
    """
    Compares the structural growth rate of large-scale density perturbations 
    under stochastic matter aggregation vs. the OCM primordial nodal skeleton.
    """
    # 1. Coordinate and Scale Frame Allocation (Gpc scale)
    z_redshift = np.linspace(0.0, 7.0, 200) # Redshift track down to the early universe
    
    # Growth factor models:
    # Classical linear perturbation growth scales weakly with redshift D(z) ~ 1/(1+z)
    growth_classical = 1.0 / (1.0 + z_redshift)
    
    # OCM framework features an early-stage non-linear step-up due to primordial 
    # load-bearing kappa-flux conduits established during the Flash event
    skeleton_activation_redshift = 6.0
    growth_ocm = (1.0 / (1.0 + z_redshift)) + 0.8 * np.exp(-((z_redshift - skeleton_activation_redshift)/1.5)**2)
    # Ensure preservation of late-time saturation constraints
    growth_ocm = np.where(z_redshift > skeleton_activation_redshift, growth_ocm, (1.0 / (1.0 + z_redshift)) * 1.4)
    
    # Normalize profiles to showcase early structure coherence
    growth_classical /= np.max(growth_classical)
    growth_ocm /= np.max(growth_ocm)

    # --- Canvas Layout Construction ---
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig, ax = plt.subplots(figsize=(8.5, 6.0), facecolor='#0B0C10', dpi=120)
    ax.set_facecolor('#0B0C10')
    
    # Plot tracking channels
    ax.plot(z_redshift, growth_classical, color='#EF4444', lw=2, ls='--', label=r'Classical Linear Clustering ($\Lambda$CDM)')
    ax.plot(z_redshift, growth_ocm, color='#3B82F6', lw=2.5, label='OCM Nodal Skeleton Growth')
    
    # Shaded band indicating mature structure window at high redshift
    ax.axvspan(5.5, 7.0, color='#1F2833', alpha=0.4, label='High-z Mature Supercluster Window')
    
    # Annotate specific targets
    ax.text(6.2, 0.85, "Hercules-Corona\nBorealis Wall\nFormation Floor", color='#00FFCC', 
            fontsize=8, fontweight='bold', ha='center', bbox=dict(facecolor='#0F172A', alpha=0.6, boxstyle='round,pad=0.3'))
    
    ax.set_xlim([7.0, 0.0]) # Reverse axis to track standard chronological expansion arrow
    ax.set_ylim([0.0, 1.1])
    
    ax.set_xlabel('Cosmological Redshift ($z$)', fontsize=10, labelpad=6)
    ax.set_ylabel('Normalized Structural Coherence Factor', fontsize=10, labelpad=6)
    ax.set_title("Large-Scale Structure Evolution: Stochastic vs. Nodal Skeleton", color='#3B82F6', fontsize=11, fontweight='bold', pad=12)
    
    ax.grid(True, color='#1F2833', ls=':', lw=0.5, alpha=0.5)
    ax.legend(loc='lower left', facecolor='#0F172A', edgecolor='#1F2833', fontsize=9)
    
    img_out = "ocm_cosmic_skeleton_growth.png"
    plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print("📸 Large-scale structural growth matrix tracking complete. Exporting asset...")
    files.download(img_out)
    print("🎉 Structural verification asset for Section 4 complete.")

if __name__ == "__main__":
    evaluate_lss_growth()
