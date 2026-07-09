# Chapter 1 — The Electromagnetic Model
## Problems and Solutions

---

### Problem 1 — Convert Charge Units

Convert 1 coulomb to statcoulombs (ESU) and abcoulombs (EMU).

**Solution:**
```
1 C = 3×10⁹  statcoulombs  (ESU/Gaussian)
1 C = 0.1     abcoulombs    (EMU)

Origin: In CGS-ESU, F = q₁q₂/r², whereas SI uses F = q₁q₂/(4πε₀r²).
The factor 3×10⁹ comes from c = 2.998×10¹⁰ cm/s ≈ 3×10¹⁰ cm/s.
```

---

### Problem 2 — Speed of Light in Different Unit Systems

Express c in m/s, cm/s, ft/ns, and km/s.

**Solution:**
```
c = 2.998×10⁸  m/s     ≈ 3×10⁸  m/s
c = 2.998×10¹⁰ cm/s    ≈ 3×10¹⁰ cm/s
c = 2.998×10⁵  km/s    ≈ 3×10⁵  km/s
c = 0.9836 ft/ns        ≈ 1 ft/ns  (useful for digital circuit delays)
c = 186,282 miles/s     ≈ 186,000 miles/s

Practical note: a signal travels ~1 foot per nanosecond in free space
(~6 inches/ns in PCB traces with εᵣ ≈ 4).
```

---

### Problem 3 — Coulomb Force Between Two Charges

Find the force between two point charges Q₁ = Q₂ = 1 μC separated by r = 1 m.

**Solution:**
```
F = Q₁Q₂/(4πε₀r²)
  = (10⁻⁶)²/(4π × 8.85×10⁻¹² × 1²)
  = 10⁻¹²/(1.113×10⁻¹⁰)
  = 8.99×10⁻³ N ≈ 9 mN  (repulsive)

Using k = 1/(4πε₀) = 8.99×10⁹  N·m²/C²:
  F = k Q₁Q₂/r² = 8.99×10⁹ × 10⁻¹² = 8.99×10⁻³ N  ✓
```

---

### Problem 4 — Relationship Between ε₀ and μ₀

Derive ε₀μ₀ = 1/c² and verify numerically.

**Solution:**
```
From Maxwell's equations, the wave equation gives:
  c = 1/√(ε₀μ₀)  →  ε₀μ₀ = 1/c²

Numerical verification:
  ε₀ = 8.854×10⁻¹²  F/m
  μ₀ = 4π×10⁻⁷ = 1.2566×10⁻⁶  H/m

  ε₀μ₀ = 8.854×10⁻¹² × 1.2566×10⁻⁶ = 1.1127×10⁻¹⁷  s²/m²

  1/c² = 1/(2.998×10⁸)² = 1/8.988×10¹⁶ = 1.1127×10⁻¹⁷  s²/m²  ✓
```

---

### Problem 5 — Convert Current Units

Convert 1 ampere to statamperes and abamperes.

**Solution:**
```
1 A = 3×10⁹  statamperes  (ESU)
1 A = 0.1    abamperes     (EMU)

Note: 1 abampere = 10 A (so 1 A = 0.1 abampere)

These follow from Q = I×t and the charge conversions in Problem 1.
```

---

### Problem 6 — Energy Density in an Electromagnetic Wave

A plane wave in free space has E₀ = 100 V/m. Find the electric and magnetic energy densities.

**Solution:**
```
Electric energy density:
  u_e = ε₀E₀²/2 = 8.85×10⁻¹² × 10⁴/2 = 4.43×10⁻⁸  J/m³

H₀ = E₀/η₀ = 100/377 = 0.265  A/m

Magnetic energy density:
  u_m = μ₀H₀²/2 = 4π×10⁻⁷ × 0.0702/2 = 4.43×10⁻⁸  J/m³

u_e = u_m  ✓  (equal in a plane wave)

Total: u = ε₀E₀² = 8.85×10⁻⁸  J/m³
```

---

### Problem 7 — Power Density

For the wave in Problem 6, find the Poynting vector magnitude.

**Solution:**
```
S = E₀ × H₀ = E₀²/η₀  (time-average = peak/2 for sinusoidal)

Peak: S_peak = 100 × 0.265 = 26.5  W/m²

Time-average: ⟨S⟩ = E₀²/(2η₀) = 10000/(2×377) = 13.26  W/m²

Also: ⟨S⟩ = u_total × c / 2 = 8.85×10⁻⁸ × 3×10⁸/2 = 13.3  W/m²  ✓
```

---

### Problem 8 — Dimensional Consistency of Maxwell's Equations

Verify ∇ × E = −∂B/∂t and ∇ × H = J + ∂D/∂t are dimensionally consistent.

