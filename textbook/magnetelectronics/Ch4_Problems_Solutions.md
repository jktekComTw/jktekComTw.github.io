# Chapter 4 — Solution of Electrostatic Problems
## Problems and Solutions

---

### Problem 1 — Laplace's Equation: 1D Cartesian

Parallel plates at x=0 (V=0) and x=d (V=V₀). Solve Laplace's equation for V(x) and find E.

**Solution:**
```
d²V/dx² = 0  →  V = Ax + B

BC: V(0)=0 → B=0
    V(d)=V₀ → A = V₀/d

V(x) = V₀ x/d  (linear variation)

E = -∇V = -dV/dx a_x = -V₀/d a_x

For V₀=100V, d=1cm:
  E = -100/0.01 a_x = -10,000 a_x V/m  (uniform, pointing from + to – plate)
  ρ_s = ε₀|E| = 8.85×10⁻¹² × 10⁴ = 88.5 nC/m²
```

---

### Problem 2 — Fourier Series Solution (Rectangular Region)

Region: 0≤x≤a, 0≤y≤b. V=0 on three sides, V = V₀ sin(πx/a) on y=b. Find V(x,y).

**Solution:**
```
Separation of variables: V = X(x) Y(y)
  X'' + λX = 0  →  X = sin(nπx/a)  (with X(0)=X(a)=0)
  Y'' - λY = 0  →  Y = sinh(nπy/a)  (with Y(0)=0)

Since BC at y=b is exactly sin(πx/a) (n=1 only):
  V(x,y) = C sin(πx/a) sinh(πy/a)

Apply V(x,b) = V₀ sin(πx/a):
  C sinh(πb/a) = V₀  →  C = V₀/sinh(πb/a)

V(x,y) = V₀ sin(πx/a) × sinh(πy/a)/sinh(πb/a)

For a=b: V(x,y) = V₀ sin(πx/a) × sinh(πy/a)/sinh(π)
```

---

### Problem 3 — Method of Images: Point Charge Above Ground Plane

Q = 1 μC at height h = 0.5 m above grounded plane (z=0). Find E at z=0 directly below, and ρ_s.

**Solution:**
```
Image charge: Q' = -Q = -1 μC at z = -h = -0.5 m

At point (0,0,0) on the plane:
  Both real charge (distance h) and image charge (distance h) contribute along z:
  E_z = -2 × Q/(4πε₀h²) = -2 × 8.99×10⁹ × 10⁻⁶/0.25
      = -71,920 V/m  (downward, toward conductor)

Surface charge density at (x,y,0):
  ρ_s = ε₀E_z = -Qh/(2π(x²+y²+h²)^{3/2})

At x=y=0: ρ_s = -Qh/(2πh³) = -Q/(2πh²) = -10⁻⁶/(2π×0.25) = -0.637 μC/m²

Total induced charge: ∫∫ρ_s dA = -Q = -1 μC  ✓
```

---

### Problem 4 — Method of Images: Line Charge and Cylinder

Line charge ρ_L parallel to a grounded conducting cylinder (radius a, center at origin),
at distance d from center (d > a). State the image configuration.

**Solution:**
```
The image is a line charge of -ρ_L located at distance a²/d from the center
(inside the cylinder, on the same line connecting center to real charge).

Image position: r_image = a²/d  (Kelvin inversion)

Potential at any point outside:
  V = ρ_L/(2πε₀) × ln(r₂/r₁)

where r₁ = distance to real charge, r₂ = distance to image charge.

On the cylinder surface (r=a): V = 0  ✓ (can be verified geometrically)

Application: Two-wire transmission line uses this result.
```

---

### Problem 5 — Capacitance Using Method of Images (Two-Wire Line)

Two parallel cylindrical conductors: radius a = 1 mm, center-to-center separation D = 10 mm. Find C/L.

**Solution:**
```
C/L = πε₀/cosh⁻¹(D/2a)

D/2a = 10/(2×1) = 5
cosh⁻¹(5) = ln(5 + √(25-1)) = ln(5 + 4.899) = ln(9.899) = 2.292

C/L = π × 8.85×10⁻¹²/2.292 = 27.80×10⁻¹²/2.292 = 12.13 pF/m

For widely separated wires (D >> a):
  cosh⁻¹(D/2a) ≈ ln(D/a) = ln(10) = 2.303
  C/L ≈ πε₀/ln(D/a) = 12.08 pF/m  (close to exact)
```

---

### Problem 6 — Poisson's Equation: Uniform Space Charge

