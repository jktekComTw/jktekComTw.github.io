# Chapter 7 — Time-Varying Fields and Maxwell's Equations
## Problems and Solutions

---

### Problem 1 — Motional EMF in a Moving Conductor

A bar of length L = 0.5 m moves at **v = 5 a_x m/s** in uniform field **B = 0.2 a_z T**. Find the induced EMF.

**Solution:**
```
v × B = (5 a_x) × (0.2 a_z) = 1.0 (a_x × a_z) = -1.0 a_y  V/m

EMF = ∫(v × B)·dl  (along bar in a_y direction, 0 to L)
    = (-1.0 a_y)·(L a_y) = -1.0 × 0.5 = -0.5 V

|EMF| = 0.5 V
```

---

### Problem 2 — Faraday's Law: Induced Electric Field

A time-varying **B = cos(100πt) a_z T** fills a circular region of radius a = 0.1 m. Find **E** at r = 0.1 m.

**Solution:**
```
Faraday's law (integral form):
∮ E·dl = -d/dt ∫∫ B·dS

By symmetry, E = E_φ a_φ along circular path:
E_φ (2πr) = -d/dt [B · πr²]
           = -πr² · (-100π sin(100πt))
           = 100π² r² sin(100πt)

E_φ = (100π² r²) / (2πr) = 50πr sin(100πt)

At r = 0.1 m:
E = 50π(0.1) sin(100πt) a_φ = 5π sin(100πt) a_φ ≈ 15.7 sin(100πt) a_φ  V/m
```

---

### Problem 3 — Displacement Current in a Capacitor

Parallel-plate capacitor: A = 0.01 m², d = 1 mm, free space. Voltage V = 100 sin(2π×10⁶t) V. Find J_d and total I_d.

**Solution:**
```
E = V/d = 100 sin(2π×10⁶t) / 10⁻³ = 10⁵ sin(2π×10⁶t)  V/m

D = ε₀ E = (8.85×10⁻¹²)(10⁵) sin(2π×10⁶t) = 8.85×10⁻⁷ sin(2π×10⁶t)  C/m²

J_d = ∂D/∂t = 8.85×10⁻⁷ × 2π×10⁶ cos(2π×10⁶t)
             = 5.56 cos(2π×10⁶t)  A/m²

I_d = J_d × A = 5.56 × 0.01 = 55.6 cos(2π×10⁶t)  mA
```

---

### Problem 4 — Verify Maxwell's Equations

Given **E = E₀ cos(kz − ωt) a_x** and **H = H₀ cos(kz − ωt) a_y** in free space. Verify and find the constraint between E₀, H₀, k, ω.

**Solution:**
```
∇·E = ∂Ex/∂x = 0  ✓  (no x-dependence)
∇·H = ∂Hy/∂y = 0  ✓  (no y-dependence)

From ∇ × E = -μ₀ ∂H/∂t :
  (∇ × E)_y = ∂Ex/∂z = -E₀k sin(kz-ωt)
  -μ₀ ∂H/∂t = -μ₀ H₀ω sin(kz-ωt)
  → E₀k = μ₀ H₀ω  ... (1)

From ∇ × H = ε₀ ∂E/∂t :
  (∇ × H)_x = -∂Hy/∂z = H₀k sin(kz-ωt)
  ε₀ ∂E/∂t  =  ε₀ E₀ω sin(kz-ωt)
  → H₀k = ε₀ E₀ω  ... (2)

From (1)×(2): k² = μ₀ε₀ ω²
  → k = ω/c  ✓

E₀/H₀ = √(μ₀/ε₀) = η₀ = 377 Ω
```

---

### Problem 5 — Vector Potential to E and H

Given **A = A₀ sin(kz − ωt) a_x**, V = 0. Find **E** and **H**.

**Solution:**
```
E = -∇V - ∂A/∂t = -∂A/∂t
  = A₀ω cos(kz - ωt) a_x

B = ∇ × A:
  (∇ × A)_y = ∂Ax/∂z = A₀k cos(kz - ωt)

H = B/μ₀ = (A₀k/μ₀) cos(kz - ωt) a_y

Check ratio: E₀/H₀ = A₀ω / (A₀k/μ₀) = μ₀ω/k = η₀  when k = ω/c  ✓
```

---

### Problem 6 — Boundary Conditions at Perfect Conductor

**E_i = 10 cos(ωt − kz) a_x V/m** incident on perfect conductor at z = 0. Find reflected field and surface current.

**Solution:**
```
BC: tangential E = 0 at z = 0
  → E_r = -10 cos(ωt + kz) a_x  V/m

Incident H:   H_i = (10/η₀) cos(ωt - kz) a_y
Reflected H:  H_r = (10/η₀) cos(ωt + kz) a_y

Total H at z = 0:
  H_total = (20/η₀) cos(ωt) a_y

Surface current (n̂ = -a_z outward from conductor):
  J_s = n̂ × H = (-a_z) × (20/η₀) cos(ωt) a_y
      = (20/η₀) cos(ωt) a_x
      = 53.1 cos(ωt)  mA/m  a_x
```

---

### Problem 7 — Solve 1D Wave Equation

Find **E(z,t)** for a +z propagating wave at f = 1 GHz, amplitude 50 V/m in free space.

