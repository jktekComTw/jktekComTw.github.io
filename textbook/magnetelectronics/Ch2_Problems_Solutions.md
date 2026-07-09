# Chapter 2 — Vector Analysis
## Problems and Solutions

---

### Problem 1 — Dot Product and Angle Between Vectors

A = 2a_x + 3a_y, B = 4a_x − a_y. Find A·B, |A|, |B|, and the angle between them.

**Solution:**
```
A·B = (2)(4) + (3)(-1) + (0)(0) = 8 - 3 = 5

|A| = √(4 + 9) = √13 = 3.606
|B| = √(16 + 1) = √17 = 4.123

cos θ = A·B/(|A||B|) = 5/(3.606 × 4.123) = 5/14.87 = 0.336

θ = arccos(0.336) = 70.4°
```

---

### Problem 2 — Cross Product in Cylindrical Coordinates

A = 2a_ρ + 3a_φ, B = a_ρ + 2a_z. Find A × B.

**Solution:**
```
Using the determinant:
A × B = |a_ρ  a_φ  a_z|
        |2     3    0  |
        |1     0    2  |

= a_ρ(3×2 - 0×0) - a_φ(2×2 - 0×1) + a_z(2×0 - 3×1)
= 6a_ρ - 4a_φ - 3a_z

Verify: A × B = -B × A
B × A = -6a_ρ + 4a_φ + 3a_z  ✓
```

---

### Problem 3 — Cartesian to Spherical Coordinate Conversion

Convert point P(1, 1, 1) from Cartesian to spherical coordinates.

**Solution:**
```
r = √(x² + y² + z²) = √(1+1+1) = √3 = 1.732

θ = arccos(z/r) = arccos(1/√3) = arccos(0.5774) = 54.74°

φ = arctan(y/x) = arctan(1/1) = arctan(1) = 45°

Result: (r, θ, φ) = (√3, 54.74°, 45°)

Check: x = r sinθ cosφ = √3 × sin54.74° × cos45° = √3×0.8165×0.7071 = 1  ✓
```

---

### Problem 4 — Surface Integral Using Divergence Theorem

Evaluate ∬ A·dS over the surface of a unit cube (0≤x,y,z≤1) for A = x a_x + y a_y + z a_z.

**Solution:**
```
Direct application of divergence theorem:
  ∬ A·dS = ∭ ∇·A dV

∇·A = ∂x/∂x + ∂y/∂y + ∂z/∂z = 1 + 1 + 1 = 3

∭ 3 dV = 3 × (1×1×1) = 3

Verify directly for one face:
  Face z=1 (n̂ = a_z, dS = dxdy):
  ∬ A·a_z dS = ∬ z|_{z=1} dxdy = ∫₀¹∫₀¹ 1 dxdy = 1
  Face z=0: contribution = 0
  By symmetry, each axis pair contributes 1 → total = 3  ✓
```

---

### Problem 5 — Gradient of a Scalar Field

Find ∇φ for φ = x²y + yz². Evaluate at P(1, 2, 3).

**Solution:**
```
∂φ/∂x = 2xy
∂φ/∂y = x² + z²
∂φ/∂z = 2yz

∇φ = 2xy a_x + (x² + z²) a_y + 2yz a_z

At P(1, 2, 3):
  ∇φ = 2(1)(2) a_x + (1 + 9) a_y + 2(2)(3) a_z
     = 4 a_x + 10 a_y + 12 a_z

|∇φ| = √(16 + 100 + 144) = √260 = 16.12

The gradient points in the direction of maximum rate of increase of φ.
```

---

### Problem 6 — Divergence in Spherical Coordinates

Calculate ∇·(r² â_r) in spherical coordinates.

**Solution:**
```
For A = A_r â_r with A_r = r²:

∇·A = (1/r²) d(r² A_r)/dr = (1/r²) d(r² × r²)/dr = (1/r²) d(r⁴)/dr

= (1/r²) × 4r³ = 4r

∇·(r² â_r) = 4r

Physical note: this is NOT zero, meaning r² â_r has sources everywhere.
Contrast with r̂/r² which has zero divergence (except at origin).
```

