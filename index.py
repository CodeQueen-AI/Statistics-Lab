# Import
import numpy as np
from scipy.stats import norm, t

# Find Critical Value
def t_critical(df, alpha=0.5, tail='two'):
    if tail == 'two':
        alpha = alpha / 2
        critical_value = t.ppf(1-alpha, df)
        critical_value_2 = - critical_value
        return (critical_value, critical_value_2)
    elif tail == 'right':
        critical_value = t.ppf(1-alpha, df)
        return critical_value
    elif tail == 'left':
        critical_value = t.ppf(alpha, df)
        return critical_value
    else:
        print("Tail must be 'two', 'right', or'left'")
        
print("T right-tailed(df=24, alpha=0.05):", t_critical(24, 0.05, "right"))
print("T two-tailed (df=9, alpha=0.05):", t_critical(9, 0.05, "two"))
print("T two-tailed (df=9, alpha=0.05):", t_critical(9, 0.05, "left"))
print("T two-tailed (df=9, alpha=0.05):", t_critical(9, 0.05, "three"))
print("T two-tailed (df=9, alpha=0.05):", t_critical(9))

# z-critical value
def z_critical(tail, alpha = 0.05):
  if tail == "two":
    alpha = alpha /2
    critical_value = norm.ppf(1-alpha)
    critical_value_2 = - critical_value
    return (critical_value, critical_value_2)
  elif tail == "left":
    alpha = alpha
    critical_value = norm.ppf(alpha)
    return critical_value
  elif tail == "right":
    alpha = 1 - alpha
    critical_value = norm.ppf(alpha)
    return critical_value
  else:
    print("tail must be 'two', 'right', or 'left'")
    
print("Z two-tailed (alpha=0.05):", z_critical("two",0.05))
print("Z right-tailed (alpha=0.05):", z_critical("right",0.05))
print("Z left-tailed (alpha=0.05):", z_critical("left",0.05))


# z-test_steps
def z_test_steps(mu0, xbar, sigma, n, alpha=0.05, tail='left'):
    
    # Step1 - Hypothesis
    print('STEP 1:')
    print("HO: mu0 = ", mu0)
    if tail == "two":
        print("H1: mu0 != ", mu0)
    elif tail == "right":
        print('H1: mu0 > ', mu0)
    elif tail == "left":
        print('H1: mu0 < ', mu0)
    else:
        print('Incorrect of value of tail!')
    
    # Step 2 - Type of Test
    print('STEP 2')
    if tail == 'two':
        print('Type of Test: Two tailwd test')
    elif tail == 'right': 
        print('Type of Test: Right tailed test')
    elif tail == 'left':
        print('Type of Test: Left tailed test')
    else:
        print('Incorrect value of tail')
    
    # Step 3 - Parameters
    print('STEP 3')
    print("n = ", n)
    print("xbar = ", xbar)
    print("sigma = ", sigma)
    print("alpha = ", alpha )
    
    # Step 4 - Z Test Calculation
    print('STEP 4')
    print('Z test = (xbar - mu0) / (sigma / sqrt(n))')
    z = (xbar - mu0) / (sigma/ np.sqrt(n))
    print(f"Z test = ({xbar} - {mu0}) / ({sigma} / sqrt({n}))")
    print("z =" , z)

    # Step 5: Critical Value + Decision (USING z_critical function)
    print('STEP 5')
    critical_value = z_critical(tail, alpha)
    print('Critical Value : ', critical_value)
    
    if tail == 'two':
        left_critical, right_critical = critical_value
        if z < left_critical or z > right_critical:
            print('Reject H0')
        else:
            print('Failed to reject H0')
    elif tail == 'right':
        if z > critical_value:
            print('Reject H0')
        else:
            print('Failed to reject H0')
    elif tail == 'left':
        if z < critical_value:
            print('Reject H0')
        else:
            print('Failed to reject H0')
            
# Step 5: Credit Card Debt
z_test_steps(mu0=3262, xbar=2995, sigma=1100, n=50, alpha=0.05, tail="left")