# Chapter 6 — Static Magnetic Fields
## Problems and Solutions

---

## Part A — Biot-Savart, Ampère's Law, Magnetostatics (Sections 6-1 to 6-7)

---

### Problem 1 — Magnetic Field from a Long Straight Wire

Infinite wire carrying I = 10 A along the z-axis. Find B at ρ = 0.05 m.

**Solution:**
```
By Ampère's law (symmetry → B in a_φ direction):
  ∮ H·dl = I_enc
  H × 2πρ = I
  H = I/(2πρ)

B = μ₀H = μ₀I/(2πρ)
  = 4π×10⁻⁷ × 10/(2π × 0.05)
  = 4π×10⁻⁶/0.1π
  = 4×10⁻⁵ T = 40 μT

Direction: a_φ (right-hand rule with current in +a_z)
```

---

### Problem 2 — Biot-Savart Law: Circular Current Loop

Circular loop of radius a = 0.1 m, current I = 5 A. Find B at center and along axis.

**Solution:**
```
At center (z=0):
  B = μ₀I/(2a) = 4π×10⁻⁷ × 5/(2 × 0.1)
    = 20π×10⁻⁷/0.2
    = 100π×10⁻⁷ = 31.4 μT  (in â_z direction)

Along axis at distance z:
  B_z = μ₀Ia²/[2(a²+z²)^{3/2}]

At z=0: B = μ₀I/(2a) = 31.4 μT  ✓
At z=a: B = μ₀I/(2a) × a³/(a²+a²)^{3/2} = μ₀I/(2a) × 1/(2√2)
       = 31.4/2.828 = 11.1 μT
```

---

### Problem 3 — Solenoid Magnetic Field

Solenoid: N=500 turns, L=0.25m, I=2A, air core. Find B inside.

**Solution:**
```
n = N/L = 500/0.25 = 2000  turns/m

Inside (uniform field, far from ends):
  H = nI = 2000 × 2 = 4000  A/m
  B = μ₀H = 4π×10⁻⁷ × 4000 = 5.026×10⁻³ T ≈ 5.03 mT

For iron core (μᵣ = 1000):
  B = μ₀μᵣnI = 1000 × 5.03×10⁻³ = 5.03 T  (MRI magnet range)

Energy stored per unit volume: u = B²/(2μ₀) = (5.03×10⁻³)²/(8π×10⁻⁷) = 10.1 J/m³
```

---

### Problem 4 — Vector Magnetic Potential

Find A for an infinite straight wire (I along z). Verify B = ∇×A.

**Solution:**
```
By symmetry: A = A_z(ρ) â_z

∇²A = -μ₀J (Poisson's equation for A)
For ρ≠0 (current region): ∇²A_z = 0

Solution: A_z = -μ₀I/(2π) lnρ + C  (chosen so B = ∇×A matches known result)

B = ∇×A:
  B_φ = -∂A_z/∂ρ = -(-μ₀I/(2πρ)) = μ₀I/(2πρ)  ✓

In general: A = -μ₀I ln(ρ/ρ_ref)/(2π) â_z
(Reference ρ_ref cancels in derivatives)
```

---

### Problem 5 — Magnetic Field Along Axis of Current Loop

Two coaxial loops (Helmholtz coil), each radius a=0.1m, separated by d=0.1m=a, each carrying I=5A. Find B at midpoint.

**Solution:**
```
B from single loop at distance z from center:
  B_z = μ₀Ia²/[2(a²+z²)^{3/2}]

Each loop is at z = ±a/2 from midpoint:
  z = a/2 = 0.05 m for each loop

B from each loop at midpoint:
  B_single = μ₀×5×0.01/[2(0.01+0.0025)^{3/2}]
           = 4π×10⁻⁷×5×0.01/[2(0.0125)^{3/2}]
           = 2π×10⁻⁸/[2×1.398×10⁻³]
           = 22.47 μT

Total (both loops add): B_total = 2×22.47 = 44.9 μT

Helmholtz condition (d=a): field is very uniform near center.
Exact value: B = (4/5)^{3/2} × μ₀nI/a ≈ 0.7155 × μ₀nI/a
```

---

### Problem 6 — Force Between Parallel Wires

Two parallel wires 0.1 m apart, each carrying I = 100 A in the same direction. Find force per unit length.

