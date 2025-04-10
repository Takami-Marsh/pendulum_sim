import numpy as np
from scipy.integrate import solve_ivp
from tabulate import tabulate

# Constants
g = 9.7965  # gravitational acceleration in Hiroshima (m/s²)
initial_angle = 10  # degrees

# Create array of lengths from 1.8m to 2.4m in 0.1m increments
lengths = np.arange(1.8, 2.41, 0.1)

def calculate_period_approximate(L):
    """Calculate period using the small-angle approximation formula."""
    return 2 * np.pi * np.sqrt(L/g)

def pendulum_ode(t, y, L):
    """Define the pendulum differential equation."""
    theta, omega = y
    dydt = [omega, -g/L * np.sin(theta)]
    return dydt

def calculate_period_numerical(L, theta0):
    """Calculate period using numerical solution of the full differential equation."""
    # Convert initial angle to radians
    theta0_rad = np.radians(theta0)
    
    # Initial conditions [theta, omega]
    y0 = [theta0_rad, 0]
    
    # Time span for integration
    t_span = [0, 10]
    
    # Solve ODE
    sol = solve_ivp(
        pendulum_ode, t_span, y0,
        args=(L,),
        method='RK45',
        t_eval=np.linspace(t_span[0], t_span[1], 1000),
        rtol=1e-8
    )
    
    # Find period by detecting zero crossings
    theta = sol.y[0]
    t = sol.t
    
    # Find zero crossings in same direction (full period)
    zero_crossings = np.where(np.diff(theta > 0))[0]
    if len(zero_crossings) >= 2:
        period = 2 * (t[zero_crossings[1]] - t[zero_crossings[0]])
    else:
        raise ValueError("Could not determine period from numerical solution")
    
    return period

# Calculate periods using both methods
periods_approx = []
periods_numerical = []

for L in lengths:
    T_approx = calculate_period_approximate(L)
    T_num = calculate_period_numerical(L, initial_angle)
    periods_approx.append(T_approx)
    periods_numerical.append(T_num)

# Create table data
table_data = [
    (f"{L:.1f}", f"{T_approx:.4f}", f"{T_num:.4f}", f"{abs(T_approx-T_num)/T_num*100:.2f}")
    for L, T_approx, T_num in zip(lengths, periods_approx, periods_numerical)
]

# Print the table with headers
headers = ["Length (m)", "Period (approx) (s)", "Period (numerical) (s)", "Difference (%)"]
print("\nPredicted Pendulum Periods in Hiroshima (g = 9.7965 m/s²)")
print(f"Initial angle: {initial_angle}°")
print(tabulate(table_data, headers=headers, tablefmt="grid"))
