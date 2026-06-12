import numpy as np

def get_rd_boundary(r_s):
    """Calculates the Laminar Injection Zone boundary limit (R_d = sqrt(5) * r_s)"""
    return np.sqrt(5) * r_s

def calculate_local_tension(r_s, h_bar=1.0, c=1.0):
    """Calculates the localized metric tension (kappa) from Section 2.3"""
    if r_s <= 0:
        raise ValueError("Horizon radius must be greater than zero.")
    return (h_bar * c * (np.pi ** 2)) / (720.0 * (r_s ** 4))
