# Chapter 5 — Steady Electric Currents
## Problems and Solutions

---

### Problem 1 — Current Density from Current

A copper wire (diameter 2 mm) carries I = 10 A. Find the current density J.

**Solution:**
```
Cross-sectional area:
  A = π(d/2)² = π(10⁻³)² = π×10⁻⁶ = 3.14×10⁻⁶  m²

Current density:
  J = I/A = 10/(3.14×10⁻⁶) = 3.18×10⁶  A/m²

For reference: copper fusing current density ≈ 10⁸ A/m² for short pulses.
Safe continuous rating ≈ 10⁶ A/m² for bare copper.
```

---

### Problem 2 — Resistance via Ohm's Law (Microscopic)

Copper (σ = 5.8×10⁷ S/m) wire: length L = 1 m, diameter d = 2 mm. Find R.

**Solution:**
```
R = L/(σA) = L/(σ π(d/2)²)
  = 1/(5.8×10⁷ × π×10⁻⁶)
  = 1/(5.8×10⁷ × 3.14×10⁻⁶)
  = 1/(182.1)
  = 5.49×10⁻³ Ω = 5.49 mΩ

Resistivity: ρ = 1/σ = 1/5.8×10⁷ = 1.72×10⁻⁸  Ω·m = 17.2 nΩ·m
R = ρL/A = 1.72×10⁻⁸ × 1/3.14×10⁻⁶ = 5.48 mΩ  ✓
```

---

### Problem 3 — EMF in a Circuit

Two batteries in series: V₁=12V (internal r₁=0.5Ω) and V₂=9V (internal r₂=1Ω), external R=10Ω.
Find I and terminal voltages.

**Solution:**
```
Total EMF: V_total = 12 + 9 = 21 V  (aiding)
Total resistance: R_total = r₁ + r₂ + R = 0.5 + 1 + 10 = 11.5 Ω

I = V_total/R_total = 21/11.5 = 1.826 A

Terminal voltage of V₁: V_T1 = 12 - I×r₁ = 12 - 1.826×0.5 = 11.09 V
Terminal voltage of V₂: V_T2 = 9 - I×r₂ = 9 - 1.826×1 = 7.17 V
Voltage across R: V_R = I×R = 1.826×10 = 18.26 V

Check: V_T1 + V_T2 = 11.09 + 7.17 = 18.26 = V_R  ✓
```

---

### Problem 4 — Kirchhoff's Voltage Law Verification

Circuit: V=24V, R₁=4Ω, R₂=8Ω in series. Verify KVL.

**Solution:**
```
I = V/(R₁+R₂) = 24/12 = 2 A

Voltage drops:
  V_R1 = I×R₁ = 2×4 = 8 V
  V_R2 = I×R₂ = 2×8 = 16 V

KVL (around loop, clockwise):
  -V + V_R1 + V_R2 = 0
  -24 + 8 + 16 = 0  ✓

Power balance:
  P_source = V×I = 24×2 = 48 W
  P_R1 = I²R₁ = 4×4 = 16 W
  P_R2 = I²R₂ = 4×8 = 32 W
  P_R1 + P_R2 = 48 W = P_source  ✓
```

---

### Problem 5 — Kirchhoff's Current Law

Node with currents: I₁=5A (in), I₂=3A (in), I₃=? (out), I₄=2A (out). Find I₃.

**Solution:**
```
KCL (sum of currents in = sum of currents out):
  I₁ + I₂ = I₃ + I₄
  5 + 3 = I₃ + 2
  I₃ = 6 A

Alternatively (sum of all currents at node = 0):
  +I₁ + I₂ - I₃ - I₄ = 0
  +5 + 3 - I₃ - 2 = 0
  I₃ = 6 A  ✓

Physically: current cannot accumulate at a node (steady state).
```

---

### Problem 6 — Power Dissipation (Joule's Law)

Resistor: R = 100 Ω, V = 50 V. Find P, I, and energy in 1 hour.

**Solution:**
```
I = V/R = 50/100 = 0.5 A

P = V²/R = 2500/100 = 25 W
P = I²R = 0.25×100 = 25 W  ✓
P = VI = 50×0.5 = 25 W  ✓

Energy in 1 hour:
  W = P × t = 25 × 3600 = 90,000 J = 90 kJ = 0.025 kWh

Temperature check: for resistor rated at 25 W, this is at full rated power.
```

---

