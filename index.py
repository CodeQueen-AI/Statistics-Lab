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
    print('STEP 1:')
    print("HO: mu0 = ", mu0)
    if tail == "two":
        print("H1: mu0 != ", mu0)
    elif tail == "right":
        print('H1: mu0 > ', mu0)
    elif tail == "left":
        print('H1: mu0 < ', mu0)
    else:
        print('Tail must be two , left or right!')
    
    print('STEP 2')
    
        