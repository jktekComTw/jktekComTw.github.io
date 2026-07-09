# Chapter 3 — Static Electric Fields
## Problems and Solutions

---

### Problem 1 — Point Charge Electric Field

Find E at r = 0.5 m from a point charge Q = 1 μC.

**Solution:**
```
E = Q/(4πε₀r²) â_r
  = 10⁻⁶/(4π × 8.85×10⁻¹² × 0.25)
  = 10⁻⁶/2.789×10⁻¹¹
  = 35,840 â_r  V/m ≈ 35.8 kV/m

Alternatively: E = kQ/r² = 8.99×10⁹ × 10⁻⁶/0.25 = 35,960 V/m ≈ 36 kV/m
```

---

### Problem 2 — Infinite Line Charge

ρ_L = 2 nC/m. Find E at ρ = 0.1 m from the line.

**Solution:**
```
E = ρ_L/(2πε₀ρ) â_ρ
  = 2×10⁻⁹/(2π × 8.85×10⁻¹² × 0.1)
  = 2×10⁻⁹/5.563×10⁻¹²
  = 359.7 â_ρ  V/m

At ρ = 0.2 m: E = 180 V/m  (inverse linear decay, not r² for line charge)
```

---

### Problem 3 — Gauss's Law: Uniformly Charged Sphere

Sphere of radius a = 0.1 m with total charge Q = 1 μC (uniform ρ_v). Find E inside and outside.

**Solution:**
```
Volume charge density:
  ρ_v = Q/(4πa³/3) = 3×10⁻⁶/(4π×0.001) = 2.387×10⁻⁴  C/m³

Outside (r > a): same as point charge
  E = Q/(4πε₀r²) = 8.99×10⁹ × 10⁻⁶/r² = 8990/r²  V/m

At surface (r = a = 0.1 m):
  E = Q/(4πε₀a²) = 8990/0.01 = 899,000 V/m ≈ 899 kV/m

Inside (r < a): only enclosed charge matters
  E = Qr/(4πε₀a³) = E_surface × r/a

At r = a/2 = 0.05 m:
  E = 899 kV/m × 0.5 = 449.5 kV/m  (linear increase from center)
```

---

### Problem 4 — Electric Potential Difference

Uniform field E = 1000 a_x V/m. Find V_A − V_B where A = (1,0,0) and B = (0,1,0).

**Solution:**
```
V_A - V_B = -∫_B^A E·dl

Choose path: B→(1,1,0)→A (segments along y then along x)

Segment 1 (y varies, x=0→1 at y varies): actually use conservative property.
Simpler: direct integral along any path.

Path: straight from B(0,1,0) to A(1,0,0)
  dl = dx a_x + dy a_y (with dy/dx = -1)
  But easier — use V = -∫E·dl from reference:

  V(x) = -∫₀^x 1000 dx' = -1000x  (taking V=0 at x=0)

  V_A = -1000 × 1 = -1000 V
  V_B = -1000 × 0 = 0 V  (x=0 regardless of y)

  V_A - V_B = -1000 - 0 = -1000 V

B is at higher potential. E points from high to low potential (+x direction). ✓
```

---

### Problem 5 — Parallel-Plate Capacitor

Plates: A = 0.01 m², d = 1 mm, εᵣ = 4. Find C, and V for Q = 1 μC.

**Solution:**
```
C = ε₀εᵣA/d = 8.85×10⁻¹² × 4 × 0.01/10⁻³
  = 8.85×10⁻¹² × 40
  = 354×10⁻¹² F = 354 pF

Voltage for Q = 1 μC:
  V = Q/C = 10⁻⁶/354×10⁻¹² = 2.825 V

Electric field:
  E = V/d = 2.825/10⁻³ = 2825 V/m
```

---

### Problem 6 — Electric Field at Conductor Surface

A conductor has surface charge density ρ_s = 5 μC/m². Find E just outside.

