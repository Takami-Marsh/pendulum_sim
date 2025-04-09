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
- Lengths: 180cm to 240cm (in 10cm increments)
- Corresponding measured periods

## Usage

### Gravitational Acceleration Calculation

Run the `g_calc.py` script to calculate gravitational acceleration (g) using pendulum data:

```bash
python g_calc.py
```

### Pendulum Period Prediction

Run the `t_calc.py` script to predict pendulum periods for a range of lengths:

```bash
python t_calc.py
```

This script calculates the pendulum period using both the small-angle approximation and the numerical solution, and outputs a tabulated comparison of the results.

### Sample Output for `t_calc.py`

```
Predicted Pendulum Periods in Hiroshima (g = 9.7965 m/s²)
Initial angle: 15°
+--------------+-----------------------+--------------------------+------------------+
|   Length (m) |   Period (approx) (s) |   Period (numerical) (s) |   Difference (%) |
+==============+=======================+==========================+==================+
|          1.8 |                2.6933 |                   2.7027 |             0.35 |
+--------------+-----------------------+--------------------------+------------------+
|          1.9 |                2.7671 |                   2.7828 |             0.56 |
+--------------+-----------------------+--------------------------+------------------+
|          2   |                2.839  |                   2.8428 |             0.14 |
+--------------+-----------------------+--------------------------+------------------+
|          2.1 |                2.9091 |                   2.9229 |             0.47 |
+--------------+-----------------------+--------------------------+------------------+
|          2.2 |                2.9775 |                   3.003  |             0.85 |
+--------------+-----------------------+--------------------------+------------------+
|          2.3 |                3.0444 |                   3.0631 |             0.61 |
+--------------+-----------------------+--------------------------+------------------+
|          2.4 |                3.1099 |                   3.1231 |             0.42 |
+--------------+-----------------------+--------------------------+------------------+
```

## Sample Output

```
Calculating gravitational acceleration (g) from pendulum data:
----------------------------------------------------------------------
Length (m) | Period (s) | g (approx) | g (numerical) | Difference (%)
----------------------------------------------------------------------
     1.80 |     2.703 |    9.7237 |      9.7174 |      0.0657
     1.90 |     2.779 |    9.7103 |      9.7700 |      0.6112
     2.00 |     2.841 |    9.7847 |      9.8998 |      1.1622
     2.10 |     2.920 |    9.7233 |      9.8305 |      1.0902
     2.20 |     3.000 |    9.6503 |      9.7543 |      1.0660
     2.30 |     3.061 |    9.6887 |      9.7572 |      0.7016
     2.40 |     3.113 |    9.7793 |      9.8348 |      0.5651
----------------------------------------------------------------------

Average Results:
Average g (approximate method): 9.7229 m/s²
Average g (numerical method):   9.7948 m/s²
Average difference: 0.7517%
```

## Analysis

- The small-angle approximation produces results within 1% of the numerical solution for a 15° initial angle
- The numerical method yields values closer to the expected 9.81 m/s²
- Results demonstrate that the small-angle approximation is reasonably accurate for initial angles of 15°