**Solution:**
```
Wave equation: ∂²E/∂z² = (1/c²) ∂²E/∂t²
General +z solution: E = E₀ cos(kz - ωt)

f = 1 GHz = 10⁹ Hz
ω = 2π × 10⁹ = 6.283×10⁹  rad/s
λ = c/f = 3×10⁸ / 10⁹ = 0.3 m
k = 2π/λ = 2π/0.3 = 20.94  rad/m

E(z,t) = 50 cos(20.94z - 6.283×10⁹ t) a_x  V/m
```

---

### Problem 8 — Time-Domain to Phasor Conversion

Convert **E(x,t) = 10 cos(ωt − 2x) a_x − 5 sin(ωt − 2x) a_y** to phasor form.

**Solution:**
```
Use E(x,t) = Re[Ẽ(x) e^(jωt)]

x-component: 10 cos(ωt - 2x) = Re[10 e^(-j2x) e^(jωt)]
  → Ẽ_x = 10 e^(-j2x)

y-component: -5 sin(ωt - 2x) = Re[j5 e^(-j2x) e^(jωt)]
             since -sin(θ) = cos(θ + π/2) and -e^(-jπ/2) = j
  → Ẽ_y = j5 e^(-j2x)

Ẽ(x) = (10 a_x + j5 a_y) e^(-j2x)  V/m
```

---

### Problem 9 — Skin Depth in Copper

Copper: σ = 5.8×10⁷ S/m, μᵣ = 1. Find δ at 60 Hz, 1 MHz, 1 GHz.

**Solution:**
```
δ = √(2 / (ωμ₀σ))  [good conductor approximation: σ >> ωε]

Simplifies to:  δ = 66.1/√f  mm  (f in Hz, for copper)

f = 60 Hz:   δ = 66.1/√60     = 8.53  mm
f = 1 MHz:   δ = 66.1/√(10⁶)  = 66.1  μm
f = 1 GHz:   δ = 66.1/√(10⁹)  = 2.09  μm
```

---

### Problem 10 — Phase Velocity in Dielectric

Non-magnetic dielectric with εᵣ = 4. Find phase velocity, wavelength at 500 MHz, and wave impedance.

**Solution:**
```
v_p = c/√(μᵣ εᵣ) = 3×10⁸/√4 = 1.5×10⁸  m/s

λ = v_p/f = 1.5×10⁸ / 500×10⁶ = 0.3 m

η = η₀ √(μᵣ/εᵣ) = 377 × √(1/4) = 188.5 Ω
```

---

### Problem 11 — Poynting Vector

**E = 100 cos(ωt − kz) a_x V/m** in free space. Find H, instantaneous S, and time-average ⟨S⟩.

**Solution:**
```
H = (E₀/η₀) cos(ωt - kz) a_y = (100/377) cos(ωt - kz) a_y = 0.265 cos(ωt-kz) a_y  A/m

S = E × H = 100 × 0.265 cos²(ωt - kz) (a_x × a_y)
          = 26.5 cos²(ωt - kz) a_z  W/m²

⟨S⟩ = E₀²/(2η₀) = 10000/(2×377) = 13.26 a_z  W/m²
```

---

### Problem 12 — Transformer EMF

Rectangular loop (0.2 m × 0.1 m) in **B = 0.5 cos(1000t) a_z T**. Find induced EMF.

**Solution:**
```
Φ = B · A = 0.5 cos(1000t) × (0.2 × 0.1) = 0.01 cos(1000t)  Wb

EMF = -dΦ/dt = 0.01 × 1000 sin(1000t) = 10 sin(1000t)  V
```

---

### Problem 13 — Motional EMF in a Sliding Bar

Bar slides at **v = 5 a_x m/s** in **B = 0.2 a_z T**, bar length L = 0.5 m along a_y. Find EMF and force on charge q.

**Solution:**
```
v × B = (5 a_x) × (0.2 a_z) = -1.0 a_y  V/m

EMF = ∫₀^L (v × B)·(dy a_y) = -1.0 × 0.5 = -0.5 V

Force on charge q in bar:
  F = q(v × B) = -q a_y  N
```

---

### Problem 14 — E from Time-Varying B

**B = B₀ sin(kx) cos(ωt) a_z**. Find **E** using Faraday's law.

**Solution:**
```
∇ × E = -∂B/∂t = B₀ω sin(kx) sin(ωt) a_z

Assume E = E_y(x,t) a_y  (by symmetry)

(∇ × E)_z = ∂E_y/∂x = B₀ω sin(kx) sin(ωt)

Integrate over x:
  E_y = -(B₀ω/k) cos(kx) sin(ωt)

E = -(B₀ω/k) cos(kx) sin(ωt) a_y  V/m
```

---

### Problem 15 — Wave Parameters from Field Expression

**E = 50 cos(2π×10⁸t − πz/1.5) a_x V/m**. Find f, ω, k, λ, v_p, H.

**Solution:**
```
Comparing with E₀ cos(ωt - kz):

ω = 2π×10⁸  rad/s
f = ω/2π = 10⁸ Hz = 100 MHz

k = π/1.5 = 2π/3 ≈ 2.094  rad/m
λ = 2π/k = 3 m

v_p = ω/k = 2π×10⁸ / (π/1.5) = 3×10⁸  m/s = c  ✓  (free space confirmed)

H = (50/377) cos(2π×10⁸ t - πz/1.5) a_y
  = 0.133 cos(2π×10⁸ t - πz/1.5) a_y  A/m
```