**Solution:**
```
∇ × E = -∂B/∂t:
  LHS: [∇×E] = [E]/[m] = (V/m)/m = V/m²
  RHS: [∂B/∂t] = [T]/[s] = (V·s/m²)/s = V/m²  ✓

∇ × H = J + ∂D/∂t:
  LHS: [∇×H] = (A/m)/m = A/m²
  RHS (J): [J] = A/m²  ✓
  RHS (∂D/∂t): [D]/[t] = (C/m²)/s = A/m²  ✓

∇ · D = ρ_v:
  [∇·D] = (C/m²)/m = C/m³ = [ρ_v]  ✓
```

---

### Problem 9 — Electric Field Unit Conversions

Convert E = 1 kV/m to (a) N/C, (b) V/cm, (c) force on a 1 μC charge.

**Solution:**
```
(a) 1 V/m = 1 N/C  (by definition, since V = J/C = N·m/C)
    → 1 kV/m = 1000 N/C

(b) 1 kV/m = 1000 V/m = 10 V/cm

(c) Force: F = qE = 10⁻⁶ × 1000 = 10⁻³ N = 1 mN
```

---

### Problem 10 — Magnetic Field Unit Conversions

Convert B = 1 T to Gauss and find H in free space.

**Solution:**
```
1 T = 10⁴ Gauss = 1 Wb/m²

H in free space (μᵣ = 1):
  H = B/μ₀ = 1/(4π×10⁻⁷) = 7.958×10⁵  A/m

For B = 0.5 T (typical MRI magnet):
  H = 3.98×10⁵  A/m
  H in Oersteds: 1 A/m = 4π×10⁻³ Oe → H = 4997 Oe ≈ 5000 Oe
```

---

### Problem 11 — Impedance of Free Space

Derive η₀ = √(μ₀/ε₀) and verify it equals 120π Ω.

**Solution:**
```
η₀ = √(μ₀/ε₀) = √(4π×10⁻⁷ / 8.85×10⁻¹²)
   = √(1.420×10⁵)
   = 376.7 Ω

Alternative derivation:
  η₀ = μ₀c = 4π×10⁻⁷ × 3×10⁸ = 4π×30 = 120π ≈ 376.99 Ω

120π = 376.99 Ω  ✓

Useful: η₀ ≈ 377 Ω for quick calculations.
```

---

### Problem 12 — Verify c = 1/√(ε₀μ₀)

Calculate 1/√(ε₀μ₀) from the SI values of ε₀ and μ₀.

**Solution:**
```
ε₀ = 8.854×10⁻¹²  F/m
μ₀ = 4π×10⁻⁷ = 1.2566×10⁻⁶  H/m

ε₀ × μ₀ = 8.854×10⁻¹² × 1.2566×10⁻⁶ = 11.13×10⁻¹⁸  s²/m²

1/√(ε₀μ₀) = 1/√(11.13×10⁻¹⁸) = 1/(3.337×10⁻⁹) = 2.998×10⁸  m/s = c  ✓

This confirms: the values of ε₀ and μ₀ are not independent —
they are linked through the measured speed of light.
```

---

### Problem 13 — Energy Density Units

For E = 1 MV/m in free space, compute u_e in J/m³, erg/cm³, and eV/m³.

**Solution:**
```
u_e = ε₀E²/2 = 8.85×10⁻¹² × (10⁶)²/2 = 8.85×10⁻¹² × 10¹²/2 = 4.425  J/m³

Convert to CGS: 1 J/m³ = 10 erg/cm³
  u_e = 4.425 × 10 = 44.25  erg/cm³

Convert to eV/m³: 1 J = 1/(1.602×10⁻¹⁹) eV = 6.242×10¹⁸  eV
  u_e = 4.425 × 6.242×10¹⁸ = 2.76×10¹⁹  eV/m³
```

---

### Problem 14 — Coulomb's Constant

Express k = 1/(4πε₀) in SI units and verify its numerical value.

**Solution:**
```
k = 1/(4πε₀)
  = 1/(4π × 8.854×10⁻¹²)
  = 1/(1.1127×10⁻¹⁰)
  = 8.988×10⁹  N·m²/C²

Also: k = c² × 10⁻⁷ = (3×10⁸)² × 10⁻⁷ = 9×10¹⁶ × 10⁻⁷ = 9×10⁹  N·m²/C²

Units: [k] = N·m²/C² = V·m/C = kg·m³/(A²·s⁴)
```

---

### Problem 15 — E/H Ratio in a Plane Wave

A plane wave in free space has H = 1 A/m. Find E, power density, and compare E/H to η₀.

**Solution:**
```
E = η₀ × H = 377 × 1 = 377  V/m

E/H = η₀ = 377 Ω  (intrinsic impedance of free space)

Time-average Poynting vector:
  ⟨S⟩ = (1/2) E₀ H₀ = (1/2) × 377 × 1 = 188.5  W/m²

Or: ⟨S⟩ = η₀H₀²/2 = 377/2 = 188.5  W/m²

Also: ⟨S⟩ = E₀²/(2η₀) = 377²/(2×377) = 377/2 = 188.5  W/m²  ✓
```
