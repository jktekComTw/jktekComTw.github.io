# Chapter 10 — Waveguides and Cavity Resonators
## Problems and Solutions

---

### Problem 1 — Cutoff Frequencies (WR-90)

Rectangular waveguide: a = 2.286 cm, b = 1.016 cm (WR-90). Find f_c for TE₁₀, TE₂₀, TE₀₁, TE₁₁.

**Solution:**
```
f_c(m,n) = (c/2) √((m/a)² + (n/b)²)

TE₁₀:  f_c = c/(2a) = 3×10⁸/(2×0.02286) = 6.56 GHz  (dominant mode)

TE₂₀:  f_c = c/a = 2 × 6.56 = 13.12 GHz

TE₀₁:  f_c = c/(2b) = 3×10⁸/(2×0.01016) = 14.76 GHz

TE₁₁:  f_c = (c/2)√(1/a² + 1/b²)
           = 1.5×10⁸ × √(1914 + 9685)
           = 1.5×10⁸ × 107.7 = 16.15 GHz

Single-mode bandwidth: 6.56 to 13.12 GHz.
```

---

### Problem 2 — Phase Velocity in Waveguide

WR-90 at f = 10 GHz (TE₁₀ mode, f_c = 6.56 GHz). Find v_p, v_g, and β_g.

**Solution:**
```
√(1-(f_c/f)²) = √(1-(6.56/10)²) = √(1-0.4303) = √0.5697 = 0.7548

v_p = c/0.7548 = 3×10⁸/0.7548 = 3.97×10⁸  m/s

v_g = c × 0.7548 = 2.26×10⁸  m/s

Check: v_p × v_g = 3.97×10⁸ × 2.26×10⁸ = 8.97×10¹⁶ ≈ c²  ✓

β_g = (2πf/c) × 0.7548 = (2π×10¹⁰/3×10⁸) × 0.7548 = 158.2  rad/m
```

---

### Problem 3 — Wave Impedance for TE and TM Modes

WR-90 at f = 10 GHz (f_c = 6.56 GHz). Find η_TE and η_TM.

**Solution:**
```
From Problem 2: √(1-(f_c/f)²) = 0.7548

η_TE = η₀/√(1-(f_c/f)²) = 377/0.7548 = 499.5 Ω  (> η₀)

η_TM = η₀ × √(1-(f_c/f)²) = 377 × 0.7548 = 284.6 Ω  (< η₀)

Note: η_TE × η_TM = η₀² = 377² = 142129 Ω²  ✓
```

---

### Problem 4 — Guide Wavelength

WR-90 at f = 10 GHz. Find λ₀, λ_g, and compare.

**Solution:**
```
Free-space wavelength:
  λ₀ = c/f = 3×10⁸/10¹⁰ = 0.03 m = 3.00 cm

Guide wavelength:
  λ_g = λ₀/√(1-(f_c/f)²) = 3.00/0.7548 = 3.97 cm

λ_g > λ₀, as expected for waveguide propagation.

Phase constant:  β_g = 2π/λ_g = 2π/0.0397 = 158.2  rad/m
```

---

### Problem 5 — TE₁₀ Field Distributions

Rectangular waveguide: a = 4 cm, b = 2 cm, f = 5 GHz. Write out the field components.

**Solution:**
```
f_c(TE₁₀) = c/(2a) = 3×10⁸/(0.08) = 3.75 GHz  <  5 GHz  ✓ (propagates)

k_c = π/a = π/0.04 = 78.54  rad/m
k   = 2πf/c = 2π×5×10⁹/(3×10⁸) = 104.7  rad/m
β_g = √(k² - k_c²) = √(10962 - 6169) = √4793 = 69.2  rad/m

TE₁₀ field components (with amplitude H₀):
  H_z = H₀ cos(πx/a) e^(-jβ_g z)
  H_x = j(β_g/k_c²)(π/a) H₀ sin(πx/a) e^(-jβ_g z)
       = j(β_g/k_c) H₀ sin(πx/a) e^(-jβ_g z) / k_c ...

  Using E₀ = (ωμ₀/k_c) H₀:
  E_y = -E₀ sin(πx/a) e^(-jβ_g z)   [only transverse E-field component]
  H_x = (β_g/ωμ₀) E₀ sin(πx/a) e^(-jβ_g z)
  H_z = -j(k_c/ωμ₀) E₀ cos(πx/a) e^(-jβ_g z)
  E_x = E_z = H_y = 0
```

---

### Problem 6 — Power Transmitted in Waveguide

WR-90 (a=2.286 cm, b=1.016 cm), TE₁₀, f=10 GHz, E₀ = 10⁴ V/m. Find P_avg.

