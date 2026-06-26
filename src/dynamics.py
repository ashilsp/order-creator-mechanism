# ==============================================================================
# OCM PROJECT: SCRIPT - DYNAMICS.PY
# PARADIGM: Non-Particle Galactic Rotation Profile Calculator
# ==============================================================================

import numpy as np

def calculate_rotation_profile(radius, mode="milky_way"):
    """
    Calculates orbital velocities v(r) using the OCM Viscous Tension Equation:
    v(r) = sqrt( (G * M) / r  +  (eta_M * Omega * r^2) / m )
    """
    # Baseline constant allocations
    G_baryonic = 1.5
    
    if mode == "m87":
        # Saturated, high-capacity active core configuration
        mass_core = 5.0
        eta_m = 0.08
        omega = 1.2
    elif mode == "milky_way":
        # Standard balanced baseline galaxy profile
        mass_core = 2.0
        eta_m = 0.03
        omega = 0.8
    elif mode == "df2":
        # Dormant node profile: zero viscosity coefficient (pure Keplerian drop)
        mass_core = 3.5
        eta_m = 0.00
        omega = 0.0
    else:
        raise ValueError("Unknown galactic system mode configuration profile.")
        
    # Compute component tracks
    newtonian_term = (G_baryonic * mass_core) / radius
    viscous_term = (eta_m * omega * (radius**2))
    
    velocity = np.sqrt(newtonian_term + viscous_term)
    return velocity, newtonian_term, viscous_term