### Problem 7 — Resistance of a Conical Conductor

Truncated cone: conductivity σ, small radius a, large radius b, length L, axis along z. Find R.

**Solution:**
```
Radius varies linearly: r(z) = a + (b-a)z/L

Cross-sectional area at z: A(z) = πr(z)²

Differential resistance: dR = dz/(σ A(z)) = dz/(σ π r(z)²)

R = ∫₀^L dz/(σ π [a + (b-a)z/L]²)

Let u = a + (b-a)z/L,  du = (b-a)/L dz:
  R = (L/(b-a)) ∫_a^b du/(σπu²)
    = (L/(b-a)) × [1/(σπu)]_a^b × (-1) ...

  R = L/((b-a)σπ) × [-1/u]_a^b
    = L/((b-a)σπ) × (1/a - 1/b)
    = L/((b-a)σπ) × (b-a)/(ab)

R = L/(σπab)

For a=b (cylinder): apply L'Hopital → R = L/(σπa²)  ✓
```

---

### Problem 8 — Boundary Conditions for J at Interface

Medium 1 (σ₁ = 10⁶ S/m) and Medium 2 (σ₂ = 10³ S/m). J₁ = 5×10⁶ A/m² at θ₁ = 30° to interface normal. Find J₂ and θ₂.

**Solution:**
```
Boundary conditions (steady current):
  Normal: J₁n = J₂n  (continuity of normal current density)
  Tangential: E₁t = E₂t  →  J₁t/σ₁ = J₂t/σ₂

J₁n = J₁ cos30° = 5×10⁶ × 0.866 = 4.33×10⁶  A/m²
J₁t = J₁ sin30° = 5×10⁶ × 0.5   = 2.5×10⁶   A/m²

Normal component continuous:
  J₂n = J₁n = 4.33×10⁶  A/m²

Tangential component:
  J₂t = (σ₂/σ₁) J₁t = (10³/10⁶) × 2.5×10⁶ = 2500  A/m²

J₂ = √(J₂n² + J₂t²) = √((4.33×10⁶)² + 2500²) ≈ 4.33×10⁶  A/m²

tan θ₂ = J₂t/J₂n = 2500/(4.33×10⁶) = 5.77×10⁻⁴
θ₂ ≈ 0.033°  (nearly normal — current crowds into normal direction in low-σ medium)

tan θ₂/tan θ₁ = σ₂/σ₁ = 10⁻³  ✓
```

---

### Problem 9 — Resistance of a Cylindrical Shell

Cylindrical shell: inner radius a=1cm, outer radius b=3cm, length L=10cm, σ = 10³ S/m, current flows radially. Find R.

**Solution:**
```
For radial current flow in cylindrical geometry:

dR = dρ/(σ × 2πρL)  (shell of thickness dρ, area 2πρL)

R = ∫_a^b dρ/(2πσLρ) = ln(b/a)/(2πσL)
  = ln(3)/(2π × 10³ × 0.1)
  = 1.099/(628.3)
  = 1.75×10⁻³ Ω = 1.75 mΩ

For axial current flow: R = L/(σπ(b²-a²))
  = 0.1/(10³ × π × (9-1)×10⁻⁴)
  = 0.1/(2.513) = 39.8 mΩ
```

---

### Problem 10 — Current Distribution in a Conducting Sphere

Uniform conductivity sphere, radius a, uniform E₀ applied externally. Find J inside.

**Solution:**
```
Inside a conducting sphere in a uniform field, if the sphere is in a medium of
conductivity σ₁ surrounded by a medium of conductivity σ₂:

J_inside = 3σ₁/(σ₁+2σ₂) × σ₂ × E₀ ...

For the simpler case: solid homogeneous conductor (σ uniform):
  J = σE (Ohm's law)
  E_inside = E₀  (same as applied if conductivities match)

For a highly conductive sphere (σ → ∞) in a resistive medium:
  E_inside → 0 (field excluded from perfect conductor)
  J → concentrated on surface

For σ_sphere = σ_medium:
  J = σE₀  (uniform, undisturbed)
```

---

### Problem 11 — Continuity Equation

Charge density ρ_v = ρ₀ e^(-t/τ) uniformly distributed in a medium (σ, ε). Find J and verify continuity.

