import math

# -----------------------------
# Constants
# -----------------------------
print("PI:", math.pi)
print("Euler's Number:", math.e)
print("Infinity:", math.inf)
print("NaN:", math.nan)

# -----------------------------
# Rounding Functions
# -----------------------------
print("\nRounding Functions")
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))
print("trunc(4.9):", math.trunc(4.9))

# -----------------------------
# Power and Logarithmic Functions
# -----------------------------
print("\nPower and Log Functions")
print("sqrt(25):", math.sqrt(25))
print("pow(2, 3):", math.pow(2, 3))
print("exp(2):", math.exp(2))
print("log(10):", math.log(10))
print("log10(100):", math.log10(100))
print("log2(8):", math.log2(8))

# -----------------------------
# Trigonometric Functions
# -----------------------------
print("\nTrigonometric Functions")
angle = math.radians(30)

print("sin(30°):", math.sin(angle))
print("cos(30°):", math.cos(angle))
print("tan(30°):", math.tan(angle))

print("asin(0.5):", math.degrees(math.asin(0.5)))
print("acos(0.5):", math.degrees(math.acos(0.5)))
print("atan(1):", math.degrees(math.atan(1)))

# -----------------------------
# Angle Conversion
# -----------------------------
print("\nAngle Conversion")
print("Radians(180):", math.radians(180))
print("Degrees(pi):", math.degrees(math.pi))

# -----------------------------
# Hyperbolic Functions
# -----------------------------
print("\nHyperbolic Functions")
print("sinh(1):", math.sinh(1))
print("cosh(1):", math.cosh(1))
print("tanh(1):", math.tanh(1))

# -----------------------------
# Factorial and Combinatorics
# -----------------------------
print("\nFactorial and Combinatorics")
print("factorial(5):", math.factorial(5))
print("gcd(12, 18):", math.gcd(12, 18))
print("lcm(12, 18):", math.lcm(12, 18))
print("comb(5, 2):", math.comb(5, 2))
print("perm(5, 2):", math.perm(5, 2))

# -----------------------------
# Absolute Value Functions
# -----------------------------
print("\nAbsolute Value Functions")
print("fabs(-7.5):", math.fabs(-7.5))

# -----------------------------
# Floating Point Functions
# -----------------------------
print("\nFloating Point Functions")
print("fmod(10, 3):", math.fmod(10, 3))
print("remainder(10, 3):", math.remainder(10, 3))
print("modf(4.75):", math.modf(4.75))
print("frexp(8):", math.frexp(8))
print("ldexp(0.5, 4):", math.ldexp(0.5, 4))

# -----------------------------
# Distance Functions
# -----------------------------
print("\nDistance Functions")
print("dist((0,0), (3,4)):",
      math.dist((0, 0), (3, 4)))

print("hypot(3,4):", math.hypot(3, 4))

# -----------------------------
# Checking Functions
# -----------------------------
print("\nChecking Functions")
print("isfinite(100):", math.isfinite(100))
print("isinf(math.inf):", math.isinf(math.inf))
print("isnan(math.nan):", math.isnan(math.nan))
print("isclose(0.1+0.2, 0.3):",
      math.isclose(0.1 + 0.2, 0.3))

# -----------------------------
# Special Functions
# -----------------------------
print("\nSpecial Functions")
print("gamma(5):", math.gamma(5))
print("lgamma(5):", math.lgamma(5))
print("erf(1):", math.erf(1))
print("erfc(1):", math.erfc(1))