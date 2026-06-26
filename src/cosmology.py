# ==============================================================================
# OCM PROJECT: SCRIPT - COSMOLOGY.PY
# PARADIGM: First-Principles Dark Sector Energy Densities & Planck Calibration
# ==============================================================================

import numpy as np

def calculate_ocm_budget(omega_baryon_input=0.0493):
    """
    Computes the exact OCM cosmic energy budget parameters using rigid 
    topological constraints (eta = 5, chi = Euler's number e).
    """
    # Rigid OCM Scaling Constants
    eta = 5.0              # Area-capture efficiency limit (R_d boundary to horizon area ratio)
    chi = np.e             # Entropy-reversal efficiency scaling constant (Euler's Number)
    
    # Calculate energy densities based on first-principles identities
    omega_dm = eta * omega_baryon_input
    omega_de = chi * omega_dm
    
    omega_total = omega_baryon_input + omega_dm + omega_de
    omega_k = 1.0 - omega_total  # Residual metric deficit manifesting as curvature
    
    return {
        "Omega_b": omega_baryon_input,
        "Omega_DM": omega_dm,
        "Omega_DE": omega_de,
        "Omega_total": omega_total,
        "Omega_k": omega_k
    }

def verify_planck_residuals():
    """
    Evaluates the residual error deviations between the first-principles 
    OCM derivations and the empirical Planck 2018 CMB legacy baselines.
    """
    # Planck 2018 baseline data points (Central values)
    planck_baselines = {
        "Omega_b": 0.0493,
        "Omega_DM": 0.2645,
        "Omega_DE": 0.6847,
        "Omega_total": 0.9993
    }
    
    # Evaluate OCM state vector using the calibrated baryonic anchor
    ocm_results = calculate_ocm_budget(planck_baselines["Omega_b"])
    
    print("="*65)
    print("      OCM GEOMETRIC CALIBRATION VS PLANCK 2018 CMB BASELINES")
    print("="*65)
    print(f"{'Parameter':<15} | {'OCM Derived':<12} | {'Planck 2018':<12} | {'Residual Delta':<14}")
    print("-"*65)
    
    for key in planck_baselines.keys():
        delta = ocm_results[key] - planck_baselines[key]
        print(f"{key:<15} | {ocm_results[key]:<12.4f} | {planck_baselines[key]:<12.4f} | {delta:<+14.4f}")
        
    print("-"*65)
    print(f"Predicted Residual Metric Deficit (Open Curvature Signature Omega_k): {ocm_results['Omega_k']:.4f}")
    print("="*65)

if __name__ == "__main__":
    verify_planck_residuals()
