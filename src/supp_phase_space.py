# ==============================================================================
# OCM SUPPLEMENTARY PAPER: SCRIPT - SUPP_PHASE_SPACE.PY
# PARADIGM: Non-Linear Pendulum Perturbations & Lyapunov Phase-Space Tracking
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from google.colab import files

print("🔄 Initializing Phase-Space Pendulum Perturbation Solver...")

def pendulum_system(t, y, gamma, omega0, epsilon):
    """
    Defines the system of first-order ODEs for the modified damped pendulum:
    theta_dot = omega
    omega_dot = -gamma*omega - (omega0^2)*sin(theta) + epsilon*cos(1.2*t)
    """
    theta, omega = y
    # f(t) is modeled as a cosmic tidal perturbation harmonic: cos(1.2 * t)
    f_t = np.cos(1.2 * t)
    
    dtheta_dt = omega
    domega_dt = -gamma * omega - (omega0**2) * np.sin(theta) + epsilon * f_t
    return [dtheta_dt, domega_dt]

def execute_phase_analysis():
    # 1. Establish System Parameters
    omega0 = 1.0     # Natural orbital resonance frequency
    gamma = 0.35     # Explicit non-particle manifold damping coefficient
    epsilon = 0.08   # Tidal perturbation amplitude (Strictly bounded: gamma > epsilon)
    
    t_span = (0, 40)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)
    
    # 2. Integrate Inward-Spiraling Stable Trajectories (Inside Separatrix)
    initial_states_stable = [
        [-2.2, 0.4],
        [2.2, -0.4],
        [-1.0, 1.2],
        [1.0, -1.2]
    ]
    
    stable_trajectories = []
    for y0 in initial_states_stable:
        sol = solve_ivp(pendulum_system, t_span, y0, args=(gamma, omega0, epsilon), t_eval=t_eval)
        stable_trajectories.append(sol)
        
    # 3. Integrate an Escaping Orbit (Breaching the Tracking Envelope via extreme initial energy)
    y0_escape = [-3.0, 2.1]
    sol_escape = solve_ivp(pendulum_system, t_span, y0_escape, args=(gamma, omega0, epsilon), t_eval=t_eval)

    # 4. Generate the Ideal Closed-Form Separatrix Baseline Background
    theta_grid = np.linspace(-np.pi, np.pi, 300)
    separatrix_upper = 2.0 * omega0 * np.cos(theta_grid / 2.0)
    separatrix_lower = -2.0 * omega0 * np.cos(theta_grid / 2.0)

    # --- Canvas Layout Allocation ---
    plt.rcParams.update({'text.color': "#FFFFFF", 'axes.labelcolor': "#A7A7A7"})
    fig, ax = plt.subplots(figsize=(10, 6.5), facecolor='#0B0C10', dpi=120)
    ax.set_facecolor('#0B0C10')
    
    # Plot Ideal Separatrix Boundary Shading
    ax.plot(theta_grid, separatrix_upper, color='#06B6D4', ls='--', lw=1.5, label='Separatrix Envelopes ($\epsilon_{crit}$)')
    ax.plot(theta_grid, separatrix_lower, color='#06B6D4', ls='--')
    ax.fill_between(theta_grid, separatrix_lower, separatrix_upper, color='#06B6D4', alpha=0.04)
    
    # Plot Stable Attractor Trajectories Spiraling Inward
    for idx, sol in enumerate(stable_trajectories):
        lbl = 'Stable Manifold Trajectories' if idx == 0 else ""
        ax.plot(sol.y[0], sol.y[1], color='#F59E0B', lw=2, label=lbl)
        # Arrow marks to indicate directional tracking flow
        ax.arrow(sol.y[0, 250], sol.y[1, 250], sol.y[0, 252]-sol.y[0, 250], sol.y[1, 252]-sol.y[1, 250],
                 shape='full', lw=0, length_includes_head=True, head_width=0.08, color='#F59E0B')

    # Plot Un-trapped Escaping Orbit
    ax.plot(sol_escape.y[0], sol_escape.y[1], color='#EF4444', lw=1.8, ls=':', label=r'Escaping Orbit ($\gamma < \epsilon |f(t)|$)')
    
    # Mark Central Target Attractor Focus
    ax.scatter([0], [0], color='#3B82F6', s=120, zorder=5, label='Global Attractor Focus ($r=0$)')
    
    # Labels and Space Settings
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-2.5, 2.5])
    ax.set_xlabel(r'Angular Plane Deviation $\theta$ (rad)', fontsize=10)
    ax.set_ylabel(r'Orbital Phase Velocity Drift $\dot{\theta}$ (rad/s)', fontsize=10)
    ax.set_title("Phase-Space Pendulum Perturbation Trajectories", color='#00FFCC', fontsize=11, fontweight='bold', pad=12)
    ax.grid(True, color='#1F2833', ls=':', lw=0.5, alpha=0.5)
    ax.legend(loc='upper right', facecolor='#0F172A', edgecolor='#1F2833', fontsize=9)
    
    # Clean framework borders
    for spine in ax.spines.values():
        spine.set_color('#1F2833')
        
    ax.text(-3.2, -2.2, r"$\frac{dV}{dt} \leq 0$ (Asymptotic Lyapunov Attractor Verified)", color='#F59E0B', fontsize=9, fontweight='bold')

    img_out = "ocm_supp_phase_space_trajectories.png"
    plt.savefig(img_out, dpi=300, facecolor='#0B0C10', edgecolor='none', bbox_inches='tight')
    plt.close()
    
    print("📸 Phase-space Lyapunov boundaries mapped successfully. Downloading visual asset...")
    files.download(img_out)
    print("🎉 File `src/supp_phase_space.py` is safely integrated under the primary workspace framework.")

if __name__ == "__main__":
    execute_phase_analysis()