**Solution:**
```
B from wire 1 at wire 2's location:
  B₁ = μ₀I/(2πd) = 4π×10⁻⁷ × 100/(2π × 0.1) = 2×10⁻⁴  T

Force per unit length on wire 2:
  F/L = I × B₁ = 100 × 2×10⁻⁴ = 0.02 N/m  (attractive, same direction currents)

Formula: F/L = μ₀I₁I₂/(2πd) = 4π×10⁻⁷ × 10⁴/(2π×0.1) = 0.02 N/m

Definition of ampere: two wires 1m apart with I=1A each → F/L = 2×10⁻⁷ N/m.
```

---

### Problem 7 — Magnetization in a Ferromagnetic Material

Iron with μᵣ = 5000, H = 500 A/m. Find B, M, and magnetization current density.

**Solution:**
```
B = μ₀μᵣH = 4π×10⁻⁷ × 5000 × 500 = 4π×10⁻⁷ × 2.5×10⁶
  = π × 10⁻¹ = 3.14×10⁻¹ T ≈ 0.314 T

Wait: 4π×10⁻⁷ × 5000 × 500 = 4π×10⁻⁷ × 2.5×10⁶ = 10π×10⁻¹ = π T
  B = π ≈ 3.14 T  (close to saturation for iron)

Magnetization: M = (μᵣ-1)H = 4999 × 500 = 2.4995×10⁶  A/m ≈ 2.5 MA/m

B = μ₀(H + M) = 4π×10⁻⁷(500 + 2.5×10⁶) ≈ μ₀M = 3.14 T  ✓

Magnetization volume current: J_m = ∇×M (zero for uniform M)
Magnetization surface current: K_m = M × â_n  (at material boundary)
```

---

### Problem 8 — Equivalent Magnetization Currents

Uniformly magnetized sphere: M = M₀ â_z. Find equivalent bound current densities.

**Solution:**
```
Volume magnetization current density:
  J_m = ∇×M = ∇×(M₀ â_z) = 0  (uniform M → zero volume current)

Surface magnetization current density:
  K_m = M × â_n  (â_n = outward normal)

In spherical coordinates, â_n = â_r:
  K_m = M₀ â_z × â_r = M₀ sinθ â_φ

(Using â_z = cosθ â_r - sinθ â_θ and â_z × â_r = sinθ (â_θ × ... )

Simplified: K_m = M₀ sinθ â_φ  [A/m]

This is the same current distribution as a spinning charged sphere —
equivalent to a magnetic dipole.
```

---

### Problem 9 — H-Field in a Toroid

Toroid: N = 200 turns, mean radius R = 0.1 m, current I = 3 A, μᵣ = 500 (iron core). Find B and H.

**Solution:**
```
By Ampère's law (closed path along mean circumference):
  H × 2πR = NI
  H = NI/(2πR) = 200×3/(2π×0.1) = 600/0.6283 = 954.9  A/m

B = μ₀μᵣH = 4π×10⁻⁷ × 500 × 954.9
  = 4π×10⁻⁷ × 4.775×10⁵
  = 0.600 T

H in air gap (if introduced): B/μ₀ = 0.600/(4π×10⁻⁷) = 4.775×10⁵ A/m
(much larger H needed to maintain same B — magnetomotive force drops across gap)
```

---

### Problem 10 — Ampère's Law: Infinite Solenoid

Ideal solenoid: n = 1000 turns/m, I = 2 A. Find B inside and outside.

**Solution:**
```
Apply Ampère's law with rectangular path (half inside, half outside):
  ∮ H·dl = NI_enclosed

Outside: by symmetry, B=0 (the contributions from both sides cancel for ideal ∞ solenoid)

Inside: H×L = n×L×I (L = path length along solenoid axis inside)
  H_inside = nI = 1000 × 2 = 2000  A/m
  B_inside = μ₀H = 4π×10⁻⁷ × 2000 = 2.51×10⁻³ T = 2.51 mT

For iron core (μᵣ=1000): B = 2.51 T

Outside B = 0 (ideal solenoid, confirmed by Ampère's law with path entirely outside)
```

---

### Problem 11 — Infinite Current Sheet

Surface current K = K₀ â_x (A/m) on z=0 plane. Find H above and below.

**Solution:**
```
By symmetry and Ampère's law (rectangular path straddling the sheet):
  H above (z>0): H = -K₀/2 â_y
  H below (z<0): H = +K₀/2 â_y

Full expression:
  H = -(K₀/2) â_z × â_n  where â_n = â_z (pointing up)

For K = K₀ â_x:
  H = ∓ K₀/2 â_y  (minus sign above, plus below)

B = μ₀H:
  Above: B = -μ₀K₀/2 â_y
  Below: B = +μ₀K₀/2 â_y

Note: tangential H is discontinuous: H_above - H_below = K × â_n (boundary condition)
  (-K₀/2 - K₀/2) â_y = -K₀ â_y = K₀â_x × (-â_z) ... (verify: â_x × â_z = -â_y ✓)
```