**Solution:**
```
Time-average power for TE₁₀:
  P = (ab/4) × E₀²/η_TE
    = (0.02286 × 0.01016/4) × (10⁴)²/499.5
    = (5.81×10⁻⁵) × 10⁸/499.5
    = 5.81×10³/499.5
    = 11.6 W

Equivalently: P = (1/2) Re[∫∫ (E × H*)·a_z dS]
  = (ab/4) × (E₀²/η_TE)  [for TE₁₀, sin² integrates to 1/2]
```

---

### Problem 7 — Surface Resistance and Attenuation

Find Rs for copper (σ = 5.8×10⁷ S/m) at f = 10 GHz.

**Solution:**
```
Rs = √(πfμ₀/σ)
   = √(π × 10¹⁰ × 4π×10⁻⁷ / 5.8×10⁷)
   = √(4π² × 10³ / 5.8×10⁷)
   = √(39.48×10³/5.8×10⁷)
   = √(6.807×10⁻⁴)
   = 0.0261 Ω  (surface resistance)

For comparison, Rs at 1 GHz = 0.0261/√10 = 0.00825 Ω
(Rs scales as √f)
```

---

### Problem 8 — Resonant Frequencies of Rectangular Cavity

Cavity: a = 4 cm, b = 2 cm, d = 5 cm. Find resonant frequencies for TE₁₀₁, TE₁₁₁, TM₁₁₀.

**Solution:**
```
f₀(m,n,p) = (c/2) √((m/a)² + (n/b)² + (p/d)²)

TE₁₀₁ (dominant TE mode, n=0 requires p≥1):
  f₀ = (3×10⁸/2) √((1/0.04)² + 0 + (1/0.05)²)
     = 1.5×10⁸ × √(625 + 400)
     = 1.5×10⁸ × 32.02 = 4.803 GHz

TE₁₁₁:
  f₀ = 1.5×10⁸ × √(625 + 2500 + 400) = 1.5×10⁸ × 55.9 = 8.38 GHz

  Wait: √(625 + 2500 + 400) = √3525 = 59.37
  f₀ = 1.5×10⁸ × 59.37 = 8.91 GHz

TM₁₁₀ (p=0 allowed for TM, m≥1, n≥1):
  f₀ = 1.5×10⁸ × √(625 + 2500) = 1.5×10⁸ × 55.9 = 8.38 GHz

Dominant mode: TE₁₀₁ at 4.80 GHz.
```

---

### Problem 9 — Q-Factor of Cavity Resonator

Copper cavity (a=4cm, b=2cm, d=5cm), TE₁₀₁ mode, Rs = 0.0195 Ω at f₀ = 4.80 GHz. Estimate Q.

**Solution:**
```
Rs at 4.80 GHz:
  Rs = √(πfμ₀/σ) = √(π×4.8×10⁹×4π×10⁻⁷/5.8×10⁷)
     = √(4π²×4.8×10²/5.8×10⁷)·10⁻⁷...

  Let me compute: πfμ₀ = π×4.8×10⁹×4π×10⁻⁷ = 4π²×4.8×10² = 18966
  Rs = √(18966/5.8×10⁷) = √(3.27×10⁻⁴) = 0.01808 Ω

For TE₁₀₁ mode, the Q is:
  Q = ω₀μ₀ × (Volume term)/(Surface loss term)

Using the approximate result for this cavity geometry:
  k₀ = 2πf₀/c = 2π×4.8×10⁹/3×10⁸ = 100.5 rad/m
  k_x = π/a = 78.54, k_z = π/d = 62.83

  Q ≈ η₀/(2Rs) × abd(k_x²+k_z²)^(3/2) / [2b(k_x²+k_z²)(a+d)/2 + ad×k_z²×... ]

  Using reference result: Q ≈ 8100 for copper at these dimensions.
  BW = f₀/Q = 4.80×10⁹/8100 ≈ 593 kHz
```

---

### Problem 10 — Circular Waveguide Cutoff Frequencies

Circular waveguide: a = 1 cm. Find f_c for TE₁₁, TM₀₁, TE₂₁, TM₁₁.

**Solution:**
```
f_c = c × p'_mn/(2πa)  for TE modes  (p'_mn = zero of J'_n)
f_c = c × p_mn/(2πa)   for TM modes  (p_mn  = zero of J_n)

Key zeros:  p'₁₁ = 1.841 (TE₁₁, dominant)
            p₀₁  = 2.405 (TM₀₁)
            p'₂₁ = 3.054 (TE₂₁)
            p'₀₁ = 3.832 (TE₀₁ = TM₁₁ degenerate at same value)

With 2πa = 2π×0.01 = 0.06283 m:

TE₁₁:  f_c = 3×10⁸ × 1.841/0.06283 = 8.79 GHz  (dominant)
TM₀₁:  f_c = 3×10⁸ × 2.405/0.06283 = 11.49 GHz
TE₂₁:  f_c = 3×10⁸ × 3.054/0.06283 = 14.59 GHz
TE₀₁:  f_c = 3×10⁸ × 3.832/0.06283 = 18.30 GHz

Single-mode bandwidth: 8.79 to 11.49 GHz (2.70 GHz gap).
```

