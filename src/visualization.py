import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.geometry import get_rd_boundary

def render_movie_s2(output_path="movie_s2_sequestration.mp4", fps=25, duration=18):
    frames_phase = int(fps * (duration / 3))
    total_frames = frames_phase * 3
    fig, ax = plt.subplots(figsize=(8, 8.5), facecolor='black')
    ax.set_facecolor('black')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4.5, 4)
    ax.axis('off')
    
    r_s = 1.0
    r_d = get_rd_boundary(r_s)
    num_feedstock = 32
    angles = np.linspace(0, 2*np.pi, num_feedstock, endpoint=False)
    radii = np.full(num_feedstock, 3.8)
    speeds = np.random.uniform(0.02, 0.04, num_feedstock)
    
    horizon_circle = plt.Circle((0, 0), r_s, color='#111111', ec='white', lw=2, alpha=0, zorder=5)
    rd_circle = plt.Circle((0, 0), r_d, color='#3498DB', ls='--', lw=2.5, fill=False, alpha=0, zorder=2)
    ax.add_patch(horizon_circle)
    ax.add_patch(rd_circle)
    particles, = ax.plot([], [], 'o', color='#EC7063', markersize=5, zorder=4)
    title_text = ax.text(-3.8, 3.6, "", color='white', fontsize=14, fontweight='bold')
    math_text = ax.text(1.2, 3.4, "", color='#3498DB', fontsize=11, fontweight='bold', family='monospace', va='top')
    desc_text = ax.text(-3.8, -3.6, "", color='#BDC3C7', fontsize=9.5, style='italic', wrap=True, va='top',
                        bbox=dict(facecolor='#111111', alpha=0.8, edgecolor='#222222', boxstyle='round,pad=0.5'))
    
    def update(frame):
        nonlocal radii
        x_p, y_p = [], []
        if frame < frames_phase:
            title_text.set_text("a) Nodal Center Baseline")
            desc_text.set_text("Establishing the central non-singular node horizon ($r_s$). The baseline surface area geometry is defined traditionally via $A = 4\\pi r_s^2$.")
            t1 = frame / frames_phase
            horizon_circle.set_alpha(min(1.0, t1 * 2))
            math_text.set_text("AREA METRICS:\\n" + r"$A_{horizon} = 1.0\\ A$")
        elif frames_phase <= frame < frames_phase * 2:
            title_text.set_text("b) OCM Injection Boundary Expansion")
            desc_text.set_text("The Order Creator Mechanism projects the metric interface boundary to $R_d = \\sqrt{5}r_s$. The functional surface area expands quadratically by an exact factor of 5.")
            t2 = (frame - frames_phase) / frames_phase
            rd_circle.set_alpha(min(1.0, t2 * 2))
            current_area = 1.0 + (4.0 * t2)
            math_text.set_text(f"AREA METRICS:\\n$A_{{R_d}} = {current_area:.2f}\\ A$\\n$\\equiv 5 \\times A_{{horizon}}$")
        else:
            title_text.set_text("c) Laminar Mass Sequestration Process")
            desc_text.set_text("Baryonic feedstock crossing the $R_d$ boundary undergoes severe vacuum polarization, removing its electromagnetic interaction profile. Matter is sequestered at a clean 5:1 ratio.")
            horizon_circle.set_alpha(1.0)
            rd_circle.set_alpha(1.0)
            math_text.set_text("AREA METRICS:\\n" + r"$A_{R_d} = 5.0\\ A_{horiz}$" + "\\n\\n" + r"LIMIT SOLUTION:" + "\\n" + r"$\\mathbf{\\Omega_{DM} \\equiv 5\\Omega_b}$")
            for i in range(num_feedstock):
                radii[i] -= speeds[i]
                if radii[i] <= r_s: radii[i] = 3.8
                x_p.append(radii[i] * np.cos(angles[i]))
                y_p.append(radii[i] * np.sin(angles[i]))
            particles.set_data(x_p, y_p)
            colors = ['#58D68D' if r <= r_d else '#EC7063' for r in radii]
            particles.set_color(colors[0])
        return [horizon_circle, rd_circle, particles, title_text, math_text, desc_text]

    ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True)
    ani.save(output_path, writer='ffmpeg', fps=fps, bitrate=2000)
    plt.close()