Between plates at x=0 (V=0) and x=d (V=V₀), uniform charge density ρ_v. Solve for V(x).

**Solution:**
```
d²V/dx² = -ρ_v/ε₀

Integrate twice:
  dV/dx = -ρ_v x/ε₀ + A
  V(x) = -ρ_v x²/(2ε₀) + Ax + B

Apply BC: V(0)=0 → B=0
          V(d)=V₀ → V₀ = -ρ_v d²/(2ε₀) + Ad
          → A = V₀/d + ρ_v d/(2ε₀)

V(x) = -ρ_v x²/(2ε₀) + [V₀/d + ρ_v d/(2ε₀)] x

E(x) = -dV/dx = ρ_v x/ε₀ - V₀/d - ρ_v d/(2ε₀)

For ρ_v=0: V = V₀x/d (reduces to Laplace result ✓)
```

---

### Problem 7 — Coaxial Cylinder Potential

Coaxial conductors: inner radius a=2mm at V₀=100V, outer radius b=10mm at V=0. Find V(ρ) and E.

**Solution:**
```
∇²V = (1/ρ)d/dρ(ρ dV/dρ) = 0
  → ρ dV/dρ = A  →  V = A lnρ + B

BC: V(a)=100, V(b)=0:
  0 = A ln(b) + B  →  B = -A ln(b)
  100 = A ln(a) - A ln(b) = A ln(a/b)
  A = 100/ln(a/b) = 100/ln(0.2) = 100/(-1.609) = -62.15

V(ρ) = -62.15 ln(ρ) + 62.15 ln(b)
      = -62.15 ln(ρ/b)
      = 62.15 ln(b/ρ)  V

E = -dV/dρ â_ρ = 62.15/ρ â_ρ  V/m

At ρ=a: E = 62.15/0.002 = 31,075 V/m = 31.1 kV/m
At ρ=b: E = 62.15/0.010 = 6,215 V/m = 6.22 kV/m
```

---

### Problem 8 — Concentric Spheres Potential

Spherical capacitor: inner sphere a=2cm at V₀=100V, outer sphere b=6cm at V=0. Find V(r) and C.

**Solution:**
```
(1/r²)d/dr(r² dV/dr) = 0
  → r² dV/dr = A  →  dV/dr = A/r²  →  V = -A/r + B

BC: V(b)=0: B = A/b
    V(a)=V₀: V₀ = -A/a + A/b = A(1/b - 1/a)
    A = V₀/(1/b - 1/a) = V₀ ab/(a-b)

For a=0.02m, b=0.06m:
  A = 100 × 0.02×0.06/(0.02-0.06) = 100×0.0012/(-0.04) = -3

V(r) = -(-3)/r + (-3)/0.06 = 3/r - 50  V

Check: V(0.02) = 3/0.02 - 50 = 150-50 = 100 V ✓
       V(0.06) = 3/0.06 - 50 = 50-50 = 0 V ✓

C = 4πε₀ ab/(b-a) = 4π×8.85×10⁻¹² × 0.02×0.06/0.04 = 3.34 pF
```

---

### Problem 9 — Grounded Conducting Sphere with Point Charge

Charge Q at distance d from center of grounded sphere (radius a, a < d). Find image charge.

**Solution:**
```
Image charge for grounded sphere:
  Q' = -Q(a/d)         (magnitude reduced by factor a/d)
  Location: r' = a²/d  (inside sphere, on line from center to Q)

Potential at any exterior point P:
  V = Q/(4πε₀r₁) + Q'/(4πε₀r₂)

where r₁ = |P - Q|, r₂ = |P - Q'|

V = 0 on sphere surface r = a  ✓ (by geometric property of image)

Induced charge on sphere: total = Q' = -Qa/d
Force on Q:
  F = QQ'/(4πε₀(d-r')²) = -Q²a/d / (4πε₀(d-a²/d)²)  [attractive]
```

---

### Problem 10 — Semi-Infinite Grounded Plane: Two Images

Point charge Q at (x₀, y₀) above a grounded plane at y=0 AND grounded plane at x=0 (corner). Find images.

**Solution:**
```
For a 90° conducting corner (x≥0, y≥0 region):
Three image charges needed:

  Real charge:     +Q at (x₀, y₀)
  Image 1:         -Q at (-x₀, y₀)   [image in x=0 plane]
  Image 2:         -Q at (x₀, -y₀)   [image in y=0 plane]
  Image 3:         +Q at (-x₀, -y₀)  [image of image, restores BC]

V = Q/(4πε₀) × [1/r₁ - 1/r₂ - 1/r₃ + 1/r₄]

where r₁,r₂,r₃,r₄ are distances from field point to each charge.

V = 0 on both x=0 and y=0 planes  ✓
```

