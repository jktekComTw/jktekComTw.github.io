# Chapter 11 — Antennas and Radiating Systems
## Problems and Solutions

---

### Problem 1 — Radiation Resistance of Short Dipole

Hertzian dipole: l = λ/50 at f = 1 GHz (λ = 0.3 m). Find R_rad, P_rad for I₀ = 1 A.

**Solution:**
```
R_rad = 80π² (l/λ)²
      = 80 × 9.870 × (1/50)²
      = 789.6/2500
      = 0.316 Ω

P_rad = (1/2) I₀² R_rad = 0.5 × 1² × 0.316 = 0.158 W
```

---

### Problem 2 — Radiation Pattern of Elemental Dipole

For a z-directed Hertzian dipole, state the E-plane and H-plane patterns and find HPBW.

**Solution:**
```
Normalized power pattern:  U(θ) = sin²(θ)

E-plane (plane containing dipole axis, e.g. xz-plane, φ = 0):
  Pattern: F(θ) = sin²(θ)
  Maximum at θ = 90° (broadside)
  Nulls at θ = 0°, 180° (along axis)
  Half-power: sin²(θ) = 0.5  →  θ = 45°, 135°
  HPBW = 135° - 45° = 90°

H-plane (equatorial plane, θ = 90°):
  Pattern: F = 1 (constant, omnidirectional circle)
  No directivity in H-plane

Directivity: D = 1.5 (3/2) = 1.76 dBi
```

---

### Problem 3 — Directivity from Radiation Pattern

An antenna has pattern U = U₀ cos²θ for 0 ≤ θ ≤ π/2, zero in lower hemisphere. Find D.

**Solution:**
```
Total radiated power:
  P_rad = ∫∫ U dΩ = ∫₀^(π/2) ∫₀^(2π) U₀ cos²θ sinθ dφ dθ
        = 2π U₀ ∫₀^(π/2) cos²θ sinθ dθ

Let u = cosθ, du = -sinθ dθ:
  = 2π U₀ ∫₀¹ u² du = 2π U₀ [u³/3]₀¹ = 2π U₀/3

Maximum intensity: U_max = U₀  (at θ = 0)

D = 4π U_max / P_rad = 4π U₀ / (2π U₀/3) = 4π × 3/(2π) = 6

D = 6 = 7.78 dBi
```

---

### Problem 4 — Effective Aperture

Half-wave dipole (D = 1.64) at f = 3 GHz (λ = 0.1 m). Find A_eff.

**Solution:**
```
A_eff = D λ²/(4π)
      = 1.64 × (0.1)²/(4π)
      = 1.64 × 0.01/12.566
      = 0.01640/12.566
      = 1.305×10⁻³ m²  = 13.05 cm²
```

---

### Problem 5 — Radiation Intensity and Power Density

Short dipole: I₀ = 1 A, l = λ/50, R_rad = 0.316 Ω (from Problem 1). Find U_max and S at r = 1 km, θ = 90°.

**Solution:**
```
P_rad = 0.158 W
D = 1.5  (short dipole)

U_max = D × P_rad/(4π) = 1.5 × 0.158/(4π) = 0.237/12.566 = 18.9 mW/sr

Power density at r = 1000 m, θ = 90°:
  S = U_max/r² = 18.9×10⁻³/10⁶ = 18.9×10⁻⁹ W/m² = 18.9 nW/m²
```

---

### Problem 6 — Half-Power Beamwidth of Half-Wave Dipole

Find HPBW for the half-wave dipole. Its E-plane pattern is F(θ) = [cos(π/2 cosθ)/sinθ]².

**Solution:**
```
At maximum (θ = 90°): F = [cos(0)/1]² = 1

Half-power condition: [cos(π/2 cosθ)/sinθ]² = 0.5
  cos(π/2 cosθ)/sinθ = 1/√2

Solve numerically:
  At θ = 51°: cos(π/2 cos51°)/sin51° = cos(π/2 × 0.629)/0.777
             = cos(0.988)/0.777 = 0.556/0.777 = 0.716 ≈ 0.707

  → θ₃dB ≈ 51°  (half-power half-angle measured from axis)

HPBW = 2(90° - 51°) = 2 × 39° = 78°

Compare to short dipole HPBW = 90°.
(Half-wave dipole is slightly more directive.)
```

