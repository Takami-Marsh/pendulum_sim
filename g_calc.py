import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Experimental data (example values)
# Length (m), Period (s) for pendulum with 15° initial angle
data = [
    (1.80, 2.698),  # 180 cm
    (1.90, 2.768),  # 190 cm
    (2.00, 2.839),  # 200 cm
    (2.10, 2.911),  # 210 cm
    (2.20, 2.978),  # 220 cm
    (2.30, 3.044),  # 230 cm
    (2.40, 3.109)   # 240 cm
]

def calculate_g_approximate(L, T):
    """Calculate g using the small-angle approximation formula."""
    return 4 * np.pi**2 * L / (T**2)

def pendulum_ode(t, y, L, g_test):
    """Define the pendulum differential equation."""
    theta, omega = y
    dydt = [omega, -g_test/L * np.sin(theta)]
    return dydt

def find_period_numerical(L, theta0):
    """
    Find the period using numerical solution of the full differential equation.
    
    Args:
        L (float): Length of pendulum in meters
        theta0 (float): Initial angle in degrees
    
    Returns:
        float: Period of oscillation in seconds
    """
    # Convert initial angle to radians
    theta0_rad = np.radians(theta0)
    
    # Initial conditions [theta, omega]
    y0 = [theta0_rad, 0]
    
    # Time span for integration (adjust if needed)
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

def calculate_g_numerical(L, T_exp, theta0):
    """
    Calculate g using the full differential equation by adjusting g until
    the numerical period matches the experimental period.
    """
    # Initial guess for g
    g_approx = calculate_g_approximate(L, T_exp)
    
    def find_period_with_g(g_test):
        """Helper function to find period with a test value of g."""
        def pendulum_ode_with_g(t, y):
            theta, omega = y
            dydt = [omega, -g_test/L * np.sin(theta)]
            return dydt
        
        # Initial conditions [theta, omega]
        y0 = [np.radians(theta0), 0]
        
        # Solve ODE
        sol = solve_ivp(
            pendulum_ode_with_g,
            [0, 10],
            y0,
            method='RK45',
            t_eval=np.linspace(0, 10, 1000),
            rtol=1e-8
        )
        
        # Find period
        theta = sol.y[0]
        t = sol.t
        zero_crossings = np.where(np.diff(theta > 0))[0]
        if len(zero_crossings) >= 2:
            return 2 * (t[zero_crossings[1]] - t[zero_crossings[0]])
        else:
            return float('inf')
    
    # Binary search to find g that gives the experimental period
    g_min, g_max = 9.0, 10.0
    tolerance = 1e-6
    
    while g_max - g_min > tolerance:
        g_test = (g_min + g_max) / 2
        T_test = find_period_with_g(g_test)
        
        if T_test > T_exp:
            g_min = g_test
        else:
            g_max = g_test
    
    return (g_min + g_max) / 2

# Calculate g using both methods for each data point
initial_angle = 15  # degrees
results = []

print("\nCalculating gravitational acceleration (g) from pendulum data:")
print("-" * 70)
print("Length (m) | Period (s) | g (approx) | g (numerical) | Difference (%)")
print("-" * 70)

for L, T in data:
    # Calculate g using both methods
    g_approx = calculate_g_approximate(L, T)
    g_num = calculate_g_numerical(L, T, initial_angle)
    
    # Calculate percentage difference
    diff_percent = abs(g_approx - g_num) / g_num * 100
    
    results.append((L, T, g_approx, g_num, diff_percent))
    
    # Print results
    print(f"{L:9.2f} | {T:9.3f} | {g_approx:9.3f} | {g_num:11.3f} | {diff_percent:11.3f}")

print("-" * 70)

# Calculate averages
avg_g_approx = np.mean([r[2] for r in results])
avg_g_num = np.mean([r[3] for r in results])
avg_diff = np.mean([r[4] for r in results])

print(f"\nAverage Results:")
print(f"Average g (approximate method): {avg_g_approx:.3f} m/s²")
print(f"Average g (numerical method):   {avg_g_num:.3f} m/s²")
print(f"Average difference: {avg_diff:.3f}%")