---

### Problem 12 — Magnetic Field of a Finite Wire

Straight wire of length 2L carrying current I along z-axis, centered at origin. Find B at point (ρ, 0, 0).

**Solution:**
```
By Biot-Savart:
  B = μ₀I/(4π) ∫_{-L}^{L} dl × â_r / r²

Result:
  B_φ = μ₀I/(4πρ) × 2L/√(L²+ρ²)
      = μ₀IL/(2πρ√(L²+ρ²))

At ρ = 0.05 m, L = 0.5 m, I = 10 A:
  B = 4π×10⁻⁷ × 10 × 0.5/(2π × 0.05 × √(0.25+0.0025))
    = 4π×10⁻⁷ × 5/(2π × 0.05 × 0.5025)
    = 2π×10⁻⁶/(0.1571)
    = 2π×10⁻⁶/0.1571 = 12.7×10⁻⁶/(0.5025×0.1π)

  Simplify: B = 4×10⁻⁷×10×0.5/(0.1×√0.2525) = 2×10⁻⁶/0.05025 = 39.8 μT

For L → ∞: B = μ₀I/(2πρ) = 40 μT  ✓ (matches infinite wire)
```

---

### Problem 13 — Magnetic Dipole Moment

Circular current loop: I = 5 A, radius a = 0.02 m. Find magnetic dipole moment m.

**Solution:**
```
m = I × A = I × πa²
  = 5 × π × (0.02)²
  = 5 × π × 4×10⁻⁴
  = 6.283×10⁻³  A·m²

Direction: â_z (right-hand rule with current direction)

Far-field approximation (r >> a):
  B_r = μ₀m cosθ/(2πr³)
  B_θ = μ₀m sinθ/(4πr³)

These are identical in form to the electric dipole field (with m replacing p/ε₀).
```

---

### Problem 14 — Vector Potential: Cylindrical Coordinates

For a solenoid (B = B₀ â_z inside, 0 outside), find A using ∇×A = B.

**Solution:**
```
By symmetry: A = A_φ(ρ) â_φ

Inside (ρ < a):
  (1/ρ)d(ρA_φ)/dρ = B₀
  d(ρA_φ)/dρ = B₀ρ
  ρA_φ = B₀ρ²/2  (integrating)
  A_φ = B₀ρ/2

Outside (ρ > a):
  d(ρA_φ)/dρ = 0  →  ρA_φ = const = B₀a²/2
  A_φ = B₀a²/(2ρ)

Summary:
  A = (B₀ρ/2) â_φ        for ρ < a
  A = (B₀a²/2ρ) â_φ      for ρ > a

Note: A exists outside even though B=0 there. This underlies the Aharonov-Bohm effect.
```

---

### Problem 15 — Force on a Current Loop

Rectangular loop (a×b) carrying current I in non-uniform field B = B₀(1+αz) â_z. Loop in xy-plane at z=0. Find net force.

**Solution:**
```
For a planar loop in a non-uniform field, net force = ∇(m·B)

m = Iab â_z,  B = B₀(1+αz)

F = ∇(m·B) = Iab ∇(B₀(1+αz)) = Iab B₀α â_z

F = IabαB₀ â_z

More rigorously: sides parallel to y have equal/opposite forces from x-component.
The z-gradient causes a net force on the loop.

For I=1A, a=b=0.05m, α=10 m⁻¹, B₀=0.1T:
  F = 1×0.0025×10×0.1 = 2.5×10⁻³ N = 2.5 mN
```

---

## Part B — Magnetic Circuits, Inductance, Energy, Forces (Sections 6-8 to 6-13)

---

### Problem 16 — Magnetic Circuit with Air Gap

Iron toroid: mean length l_iron = 0.3 m, μᵣ = 2000, cross-section A = 4 cm², air gap l_g = 2 mm.
N = 500 turns, I = 1 A. Find B.