---

### Problem 7 — Far-Field of a Hertzian Dipole

I₀l = 0.1 A·m at f = 300 MHz (λ = 1 m). Find |E_θ| at r = 1 km, θ = 90°.

**Solution:**
```
Far-field formula:
  |E_θ| = (60π/r) × (I₀l/λ) × sinθ
         = (60π/1000) × (0.1/1) × sin(90°)
         = 60π × 10⁻⁴
         = 18.85×10⁻³  V/m = 18.85 mV/m

Power density:
  S = |E_θ|²/(2η₀) = (18.85×10⁻³)²/(2×377) = 3.55×10⁻⁴/754 = 0.471 μW/m²
```

---

### Problem 8 — Array Factor for Two-Element Array

Two isotropic elements separated by d = λ/2, fed with equal amplitudes and 90° progressive phase (δ = 90°). Find |AF(θ)| and the direction of maximum.

**Solution:**
```
Array factor: AF = 1 + e^(j(βd cosθ + δ))
  where βd = π (for d=λ/2)

|AF| = |1 + e^j(πcosθ + π/2)|
     = 2|cos((πcosθ + π/2)/2)|
     = 2|cos(πcosθ/2 + π/4)|

Maximum when argument = 0:
  πcosθ/2 + π/4 = 0  →  cosθ = -1/2  →  θ_max = 120°

At θ = 90°:  |AF| = 2|cos(π/4)| = 2 × 0.707 = 1.414
At θ = 0°:   |AF| = 2|cos(π/2 + π/4)| = 2|cos(3π/4)| = 2×0.707 = 1.414
At θ = 120°: |AF| = 2|cos(0)| = 2.0   (maximum)
```

---

### Problem 9 — Half-Wave Dipole Radiation

Calculate F(θ) for the half-wave dipole at θ = 90°, 60°, 30°, 0°. Express in dB.

**Solution:**
```
F(θ) = [cos(π/2 cosθ)/sinθ]²

θ = 90°:  cos(0)/1 = 1.000  →  F = 1.000 = 0 dB
θ = 60°:  cos(π/4)/0.866 = 0.707/0.866 = 0.816  →  F = 0.667 = -1.76 dB
θ = 30°:  cos(π√3/4)/0.500 = cos(1.36)/0.5 = 0.211/0.5 = 0.422 → F = 0.178 = -7.5 dB
θ = 0°:   [0/0] → L'Hopital: = 0  →  F = 0  (null along wire axis)

Summary:
  θ      F(θ)    dB
  90°    1.000    0
  60°    0.667   -1.8
  30°    0.178   -7.5
  0°     0       −∞
```

---

### Problem 10 — Antenna Gain

Antenna with D = 8 dBi, radiation efficiency η_e = 85%. Find gain G.

**Solution:**
```
D = 8 dBi  →  D_linear = 10^(8/10) = 6.31

G = η_e × D = 0.85 × 6.31 = 5.36

G (dBi) = 10 log₁₀(5.36) = 7.29 dBi

Or: G(dBi) = D(dBi) + 10 log₁₀(η_e) = 8 + 10 log₁₀(0.85) = 8 - 0.71 = 7.29 dBi
```

---

### Problem 11 — E-Plane and H-Plane Patterns

Describe E-plane and H-plane patterns for (a) Hertzian dipole (z-directed), (b) half-wave dipole.

**Solution:**
```
(a) Hertzian dipole (z-directed):
    E-plane: plane containing z-axis (e.g., xz- or yz-plane)
      Pattern: F(θ) = sin²θ  (figure-eight, zero along z-axis)
    H-plane: plane ⊥ to z (xy-plane, θ = 90°)
      Pattern: F = 1 (constant circle, omnidirectional)

(b) Half-wave dipole (z-directed):
    E-plane: F(θ) = [cos(π/2 cosθ)/sinθ]²
      Narrower than short dipole, HPBW = 78°
      Zero along z-axis
    H-plane: F = 1 (constant, omnidirectional)
      Identical to short dipole in H-plane

Both are omnidirectional in azimuth (no φ dependence).
```