**Solution:**
```
Boundary condition at perfect conductor (normal direction â_n away from conductor):
  E_n = ρ_s/ε₀  (tangential E = 0 inside and at surface)

E = ρ_s/ε₀ â_n = 5×10⁻⁶/8.85×10⁻¹² â_n = 5.65×10⁵ â_n  V/m = 565 kV/m

For a conductor: E is always perpendicular to the surface and equals ρ_s/ε₀.
Inside the conductor: E = 0.
```

---

### Problem 7 — Polarization in a Dielectric

Find P and D for E = 10⁶ V/m in a dielectric with εᵣ = 5.

**Solution:**
```
Electric susceptibility: χ_e = εᵣ - 1 = 4

Polarization:
  P = ε₀ χ_e E = 8.85×10⁻¹² × 4 × 10⁶ = 35.4×10⁻⁶  C/m² = 35.4 μC/m²

Flux density:
  D = ε₀εᵣE = 8.85×10⁻¹² × 5 × 10⁶ = 44.25 μC/m²

Check: D = ε₀E + P = 8.85 + 35.4 = 44.25 μC/m²  ✓
```

---

### Problem 8 — Boundary Conditions at Air–Dielectric Interface

E₁ = 10³ V/m at θ₁ = 45° to interface. Medium 1: air (ε₁=ε₀), Medium 2: εᵣ=4. Find θ₂.

**Solution:**
```
Tangential component (continuous): E₁t = E₁ sin45° = 707 V/m
Normal component:                  E₁n = E₁ cos45° = 707 V/m

Boundary condition (no free surface charge): D₁n = D₂n
  ε₀ E₁n = ε₀εᵣ E₂n
  E₂n = E₁n/εᵣ = 707/4 = 176.8 V/m

Tangential is continuous: E₂t = E₁t = 707 V/m

Refraction angle:
  tan θ₂ = E₂t/E₂n = 707/176.8 = 4.0
  θ₂ = arctan(4) = 76.0°

tan θ₂/tan θ₁ = ε₂/ε₁ = 4  (Snell's law for dielectrics)  ✓
```

---

### Problem 9 — Energy Stored in Capacitor

For C = 354 pF charged to V = 100 V, find stored energy W.

**Solution:**
```
W = CV²/2 = 354×10⁻¹² × 10000/2 = 1.77×10⁻⁶ J = 1.77 μJ

Alternatively using charge: Q = CV = 354×10⁻¹² × 100 = 35.4 nC
  W = Q²/(2C) = (35.4×10⁻⁹)²/(2×354×10⁻¹²)
    = 1.253×10⁻¹⁵/7.08×10⁻¹⁰ = 1.77×10⁻⁶ J  ✓

Or in terms of field energy (A=0.01m², d=1mm, εᵣ=4):
  E = V/d = 10⁵ V/m
  W = (1/2)ε₀εᵣE²(Ad) = 0.5×8.85×10⁻¹²×4×10¹⁰×10⁻⁵ = 1.77 μJ  ✓
```

---

### Problem 10 — Force Between Capacitor Plates

Same capacitor (C=354pF, V=100V, εᵣ=4, A=0.01m²). Find the attractive force between plates.

**Solution:**
```
Electric field inside: E = V/d = 10⁵ V/m

Electrostatic pressure (force per unit area):
  p = D·E/2 = ε₀εᵣE²/2 = 8.85×10⁻¹² × 4 × 10¹⁰/2 = 177 N/m²

Total force:
  F = p × A = 177 × 0.01 = 1.77 N  (attractive)

Alternative using energy: F = -dW/dd (at constant charge)
  W = Q²/(2C) = Q²d/(2ε₀εᵣA)  → F = Q²/(2ε₀εᵣA) = (35.4×10⁻⁹)²/(2×ε₀×4×0.01) ≈ 1.77 N ✓
```

---