**Solution:**
```
Continuity equation: ∂ρ_v/∂t + ∇·J = 0

∂ρ_v/∂t = -ρ₀/τ × e^(-t/τ)

From ∇·J = -∂ρ_v/∂t = ρ₀/τ × e^(-t/τ)

For ohmic medium: J = σE = σD/ε → ∇·J = σ/ε × ∇·D = σ/ε × ρ_v
  σ/ε × ρ₀ e^(-t/τ) = ρ₀/τ × e^(-t/τ)
  → τ = ε/σ  (relaxation time)

For copper: τ = ε₀/σ = 8.85×10⁻¹²/5.8×10⁷ ≈ 1.5×10⁻¹⁹ s  (extremely fast)
For seawater: τ ≈ ε₀×80/4 ≈ 1.8×10⁻¹⁰ s = 0.18 ns
For glass: τ ≈ hours (charges persist)
```

---

### Problem 12 — Resistance Between Two Electrodes

Two spherical electrodes (radius a = 5 mm) buried in earth (σ = 10⁻² S/m), separation D = 1 m (D >> a). Find R.

**Solution:**
```
For two spherical electrodes in a conducting medium (D >> a):
  R ≈ 2 × [1/(4πσa)] - 1/(2πσD)
  ≈ 1/(2πσa)  when D >> a

R ≈ 1/(2πσa) = 1/(2π × 10⁻² × 5×10⁻³) = 1/(3.14×10⁻⁴) = 3183 Ω ≈ 3.18 kΩ

Full expression:
  R = 1/(2πσ) × (1/a - 1/D)
    = 1/(2π×10⁻²) × (1/0.005 - 1/1.0)
    = 15.92 × (200 - 1)
    = 15.92 × 199
    = 3168 Ω ≈ 3.17 kΩ
```

---

### Problem 13 — Equivalent Resistance of Network

Find equivalent resistance: R₁=6Ω, R₂=3Ω in parallel, that combination in series with R₃=4Ω.

**Solution:**
```
R₁₂ (parallel): 1/R₁₂ = 1/6 + 1/3 = 1/6 + 2/6 = 3/6
  R₁₂ = 2 Ω

R_total = R₁₂ + R₃ = 2 + 4 = 6 Ω

For V=12V across whole network:
  I_total = 12/6 = 2 A
  V_R3 = 2×4 = 8 V
  V_R12 = 2×2 = 4 V
  I_R1 = 4/6 = 0.667 A
  I_R2 = 4/3 = 1.333 A
  Check: 0.667 + 1.333 = 2 A  ✓
```

---

### Problem 14 — Current Density in a Tapered Conductor

Conductor tapers linearly from radius a to 2a over length L. Uniform current I flows axially. Find J(z) and E(z).

**Solution:**
```
Radius at position z: r(z) = a(1 + z/L)  for 0 ≤ z ≤ L

Area: A(z) = πr(z)² = πa²(1 + z/L)²

J(z) = I/A(z) = I/[πa²(1 + z/L)²]

At z=0: J = I/(πa²)
At z=L: J = I/(4πa²) = J(z=0)/4

E(z) = J(z)/σ = I/[σπa²(1 + z/L)²]

Voltage across conductor:
  V = ∫₀^L E dz = I/(σπa²) ∫₀^L dz/(1+z/L)²

  Let u = 1+z/L: V = I/(σπa²) × L ∫₁^2 u⁻² du = IL/(σπa²) × [-1/u]₁²
    = IL/(σπa²) × (1 - 1/2) = IL/(2σπa²)

R = V/I = L/(2σπa²)  [compare to uniform wire: R = L/(σπa²), so tapered R is halved]
```

---

### Problem 15 — Power Loss in a Transmission Line

Two-wire line: conductor radius a=1mm, separation D=10mm, σ_c=5.8×10⁷ S/m, length L=100m, I=10A. Find P_loss.

**Solution:**
```
Resistance per unit length (two wires in series):
  R/L = 2/(σ_c πa²)
      = 2/(5.8×10⁷ × π × 10⁻⁶)
      = 2/(182.2)
      = 10.98×10⁻³  Ω/m ≈ 11 mΩ/m

Total resistance: R = 10.98×10⁻³ × 100 = 1.098 Ω

Power loss: P = I²R = 100 × 1.098 = 109.8 W

At 50Hz with skin effect correction (δ=9.3mm >> a=1mm for 50Hz):
  Skin effect negligible at power frequency for this wire size.
  (At 100MHz, δ=6.6μm << a, and AC resistance increases significantly)
```