---

### Problem 12 — Optimal Array Spacing

For a broadside linear array of N elements, state the optimal element spacing and explain the grating lobe condition.

**Solution:**
```
Broadside array: maximum at θ = 90°, progressive phase δ = 0.

Array factor maximum: AF = N (at θ = 90°)

Grating lobes appear when βd cosθ = ±2π (additional maxima besides main lobe):
  d cosθ = ±λ  →  grating lobe at θ where |cosθ| = λ/d

To prevent grating lobes for all θ: d < λ
  (since |cosθ| ≤ 1, need λ/d > 1)

Optimal spacing: d = λ/2
  - Avoids grating lobes (d < λ)
  - Provides sufficient aperture for good directivity
  - Half-wave spacing is the standard choice

For end-fire array: d ≤ λ/2 to avoid grating lobes,
  Hansen-Woodyard optimum: d ≈ λ/4.
```

---

### Problem 13 — Friis Transmission Formula

Link budget: P_t = 10 W, G_t = 15 dBi, G_r = 10 dBi, f = 2.4 GHz, r = 1 km. Find P_r.

**Solution:**
```
λ = c/f = 3×10⁸/2.4×10⁹ = 0.125 m

G_t = 10^(15/10) = 31.6   (linear)
G_r = 10^(10/10) = 10.0   (linear)

Friis formula:
  P_r = P_t G_t G_r (λ/(4πr))²
      = 10 × 31.6 × 10 × (0.125/(4π×10³))²
      = 3160 × (0.125/12566)²
      = 3160 × (9.947×10⁻⁶)²
      = 3160 × 9.894×10⁻¹¹
      = 3.13×10⁻⁷ W = 313 nW

In dB:
  P_r(dBW) = 10 + 15 + 10 + 20 log(0.125/12566)
           = 35 + 20 log(9.947×10⁻⁶)
           = 35 + 20×(−5.002)
           = 35 − 100.04
           = −65.0 dBW = −35.0 dBm
```

---

### Problem 14 — Radar Equation

Monostatic radar: P_t = 1 kW, G_t = G_r = 30 dBi, f = 10 GHz, target at r = 1 km with σ = πa² (conducting sphere, a = 0.1 m). Find P_r.

**Solution:**
```
f = 10 GHz → λ = 0.03 m
a = 0.1 m >> λ → optical regime → σ_RCS = πa² = π×0.01 = 0.0314 m²

G_t = G_r = 10^(30/10) = 1000

Radar equation:
  P_r = P_t G_t G_r λ² σ/(4π)³ r⁴

  (4π)³ = 1984.4
  r⁴ = (10³)⁴ = 10¹²

  P_r = 10³ × 10³ × 10³ × (0.03)² × 0.0314 / (1984 × 10¹²)
      = 10⁹ × 9×10⁻⁴ × 0.0314 / (1984 × 10¹²)
      = 10⁹ × 2.826×10⁻⁵ / (1.984×10¹⁵)
      = 2.826×10⁴ / (1.984×10¹⁵)
      = 1.42×10⁻¹¹ W = 14.2 pW
```

---

### Problem 15 — Effective Radiated Power (ERP / EIRP)

Transmitter: P_t = 100 W, feeder loss = 1 dB, antenna gain G = 20 dBi. Find EIRP.

**Solution:**
```
Convert to dB:
  P_t = 10 log(100) = 20 dBW
  Feeder loss = -1 dB
  G = 20 dBi

EIRP = P_t - L_feeder + G
     = 20 - 1 + 20
     = 39 dBW

EIRP (linear) = 10^(39/10) = 7943 W ≈ 7.94 kW

Power delivered to antenna: P_ant = 100/10^(1/10) = 100/1.259 = 79.4 W
ERP (vs. half-wave dipole, D_dipole = 2.15 dBi):
  ERP = EIRP - 2.15 dBi = 36.85 dBW = 4847 W ≈ 4.85 kW
```
