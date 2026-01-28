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