**Solution:**
```
Total MMF: F = NI = 500 × 1 = 500  A·turns

Reluctances:
  R_iron = l_iron/(μ₀μᵣA) = 0.3/(4π×10⁻⁷ × 2000 × 4×10⁻⁴)
         = 0.3/(1.005×10⁻⁶) = 2.985×10⁵  A/Wb

  R_gap  = l_g/(μ₀A) = 2×10⁻³/(4π×10⁻⁷ × 4×10⁻⁴)
         = 2×10⁻³/(5.027×10⁻¹⁰) = 3.979×10⁶  A/Wb

Total reluctance: R = R_iron + R_gap = 2.985×10⁵ + 3.979×10⁶ = 4.278×10⁶  A/Wb

Flux: Φ = F/R = 500/(4.278×10⁶) = 1.169×10⁻⁴  Wb

B = Φ/A = 1.169×10⁻⁴/4×10⁻⁴ = 0.292 T

Note: gap (2mm) dominates reluctance despite iron being 150× longer.
```

---

### Problem 17 — Reluctance of a Magnetic Path

Same core as Problem 16. Find reluctance ratio R_gap/R_iron.

**Solution:**
```
From Problem 16:
  R_iron = 2.985×10⁵  A/Wb
  R_gap  = 3.979×10⁶  A/Wb

Ratio: R_gap/R_iron = 3.979×10⁶/2.985×10⁵ = 13.33

General formula:
  R_gap/R_iron = (l_g/l_iron) × μᵣ = (2×10⁻³/0.3) × 2000
               = 0.00667 × 2000 = 13.33  ✓

Even a small gap (l_g << l_iron) dominates if μᵣ is large.
```

---

### Problem 18 — B-H Curve and Hysteresis

For a soft iron sample, the B-H relationship approximates B = μ₀μᵣH with μᵣ = 1500 for H < 500 A/m, then saturates at B_sat = 1.5 T. Find H at B = 1.0 T and B = 1.5 T.

**Solution:**
```
Linear region (B < μ₀×1500×500 = 0.942 T):
  H = B/(μ₀μᵣ) = B/(4π×10⁻⁷×1500) = B/1.885×10⁻³

At B = 0.8 T: H = 0.8/1.885×10⁻³ = 424.4 A/m  (linear region)

At B = 1.0 T:
  Linear extrapolation: H = 1.0/1.885×10⁻³ = 530.8 A/m (above linear limit)
  Actual H > 530 A/m (curve bends up before saturation)
  Typical: H ≈ 800-1000 A/m at B=1.0T for soft iron

At B = B_sat = 1.5 T:
  H is very large (thousands of A/m) — saturation means dB/dH → 0
  Practical value: H ≈ 10,000-50,000 A/m at saturation
```

---

### Problem 19 — Boundary Conditions at Iron-Air Interface

B₁ = 0.5 T at θ₁ = 60° to normal, in iron (μᵣ = 1000). Find B₂ in air.

**Solution:**
```
Boundary conditions:
  Normal: B₁n = B₂n  (continuous)
  Tangential: H₁t = H₂t  →  B₁t/μ₁ = B₂t/μ₂

B₁n = B₁ cos60° = 0.5 × 0.5 = 0.25 T
B₁t = B₁ sin60° = 0.5 × 0.866 = 0.433 T

B₂n = B₁n = 0.25 T

B₂t = (μ₂/μ₁) × B₁t = (μ₀/μ₀μᵣ) × 0.433 = 0.433/1000 = 4.33×10⁻⁴ T

B₂ = √(B₂n² + B₂t²) = √(0.0625 + 1.88×10⁻⁷) ≈ 0.25 T

tan θ₂/tan θ₁ = μ₂/μ₁ = 1/1000
θ₂ = arctan(tan60°/1000) = arctan(0.001732) = 0.099° ≈ 0.1°

Magnetic field lines are nearly normal to iron surface in air (flux concentration effect).
```

---

### Problem 20 — Self-Inductance of a Solenoid

Solenoid: N=500 turns, L=0.25m, radius r=1cm, air core. Find L.

**Solution:**
```
L = μ₀N²A/l = μ₀n²Al

n = N/l = 500/0.25 = 2000  turns/m
A = πr² = π×(0.01)² = 3.14×10⁻⁴  m²

L = 4π×10⁻⁷ × (2000)² × 3.14×10⁻⁴ × 0.25
  = 4π×10⁻⁷ × 4×10⁶ × 7.854×10⁻⁵
  = 4π×10⁻⁷ × 314.16
  = 4π × 3.1416×10⁻⁵
  = 12.566×3.1416×10⁻⁵
  = 3.948×10⁻⁴ H ≈ 0.395 mH

For iron core (μᵣ=1000): L = 0.395 H
```

---

### Problem 21 — Mutual Inductance

