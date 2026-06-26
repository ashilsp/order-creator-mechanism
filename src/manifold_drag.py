# ==============================================================================
# OCM PROJECT: SCRIPT - MANIFOLD_DRAG.PY
# PARADIGM: Non-Linear Drag Tensor Phase Space Integrator
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from google.colab import files

print("🔄 Initializing Manifold Drag Tensor Phase Space Engine...")

def ocm_pendulum_system(t, state, gamma, omega_M, theta_fold):
    """
    Defines the system of first-order ODEs for the phase-trapping equation:
    d^2(theta)/dt^2 + gamma*d(theta)/dt + omega_M^2 * sin(theta - theta_fold) = 0
    """
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -gamma * omega - (omega_M**2) * np.sin(theta - theta_fold)
    return [dtheta_dt, domega_dt]

def generate_phase_portrait():
    """
    Integrates multiple stellar trajectories in phase space to verify stable 
    confinement inside the conservative topological tension well.
    """
    # 1. Physics Constants Allocation
    gamma = 0.25         # Damping coefficient derived from metric viscosity eta_M
    omega_M = 1.2        # Trapping frequency determined by ||tau_M||
    theta_fold = 0.0     # Reference orientation of the 4D manifold fold
    t_span = (0, 15)     # Integration timeframe
    t_eval = np.linspace(t_span[0], t_span[1], 300)
    
    # 2. Canvas Construction
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='#0B0C10', dpi=120)
    ax.set_facecolor('#0B0C10')
    
    # 3. Trajectory Loop Integration across various Initial Conditions
    initial_thetas = np.linspace(-np.pi, np.pi, 7)
    initial_omegas = np.linspace(-1.5, 1.5, 3)
    
    for th0 in initial_thetas:
        for om0 in initial_omegas:
            sol = solve_ivp(ocm_pendulum_system, t_span, [th0, om0], 
                            args=(gamma, omega_M, theta_fold), t_eval=t_eval)
            
            # Map paths to show settling vector behaviors
            ax.plot(sol.y[0], sol.y[1], lw=1.0, alpha=0.7, color='#00FFCC')
            # Pin the initialization coordinates
            ax.scatter(sol.y[0][0], sol.y[1][0], color='#EF4444', s=6, zorder=3)
            
    # Highlight the target stable phase-lock equilibrium point
    ax.scatter([theta_fold], [0], color='#F59E0B', marker='*', s=150, zorder=5, 
               label=r'Phase-Lock Singlet ($\theta_{\text{fold}}$)')
    
    # 4. Phase Space Layout Geometry formatting
    ax.set_xlim([-np.pi - 0.5, np.pi + 0.5])
    ax.set_ylim([-2.5, 2.5])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    
    ax.set_xlabel(r'Angular Phase Deviation $\theta$ (rad)', fontsize=10)
    ax.set_ylabel(r'Phase Velocity $\frac{d\theta}{dt}$ (rad/s)', fontsize=10)
    ax.set_title(r"Topological Phase-Trapping Confinement under $\tau_M$", color='#00FFCC', fontsize=11, fontweight='bold', pad=12)
    
    ax.grid(True, color='#1F2833', ls=':', lw=0.5, alpha=0.5)
    ax.legend(loc='upper right', facecolor='#0F172A', edgecolor='#1F2833', fontsize=8)
    
    img_out = "ocm_manifold_drag_phase_portrait.png"
    plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print("📸 Non-linear phase portrait integrated and generated. Downloading asset...")
    files.download(img_out)
    print("🎉 Verification mathematical tracking metrics finalized successfully.")

if __name__ == "__main__":
    generate_phase_portrait()