### Problem 11 — Equivalent Capacitance

Three capacitors: C₁=10pF, C₂=20pF, C₃=30pF. Find C for (a) all series, (b) all parallel, (c) C₁ series with (C₂ ∥ C₃).

**Solution:**
```
(a) All series:
  1/C = 1/10 + 1/20 + 1/30 = 6/60 + 3/60 + 2/60 = 11/60
  C = 60/11 = 5.45 pF

(b) All parallel:
  C = 10 + 20 + 30 = 60 pF

(c) C₁ in series with (C₂ ∥ C₃):
  C₂₃ = 20 + 30 = 50 pF
  1/C = 1/10 + 1/50 = 5/50 + 1/50 = 6/50
  C = 50/6 = 8.33 pF
```

---

### Problem 12 — Field in a Dielectric Slab

A slab (εᵣ=4, thickness 5mm) sits between two others (εᵣ=1, air). Normal D = 10 μC/m². Find E in each region.

**Solution:**
```
Normal component of D is continuous (no free surface charge):
  D_n = 10 μC/m² everywhere (same value)

E in air (εᵣ=1):   E₁ = D/ε₀ = 10⁻⁵/8.85×10⁻¹² = 1.13 MV/m
E in slab (εᵣ=4):  E₂ = D/(ε₀εᵣ) = 1.13×10⁶/4 = 282.5 kV/m

Voltage across 5mm slab: V = E₂ × d = 282500 × 0.005 = 1412.5 V
```

---

### Problem 13 — Surface Charge on an Isolated Conductor

Isolated conducting sphere, radius a = 0.1 m, raised to V₀ = 1000 V. Find Q and ρ_s.

**Solution:**
```
Capacitance of isolated sphere: C = 4πε₀a = 4π×8.85×10⁻¹²×0.1 = 11.13 pF

Charge: Q = CV₀ = 11.13×10⁻¹² × 1000 = 11.13 nC

Surface charge density (uniform):
  ρ_s = Q/(4πa²) = 11.13×10⁻⁹/(4π×0.01) = 88.5 nC/m²

Check E at surface: E = ρ_s/ε₀ = 88.5×10⁻⁹/8.85×10⁻¹² = 10,000 V/m
Also: E = V₀/a = 1000/0.1 = 10,000 V/m  ✓
```

---

### Problem 14 — Dielectric Sphere in Uniform Field

A dielectric sphere (εᵣ = 3, radius a) is placed in a uniform field E₀. Find E inside.

**Solution:**
```
Exact solution (separation of variables in spherical coordinates):
  E_inside = 3E₀/(εᵣ + 2)

For εᵣ = 3:
  E_inside = 3E₀/(3 + 2) = 3E₀/5 = 0.6 E₀

The field inside is uniform and weaker than the applied field.

For εᵣ → ∞ (conductor): E_inside → 0 (field excluded)
For εᵣ = 1 (no sphere): E_inside → E₀  ✓
For εᵣ = 3: E_inside = 0.6 E₀  (reduced but not zero)
```

---

### Problem 15 — Electrostatic Shielding

Explain why a closed conducting shell provides complete electrostatic shielding. Quantify for copper.

**Solution:**
```
Static shielding (DC):
  By Gauss's law, if no free charge is enclosed, E = 0 everywhere inside
  the conductor and inside the hollow. The conductor redistributes surface
  charges to cancel any external field inside.
  → SE = ∞ for static fields (perfect shielding).

At AC frequency f = 1 GHz, copper (σ = 5.8×10⁷ S/m):
  δ = 2.09 μm  (skin depth)

For shell thickness t = 1 mm >> δ:
  Absorption loss = 8.686 × t/δ = 8.686 × (10⁻³/2.09×10⁻⁶) = 4156 dB

Practical rule: SE ≈ 8.686t/δ (dB) for t >> δ.
For static fields, no thickness is needed — shielding is complete regardless.
```