Two coaxial solenoids: both length l=0.25m, inner (N₁=500, r₁=1cm), outer (N₂=200, r₂=2cm). Find M.

**Solution:**
```
All flux from inner solenoid passes through the outer (since r₂ > r₁):

Flux from inner at inner area:
  B₁ = μ₀n₁I₁ = μ₀ × 2000 × I₁

Flux linkage through outer (N₂ turns, area = inner area since flux is confined to inner):
  Λ₂₁ = N₂ × B₁ × A₁ = N₂ × μ₀n₁I₁ × πr₁²

M = Λ₂₁/I₁ = N₂ × μ₀n₁ × πr₁²
  = 200 × 4π×10⁻⁷ × 2000 × π×10⁻⁴
  = 200 × 4π×10⁻⁷ × 2000 × 3.14×10⁻⁴
  = 200 × 2.513×10⁻⁷ × 2000 × ...

Simpler: M = μ₀N₁N₂A₁/l = 4π×10⁻⁷ × 500×200 × 3.14×10⁻⁴/0.25
         = 4π×10⁻⁷ × 10⁵ × 1.257×10⁻³
         = 4π×10⁻⁷ × 125.7
         = 1.581×10⁻⁴ H = 0.158 mH

Check: M ≤ √(L₁L₂) = √(0.395×10⁻³ × L₂)  (Neumann inequality)
```

---

### Problem 22 — Energy Stored in Magnetic Field

Solenoid (L=0.395 mH) carrying I=5A. Find stored energy W.

**Solution:**
```
W = LI²/2 = 0.395×10⁻³ × 25/2 = 4.9375×10⁻³ J ≈ 4.94 mJ

In terms of field:
  B = μ₀nI = 4π×10⁻⁷ × 2000 × 5 = 12.57×10⁻³ T = 12.57 mT

  u = B²/(2μ₀) = (12.57×10⁻³)²/(8π×10⁻⁷)
    = 1.580×10⁻⁴/(2.513×10⁻⁶)
    = 62.88 J/m³

  Volume = πr²l = 3.14×10⁻⁴ × 0.25 = 7.854×10⁻⁵  m³

  W = u × Volume = 62.88 × 7.854×10⁻⁵ = 4.94×10⁻³ J  ✓
```

---

### Problem 23 — Magnetic Force on a Current Loop

Rectangular loop (a=0.1m, b=0.05m), I=2A, in field B = 0.3 â_z T. Loop in xy-plane. Find torque.

**Solution:**
```
Magnetic dipole moment:
  m = Iab â_z = 2 × 0.1 × 0.05 â_z = 0.01 â_z  A·m²

Torque: T = m × B = 0.01 â_z × 0.3 â_z = 0  (parallel → zero torque)

Now tilt loop so m = 0.01 â_x:
  T = 0.01 â_x × 0.3 â_z = 0.003 (â_x × â_z) = -0.003 â_y  N·m

Maximum torque occurs when m ⊥ B:
  T_max = |m||B| = 0.01 × 0.3 = 3×10⁻³ N·m = 3 mN·m
```

---

### Problem 24 — Torque on a Magnetic Dipole

Magnetic dipole m = 0.05 â_x A·m² in field B = 2 â_z T. Find torque and stable equilibrium position.

**Solution:**
```
T = m × B = 0.05 â_x × 2 â_z = 0.1 (â_x × â_z) = -0.1 â_y  N·m

|T| = 0.1 N·m

Potential energy: U = -m·B = -(0.05 â_x)·(2 â_z) = 0 J  (currently 90° orientation)

Stable equilibrium: U_min when m ∥ B (same direction)
  → m aligns with B: m = 0.05 â_z

At equilibrium:
  U = -m·B = -0.05 × 2 = -0.1 J
  T = 0

Unstable equilibrium: m anti-parallel to B, U = +0.1 J (T=0 but any perturbation destabilizes)
```

---

### Problem 25 — Force Between Magnetic Poles

Two bar magnets: pole strength p = 0.01 Wb, separation r = 0.1 m (between same poles). Find force.

**Solution:**
```
Force between magnetic poles (analogous to Coulomb's law):
  F = p₁p₂/(4πμ₀r²)

  = (0.01)²/(4π × 4π×10⁻⁷ × 0.01)
  = 10⁻⁴/(16π² × 4×10⁻⁹)
  = 10⁻⁴/(631.7×10⁻⁹)
  = 10⁻⁴/6.317×10⁻⁷
  = 158.3 N  (repulsive, same poles)

Note: pole strength p has units of Weber (Wb = V·s), and p = μ₀×(pole area)×H_surface.
```

