# %%
import sympy
from fractions import Fraction

# %%
from sympy.abc import n, r, a


# %%
def print_coffs(eq, r0, N):
    coff = a
    for i in range(1, N+1):
        coff = coff * (eq.subs(n, i-1).subs(r, r0))
        display(coff)


# %%
eq = (4*(n+r)**2 - 1)/(n+r+1)/(4*n+4*r+1)

# %%
print_coffs(eq, 0, 3)

# %%
print_coffs(eq, Fraction('3/4'), 3)