---

### Problem 11 — Mixed Boundary Conditions

Half-space y>0 with V=V₀ for x>0 on y=0, and V=0 for x<0 on y=0. Find V(x,y).

**Solution:**
```
Solution using complex variables / conformal mapping:

V(x,y) = V₀/2 + (V₀/π) arctan(x/y)

Check boundaries:
  y→0⁺, x>0: arctan(x/0⁺) → π/2  →  V = V₀/2 + V₀/2 = V₀  ✓
  y→0⁺, x<0: arctan(x/0⁺) → -π/2 →  V = V₀/2 - V₀/2 = 0   ✓

E = -∇V:
  E_x = -∂V/∂x = -V₀y/(π(x²+y²))
  E_y = -∂V/∂y = +V₀x/(π(x²+y²))

The field has an r⁻¹ singularity at the edge (x=0, y=0).
```

---

### Problem 12 — Separation of Variables: 3D Box

Rectangular box: 0≤x≤a, 0≤y≤b, 0≤z≤c. V=0 on all faces except z=c where V = V₀ sin(πx/a) sin(πy/b).

**Solution:**
```
V(x,y,z) = X(x) Y(y) Z(z)

X = sin(πx/a),  Y = sin(πy/b)  (to satisfy V=0 at x=0,a and y=0,b)

Z'' = γ²Z where γ² = (π/a)² + (π/b)²
  Z = sinh(γz)  (to satisfy Z(0)=0)

Apply V(x,y,c) = V₀ sin(πx/a) sin(πy/b):
  V₀ = C sinh(γc)  →  C = V₀/sinh(γc)

V(x,y,z) = V₀ sin(πx/a) sin(πy/b) × sinh(γz)/sinh(γc)

with γ = π√(1/a² + 1/b²)
```

---

### Problem 13 — Coaxial Cable E and C

Inner conductor radius a=1mm, outer radius b=4mm, εᵣ=2.25. Find E(ρ) and C/L.

**Solution:**
```
From Problem 7 generalized with εᵣ:
  V(ρ) = V₀ ln(b/ρ)/ln(b/a)

E = -dV/dρ â_ρ = V₀/(ρ ln(b/a)) â_ρ

C/L = 2πε₀εᵣ/ln(b/a)
    = 2π × 8.85×10⁻¹² × 2.25/ln(4)
    = 2π × 19.91×10⁻¹²/1.386
    = 90.3 pF/m

E_max (at inner conductor, ρ=a):
  E_max = V₀/(a ln(b/a)) = V₀/(0.001 × 1.386) = 721 V₀  V/m per volt
```

---

### Problem 14 — Cylindrical Region with Space Charge

Cylindrical region 0≤ρ≤a, uniform ρ_v. V(a)=0 (grounded). Find V(ρ).

**Solution:**
```
(1/ρ)d/dρ(ρ dV/dρ) = -ρ_v/ε₀

Integrate: ρ dV/dρ = -ρ_v ρ²/(2ε₀) + C₁
           dV/dρ = -ρ_v ρ/(2ε₀) + C₁/ρ

For V finite at ρ=0: C₁ = 0 (otherwise ln singularity at center)

dV/dρ = -ρ_v ρ/(2ε₀)
V(ρ) = -ρ_v ρ²/(4ε₀) + C₂

BC: V(a)=0: C₂ = ρ_v a²/(4ε₀)

V(ρ) = ρ_v(a² - ρ²)/(4ε₀)  [maximum at center]

E(ρ) = ρ_v ρ/(2ε₀) â_ρ  [matches Gauss's law result]
```

---

### Problem 15 — Wedge-Shaped Region Potential

Conducting wedge: V=0 at φ=0 and V=V₀ at φ=α. Find V(φ) and E.

**Solution:**
```
∇²V = (1/ρ²)d²V/dφ² = 0  →  d²V/dφ² = 0

V(φ) = Aφ + B

BC: V(0)=0 → B=0
    V(α)=V₀ → A = V₀/α

V(φ) = V₀ φ/α  (linear in angle)

E = -∇V = -(1/ρ)dV/dφ â_φ = -V₀/(αρ) â_φ

The field is inversely proportional to ρ — stronger near the vertex.
For a parallel-plate capacitor (α→0, V₀/α = E₀): E = -E₀ â_φ (uniform ✓)

C/L = ε₀α/ln(b/a)  (for wedge bounded by cylinders ρ=a and ρ=b)
```