---

### Problem 7 — Divergence Theorem Verification

Verify the divergence theorem for A = x a_x over the unit cube.

**Solution:**
```
∇·A = ∂x/∂x = 1

Volume integral:
  ∭ ∇·A dV = ∭ 1 dV = 1

Surface integral (6 faces):
  x=1 (n̂=a_x):  ∬ x a_x·a_x dS = ∬ 1 dS = 1
  x=0 (n̂=-a_x): ∬ x a_x·(-a_x) dS = ∬ 0 dS = 0
  y=1 (n̂=a_y):  A·a_y = 0
  y=0 (n̂=-a_y): A·(-a_y) = 0
  z=1 (n̂=a_z):  A·a_z = 0
  z=0 (n̂=-a_z): A·(-a_z) = 0

  Total surface integral = 1 + 0 + 0 = 1  ✓
```

---

### Problem 8 — Curl in Cylindrical Coordinates

Find ∇ × A for A = ρ² a_φ.

**Solution:**
```
In cylindrical coordinates (A_ρ=0, A_φ=ρ², A_z=0):

(∇×A)_ρ = (1/ρ)∂A_z/∂φ - ∂A_φ/∂z = 0

(∇×A)_φ = ∂A_ρ/∂z - ∂A_z/∂ρ = 0

(∇×A)_z = (1/ρ)[∂(ρA_φ)/∂ρ - ∂A_ρ/∂φ]
         = (1/ρ) ∂(ρ × ρ²)/∂ρ
         = (1/ρ) ∂(ρ³)/∂ρ
         = (1/ρ) × 3ρ² = 3ρ

∇ × A = 3ρ a_z
```

---

### Problem 9 — Stokes's Theorem Verification

For A = y a_x, verify Stokes's theorem using the unit square in the xy-plane (counterclockwise).

**Solution:**
```
Surface integral:
  ∇×A = (∂A_y/∂x - ∂A_x/∂y) a_z = (0 - 1) a_z = -a_z
  ∬(∇×A)·dS = -1 × (1×1) = -1

Line integral (counterclockwise: C1→C2→C3→C4):
  C1: y=0, x: 0→1: ∫ y dx = 0
  C2: x=1, y: 0→1: ∫ y a_x·a_y dy = 0
  C3: y=1, x: 1→0: ∫ 1·dx = ∫₁⁰ dx = -1
  C4: x=0, y: 1→0: ∫ y a_x·a_y(-dy) = 0

  Total: 0 + 0 + (-1) + 0 = -1  ✓
```

---

### Problem 10 — Null Identity: ∇·(∇×A) = 0

Prove that the divergence of a curl is always zero.

**Solution:**
```
In Cartesian:
  ∇×A = (∂A_z/∂y - ∂A_y/∂z) a_x
       + (∂A_x/∂z - ∂A_z/∂x) a_y
       + (∂A_y/∂x - ∂A_x/∂y) a_z

∇·(∇×A) = ∂/∂x(∂A_z/∂y - ∂A_y/∂z)
          + ∂/∂y(∂A_x/∂z - ∂A_z/∂x)
          + ∂/∂z(∂A_y/∂x - ∂A_x/∂y)

= ∂²A_z/∂x∂y - ∂²A_y/∂x∂z
+ ∂²A_x/∂y∂z - ∂²A_z/∂y∂x
+ ∂²A_y/∂z∂x - ∂²A_x/∂z∂y

For continuous second derivatives, mixed partials are equal:
  ∂²A_z/∂x∂y = ∂²A_z/∂y∂x  → these cancel
  Similarly for the other pairs.
  → ∇·(∇×A) = 0  ✓
```

---

### Problem 11 — Null Identity: ∇×(∇φ) = 0

Prove the curl of a gradient is always zero.