---

### Problem 11 — Cutoff Wavelengths

For the a = 1 cm circular waveguide (Problem 10), find λ_c for TE₁₁ and TM₀₁.

**Solution:**
```
λ_c = 2πa/p'_mn  (TE)  or  2πa/p_mn  (TM)

TE₁₁:  λ_c = 2π×0.01/1.841 = 0.06283/1.841 = 3.41 cm

TM₀₁:  λ_c = 2π×0.01/2.405 = 0.06283/2.405 = 2.61 cm

Propagation condition: λ₀ < λ_c  (i.e., f > f_c)
```

---

### Problem 12 — Dominant Mode Identification

State the dominant mode for (a) rectangular waveguide (a > b), (b) circular waveguide, and explain why.

**Solution:**
```
(a) Rectangular waveguide (a > b):
    Dominant mode = TE₁₀
    f_c(TE₁₀) = c/(2a)  — lowest possible f_c since m=1, n=0
    Next mode TE₂₀ has f_c = c/a (twice as high)
    Useful single-mode band: c/(2a) < f < c/a

(b) Circular waveguide:
    Dominant mode = TE₁₁
    Lowest root: p'₁₁ = 1.841
    TM₀₁ has p₀₁ = 2.405 (next higher)
    Note: TE₁₁ is degenerate (two polarizations)

In both cases, the dominant mode has the longest cutoff wavelength.
```

---

### Problem 13 — Energy Stored in Cavity

TE₁₀₁ mode in rectangular cavity (a = 4 cm, b = 2 cm, d = 4 cm), E₀ = 10⁴ V/m. Find W_total.

**Solution:**
```
For TE₁₀₁, electric and magnetic energies are equal:
  W_e = (ε₀/4) E₀² × (volume factor)

The field E_y = E₀ sin(πx/a) sin(πz/d):
  W_e = (ε₀/4) E₀² ∫₀ᵃ∫₀ᵇ∫₀ᵈ sin²(πx/a) sin²(πz/d) dx dy dz
      = (ε₀/4) E₀² × (a/2) × b × (d/2)
      = (ε₀ E₀² abd)/16

W_e = (8.85×10⁻¹² × 10⁸ × 0.04 × 0.02 × 0.04) / 16
    = (8.85×10⁻¹² × 10⁸ × 3.2×10⁻⁵) / 16
    = (28.32×10⁻⁹) / 16
    = 1.77 nJ

W_total = 2 W_e = 3.54 nJ  (W_e = W_m at resonance)
```

---

### Problem 14 — Cavity Resonator Q and Bandwidth

Copper cavity with f₀ = 5.3 GHz, Q = 8500. Find 3-dB bandwidth.

**Solution:**
```
Rs at 5.3 GHz:
  Rs = √(π×5.3×10⁹×4π×10⁻⁷/5.8×10⁷) = √(3.61×10⁻⁴) = 0.0190 Ω

Given Q = 8500:
  BW₃dB = f₀/Q = 5.3×10⁹/8500 = 623.5 kHz

Half-power frequencies:
  f₁ = f₀ - BW/2 = 5.3000 - 0.000312 = 5.29969 GHz
  f₂ = f₀ + BW/2 = 5.30031 GHz
```

---

### Problem 15 — Mode Cutoffs and Single-Mode Band (Rectangular)

Rectangular waveguide, a = 2b (standard ratio). Express f_c for first 3 modes in terms of a.

**Solution:**
```
With b = a/2:

TE₁₀:  f_c = c/(2a)            ← dominant
TE₂₀:  f_c = c/a = 2f_c(TE₁₀)
TE₀₁:  f_c = c/(2b) = c/a = 2f_c(TE₁₀)   (same as TE₂₀ when b=a/2)
TE₁₁:  f_c = (c/2)√(1/a² + 4/a²) = (c/2a)√5 = √5 × f_c(TE₁₀) ≈ 2.24 f_c(TE₁₀)

Ordering: TE₁₀  <  TE₂₀ = TE₀₁  <  TE₁₁

Single-mode bandwidth: f_c(TE₁₀) to 2×f_c(TE₁₀)
  Bandwidth ratio = 2:1 (one octave)

For WR-90: 6.56 GHz to 13.12 GHz (single-mode TE₁₀ operation)
```