---

### Problem 26 — Inductance of a Toroidal Coil

Toroid: N=500 turns, mean radius R=5cm, cross-sectional radius r=1cm, μᵣ=1. Find L.

**Solution:**
```
For toroid with circular cross-section (r << R):
  L ≈ μ₀N²A/(2πR)  [using mean path length = 2πR]

  A = πr² = π×(0.01)² = 3.14×10⁻⁴  m²

  L = 4π×10⁻⁷ × 500² × 3.14×10⁻⁴/(2π×0.05)
    = 4π×10⁻⁷ × 25×10⁴ × 3.14×10⁻⁴/0.3142
    = 4π×10⁻⁷ × 78.54/0.3142
    = 4π×10⁻⁷ × 250
    = 10π×10⁻⁵ = 3.14×10⁻⁴ H = 0.314 mH

For iron core μᵣ=500: L = 500 × 0.314 = 157 mH
```

---

### Problem 27 — Magnetic Pressure on a Surface

Toroid gap with B = 1 T in gap. Find the magnetic pressure (force per unit area) trying to close the gap.

**Solution:**
```
Magnetic pressure: p_m = B²/(2μ₀)
  = (1)²/(2 × 4π×10⁻⁷)
  = 1/(8π×10⁻⁷)
  = 3.979×10⁵  N/m² = 397.9 kPa ≈ 4 atm

Force on gap faces (area A = 4 cm² = 4×10⁻⁴ m²):
  F = p_m × A = 3.979×10⁵ × 4×10⁻⁴ = 159.2 N

This is why electromagnets can exert strong forces (closing the gap).
For B = 2 T: pressure = 1.59 MPa ≈ 16 atm.
```

---

### Problem 28 — Energy in Terms of Inductance

For the toroid in Problem 26 (L=0.314 mH), carrying I=2A. Find W and verify with field integral.

**Solution:**
```
W = LI²/2 = 0.314×10⁻³ × 4/2 = 6.28×10⁻⁴ J = 0.628 mJ

From field:
  H = NI/(2πR) = 500×2/(2π×0.05) = 1000/0.3142 = 3183  A/m
  B = μ₀H = 4π×10⁻⁷ × 3183 = 4.00×10⁻³ T = 4 mT

  u = B²/(2μ₀) = (4×10⁻³)²/(8π×10⁻⁷) = 1.6×10⁻⁵/2.513×10⁻⁶ = 6.37  J/m³

  Volume = A × 2πR = 3.14×10⁻⁴ × 0.3142 = 9.868×10⁻⁵  m³

  W = 6.37 × 9.868×10⁻⁵ = 6.28×10⁻⁴ J  ✓
```

---

### Problem 29 — Hall Effect

Copper conductor: width w = 5 mm, thickness t = 0.5 mm, B = 0.5 T (⊥ to current), I = 10 A.
n = 8.5×10²⁸ electrons/m³. Find Hall voltage V_H.

**Solution:**
```
Hall coefficient: R_H = -1/(ne) = -1/(8.5×10²⁸ × 1.6×10⁻¹⁹)
                = -1/(1.36×10¹⁰) = -7.35×10⁻¹¹  m³/C

Hall electric field:
  E_H = R_H × J × B = R_H × (I/(wt)) × B

  J = I/(wt) = 10/(5×10⁻³ × 0.5×10⁻³) = 10/2.5×10⁻⁶ = 4×10⁶  A/m²

  E_H = 7.35×10⁻¹¹ × 4×10⁶ × 0.5 = 1.47×10⁻⁴  V/m

Hall voltage: V_H = E_H × w = 1.47×10⁻⁴ × 5×10⁻³ = 7.35×10⁻⁷ V = 0.735 μV

Small for copper (many carriers). For semiconductors (n ~10²⁰), V_H is much larger.
```

---

### Problem 30 — Force on a Conductor in Magnetic Field

Straight wire, length L = 0.5 m, I = 20 A, in field B = 0.4 â_z T. Wire is along â_x. Find force.

**Solution:**
```
Force on current-carrying conductor:
  F = I L × B = I (L â_x) × (B â_z)
    = IL × B × (â_x × â_z)
    = ILB × (-â_y)
    = 20 × 0.5 × 0.4 × (-â_y)
    = -4 â_y  N

|F| = 4 N  (in -y direction)

General: F = IL × B  (where L is vector in direction of current flow)
```