def render_movie_s3(output_path="movie_s3_vacuum_dilution.mp4", fps=25, duration=12):
    total_frames = fps * duration
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5), facecolor='black')
    plt.subplots_adjust(wspace=0.25)
    for ax in [ax1, ax2]:
        ax.set_facecolor('black')
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.axis('off')
        
    r_s_stellar = 0.4
    r_s_smbh = 2.0
    ax1.add_patch(plt.Circle((0, 0), r_s_stellar, color='#111111', ec='white', lw=1.5))
    ax2.add_patch(plt.Circle((0, 0), r_s_smbh, color='#111111', ec='white', lw=1.5))
    ax1.text(-3.8, 3.6, "a) Stellar-Mass Node ($M_{\\odot}$)", color='white', fontsize=14, fontweight='bold')
    ax1.text(-3.8, 3.2, "Micro-Scale: High Tension", color='#EC7063', fontsize=11, style='italic')
    ax2.text(-3.8, 3.6, "b) Supermassive Node ($10^9\\ M_{\\odot}$)", color='white', fontsize=14, fontweight='bold')
    ax2.text(-3.8, 3.2, "Macro-Scale: Geometric Dilution", color='#A569BD', fontsize=11, style='italic')
    
    box_stellar = ax1.text(0.2, -3.6, "", color='white', fontsize=10, family='monospace', va='bottom',
                            bbox=dict(facecolor='#111111', alpha=0.8, edgecolor='#EC7063', boxstyle='round,pad=0.4'))
    box_smbh = ax2.text(0.2, -3.6, "", color='white', fontsize=10, family='monospace', va='bottom',
                        bbox=dict(facecolor='#111111', alpha=0.8, edgecolor='#A569BD', boxstyle='round,pad=0.4'))
    
    stellar_arrows, smbh_arrows = [], []
    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    for theta in angles:
        line_st, = ax1.plot([], [], color='#EC7063', lw=2, alpha=0.9)
        stellar_arrows.append((line_st, theta))
        line_sm, = ax2.plot([], [], color='#A569BD', lw=1, alpha=0.2)
        smbh_arrows.append((line_sm, theta))
        
    def update(frame):
        artists = []
        pulse = 1.0 + 0.15 * np.sin(frame * 0.15)
        for line, theta in stellar_arrows:
            line.set_data([(r_s_stellar + 0.1) * np.cos(theta), (r_s_stellar + 1.2 * pulse) * np.cos(theta)],
                          [(r_s_stellar + 0.1) * np.sin(theta), (r_s_stellar + 1.2 * pulse) * np.sin(theta)])
            artists.append(line)
        box_stellar.set_text("LOCAL METRIC STATE:\\n" + r"$\\kappa \\propto 1 / r_s^4 \\to \\mathbf{{MAX}}$" + "\\n" + r"$\\rho_{{vac}} \\approx 10^{{111}}\\text{{ kg/m}}^3$")
        artists.append(box_stellar)
        for line, theta in smbh_arrows:
            line.set_data([(r_s_smbh + 0.1) * np.cos(theta), (r_s_smbh + 0.6 * pulse) * np.cos(theta)],
                          [(r_s_smbh + 0.1) * np.sin(theta), (r_s_smbh + 0.6 * pulse) * np.sin(theta)])
            artists.append(line)
        box_smbh.set_text("DILUTED GLOBAL STATE:\\n" + r"$\\kappa \\to 1 / (2.0)^4 \\to \\mathbf{{MIN}}$" + "\\n" + r"$\\rho_{\\Lambda} \\approx 10^{{-27}}\\text{{ kg/m}}^3$")
        artists.append(box_smbh)
        return artists

    ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True)
    ani.save(output_path, writer='ffmpeg', fps=fps, bitrate=2000)
    plt.close()
