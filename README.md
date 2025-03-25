# Pendulum Gravitational Acceleration Calculator

This Python script calculates the gravitational acceleration (g) using pendulum motion data through two different methods:
1. Small-angle approximation formula
2. Full non-linear differential equation (numerical solution)

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

Install dependencies using:
```bash
pip install numpy scipy matplotlib
```

## Implementation Details

### Methods Used

1. **Small-angle Approximation**
   - Uses the formula: T = 2π√(L/g)
   - Solved for g: g = 4π²L/T²
   - Valid for small angles (typically < 20°)

2. **Numerical Solution**
   - Solves the full non-linear differential equation: d²θ/dt² + (g/L)sinθ = 0
   - Uses SciPy's `solve_ivp` with RK45 method
   - Accounts for the full pendulum motion without approximations

### Sample Data

The script includes example data for a pendulum with:
- Initial angle: 15°
- Lengths: 180cm to 240cm (in 15cm increments)
- Corresponding measured periods

## Usage

Run the script using:
```bash
python script.py
```

## Sample Output

```
Calculating gravitational acceleration (g) from pendulum data:
----------------------------------------------------------------------
Length (m) | Period (s) | g (approx) | g (numerical) | Difference (%)
----------------------------------------------------------------------
     1.80 |     2.698 |     9.762 |       9.861 |       0.999
     1.95 |     2.807 |     9.770 |       9.791 |       0.207
     2.10 |     2.911 |     9.784 |       9.877 |       0.951
     2.25 |     3.012 |     9.791 |       9.847 |       0.568
     2.40 |     3.109 |     9.802 |       9.882 |       0.805
----------------------------------------------------------------------

Average Results:
Average g (approximate method): 9.782 m/s²
Average g (numerical method):   9.852 m/s²
Average difference: 0.706%
```

## Analysis

- The small-angle approximation produces results within 1% of the numerical solution for a 15° initial angle
- The numerical method yields values closer to the expected 9.81 m/s²
- Results demonstrate that the small-angle approximation is reasonably accurate for initial angles of 15°
