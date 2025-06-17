
import math

def chs_risk(thc_mg_day: float, cb1_ratio: float, autonomic_z: float, trauma_index: int):
    """
    Calculate CHS risk probability using logistic model from Zot et al. 2025.
    """
    z = -4.3 + 0.07*thc_mg_day - 1.1*cb1_ratio + 0.03*autonomic_z + 0.9*trauma_index
    return 1 / (1 + math.exp(-z))

if __name__ == "__main__":
    print("Enter daily THC mg:")
    D = float(input().strip())
    print("Enter CB1 availability ratio (1.0 = normal control):")
    R = float(input().strip())
    print("Enter autonomic dysregulation z-score:")
    A = float(input().strip())
    print("Enter trauma shell index (0-3):")
    S = int(input().strip())
    risk = chs_risk(D, R, A, S)
    print(f"Predicted CHS probability: {risk:.2%}")