**Solution:**
```
∇φ = ∂φ/∂x a_x + ∂φ/∂y a_y + ∂φ/∂z a_z

(∇×∇φ)_x = ∂/∂y(∂φ/∂z) - ∂/∂z(∂φ/∂y)
           = ∂²φ/∂y∂z - ∂²φ/∂z∂y = 0  (mixed partials equal)

Similarly for y and z components.
→ ∇×(∇φ) = 0  ✓

Physical meaning: an electrostatic field E = -∇V is always irrotational,
consistent with ∇×E = 0 in static cases.
```

---

### Problem 12 — Laplacian in Cylindrical Coordinates

Find ∇²φ in cylindrical form. Apply it to φ = ρ² cos(2α) (where α is the azimuthal angle).

**Solution:**
```
General form:
  ∇²φ = (1/ρ)∂/∂ρ(ρ ∂φ/∂ρ) + (1/ρ²)∂²φ/∂α² + ∂²φ/∂z²

For φ = ρ² cos(2α):
  ∂φ/∂ρ = 2ρ cos(2α)
  (1/ρ)∂(ρ × 2ρ cos2α)/∂ρ = (1/ρ) × 4ρ cos(2α) = 4 cos(2α)

  ∂²φ/∂α² = -4ρ² cos(2α)
  (1/ρ²)(−4ρ² cos(2α)) = -4 cos(2α)

  ∂²φ/∂z² = 0

∇²φ = 4cos(2α) - 4cos(2α) = 0

φ = ρ² cos(2α) satisfies Laplace's equation. (Used in wedge problems.)
```

---

### Problem 13 — Unit Normal to a Surface

Find the unit normal to the surface z = x² + y² at point (1, 1, 2).

**Solution:**
```
Rewrite as F(x,y,z) = z - x² - y² = 0

∇F = -2x a_x - 2y a_y + a_z

At (1, 1, 2):
  ∇F = -2 a_x - 2 a_y + a_z

|∇F| = √(4 + 4 + 1) = 3

n̂ = ∇F/|∇F| = (-2a_x - 2a_y + a_z)/3
   = -0.667 a_x - 0.667 a_y + 0.333 a_z

(This is the upward-pointing normal since the a_z component is positive.)
```

---

### Problem 14 — Circulation of a Vector Field

Evaluate ∮ A·dl for A = −y a_x + x a_y around a circle of radius a in the xy-plane.

**Solution:**
```
Parametrize: x = a cosφ, y = a sinφ, dl = a dφ(-sinφ a_x + cosφ a_y)

A on circle: -a sinφ a_x + a cosφ a_y

A·dl = (-a sinφ)(a)(-sinφ) dφ + (a cosφ)(a)(cosφ) dφ
     = a²sin²φ dφ + a²cos²φ dφ = a² dφ

∮ A·dl = ∫₀^{2π} a² dφ = 2πa²

Verify via Stokes:
  ∇×A = (∂x/∂x - ∂(-y)/∂y) a_z = (1+1) a_z = 2a_z
  ∬(∇×A)·dS = 2 × πa² = 2πa²  ✓
```

---

### Problem 15 — Helmholtz Theorem

Decompose F = x a_x + y a_y + z a_z into irrotational and solenoidal parts.

**Solution:**
```
Check divergence and curl:
  ∇·F = 1 + 1 + 1 = 3  (not zero → has irrotational part)
  ∇×F = 0              (irrotational — purely a gradient)

Since ∇×F = 0, the solenoidal part is zero (A = 0).
The field is purely irrotational: F = -∇φ

Find φ: -∇φ = F = r̂r → φ = -r²/2 = -(x²+y²+z²)/2

Verify: -∇φ = -(∂(-r²/2)/∂x a_x + ...) = x a_x + y a_y + z a_z = F  ✓

Helmholtz: F = -∇φ + ∇×A
  Here: φ = -(x²+y²+z²)/2,  A = 0
```
