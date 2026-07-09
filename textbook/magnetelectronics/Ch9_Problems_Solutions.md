# Chapter 9 — Theory and Applications of Transmission Lines
## Problems and Solutions

---

### Problem 1 — Characteristic Impedance

Find Z₀ for a coaxial line with inner radius a = 1 mm, outer radius b = 5 mm, εᵣ = 2.25.

**Solution:**
```
Z₀ = (60/√εᵣ) ln(b/a)
   = (60/1.5) ln(5)
   = 40 × 1.609
   = 64.4 Ω
```

---

### Problem 2 — Propagation Constant

Line parameters at f = 1 MHz: R = 0.1 Ω/m, L = 0.5 μH/m, G = 0, C = 50 pF/m. Find α and β.

**Solution:**
```
ω = 2π×10⁶  rad/s

Lossless β:
  β₀ = ω√(LC) = 2π×10⁶ × √(0.5×10⁻⁶ × 50×10⁻¹²)
      = 2π×10⁶ × √(25×10⁻¹⁸)
      = 2π×10⁶ × 5×10⁻⁹
      = 0.0314  rad/m

Attenuation (low-loss approximation):
  Z₀ = √(L/C) = √(0.5×10⁻⁶/50×10⁻¹²) = √(10⁴) = 100 Ω
  α ≈ R/(2Z₀) = 0.1/(2×100) = 5×10⁻⁴  Np/m

γ = α + jβ = 5×10⁻⁴ + j0.0314  /m
```

---

### Problem 3 — VSWR from Reflection Coefficient

Z₀ = 50 Ω, Z_L = 100 + j50 Ω. Find Γ and SWR.

**Solution:**
```
Γ = (Z_L - Z₀)/(Z_L + Z₀) = (50 + j50)/(150 + j50)

|numerator| = √(50² + 50²) = 50√2 = 70.71
|denominator| = √(150² + 50²) = √25000 = 158.1

|Γ| = 70.71/158.1 = 0.447

SWR = (1 + |Γ|)/(1 - |Γ|) = 1.447/0.553 = 2.62
```

---

### Problem 4 — Input Impedance of Terminated Line

Z₀ = 75 Ω, Z_L = 150 Ω (real), l = λ/8. Find Z_in.

**Solution:**
```
βl = (2π/λ)(λ/8) = π/4  →  tan(βl) = 1

Z_in = Z₀ × (Z_L + jZ₀ tanβl)/(Z₀ + jZ_L tanβl)
     = 75 × (150 + j75)/(75 + j150)

Factor 75 from each:
  = 75 × (2 + j)/(1 + j2)

Multiply by conjugate (1 - j2)/(1 - j2):
  (2+j)(1-j2) = 2 - j4 + j - j²2 = 2 - j4 + j + 2 = 4 - j3
  (1+j2)(1-j2) = 1 + 4 = 5

Z_in = 75 × (4-j3)/5 = 15(4-j3) = 60 - j45 Ω
```

---

### Problem 5 — Reflection Coefficient for Complex Load

Z₀ = 50 Ω, Z_L = 25 − j50 Ω. Find Γ and SWR.

**Solution:**
```
Γ = (Z_L - Z₀)/(Z_L + Z₀) = (-25 - j50)/(75 - j50)

Multiply by conjugate (75 + j50):
  Numerator: (-25-j50)(75+j50) = -1875 - j1250 - j3750 - j²2500
           = -1875 + 2500 - j5000 = 625 - j5000
  Denominator: 75² + 50² = 5625 + 2500 = 8125

Γ = (625 - j5000)/8125 = 0.0769 - j0.6154

|Γ| = √(0.0769² + 0.6154²) = √(0.00592 + 0.3787) = √0.3846 = 0.620

SWR = (1 + 0.620)/(1 - 0.620) = 1.620/0.380 = 4.26
```

---

### Problem 6 — Quarter-Wave Transformer

Match Z_L = 200 Ω to Z₀ = 50 Ω using a λ/4 transformer section. Find Z₀' and verify Z_in.

**Solution:**
```
Quarter-wave transformer impedance:
  Z₀' = √(Z₀ × Z_L) = √(50 × 200) = √10000 = 100 Ω

Input impedance of λ/4 section:
  Z_in = (Z₀')²/Z_L = 10000/200 = 50 Ω  = Z₀  ✓

The λ/4 section (Z₀' = 100 Ω) provides a perfect match at the design frequency.
```

---

### Problem 7 — Reflection Coefficient

Z₀ = 50 Ω, Z_L = 75 + j25 Ω. Find |Γ| and ∠Γ.

**Solution:**
```
Γ = (Z_L - Z₀)/(Z_L + Z₀) = (25 + j25)/(125 + j25)

|numerator| = 25√2 = 35.36
|denominator| = √(125² + 25²) = √16250 = 127.5

|Γ| = 35.36/127.5 = 0.277

∠Γ = arctan(25/25) - arctan(25/125) = 45° - 11.3° = 33.7°

Γ = 0.277 ∠33.7°
```

---

### Problem 8 — Line Loss in dB

Transmission line: α = 0.01 Np/m, length l = 100 m. Find power loss in dB.

**Solution:**
```
Total attenuation = αl = 0.01 × 100 = 1 Np

Convert: 1 Np = 8.686 dB
  Loss = 1 × 8.686 = 8.69 dB

Power ratio: P_out/P_in = e^(-2αl) = e^(-2) = 0.1353 = -8.69 dB  ✓

Voltage ratio: V_out/V_in = e^(-αl) = e^(-1) = 0.368
```

---

### Problem 9 — Single-Stub Matching

Z₀ = 50 Ω, Z_L = 100 Ω (real). Find short-circuit stub position d and length l for matching.

**Solution:**
```
Normalized: y_L = Z₀/Z_L = 0.5

Find d where Re[y(d)] = 1:
  Let t = tan(βd). Require real part = 1:
  y_L(1 + t²)/(1 + y_L² t²) = 1
  → t² = 1/y_L = 2  →  t = ±√2

Solution 1 (t = +√2):
  βd₁ = arctan(√2) = 54.7°  →  d₁ = 0.152λ
  Im[y(d₁)] = +√2 × 0.75/1.5 = +0.707
  → y(d₁) = 1 + j0.707,  need jb_s = -j0.707
  SC stub: -cot(βl₁) = -0.707  →  tan(βl₁) = √2  →  l₁ = 0.152λ

Solution 2 (t = -√2):
  βd₂ = 180° - 54.7° = 125.3°  →  d₂ = 0.348λ
  Im[y(d₂)] = -0.707  →  need jb_s = +j0.707
  SC stub: -cot(βl₂) = +0.707  →  βl₂ = 125.3°  →  l₂ = 0.348λ
```

---

### Problem 10 — Transient Response (Step Input)

Z₀ = 50 Ω, Z_g = 50 Ω, Z_L = ∞ (open), V_g = 100 V step. Find V at load for 0 < t < 3T.

**Solution:**
```
Γ_g = (Z_g - Z₀)/(Z_g + Z₀) = (50-50)/(50+50) = 0   (matched source)
Γ_L = (Z_L - Z₀)/(Z_L + Z₀) = 1                     (open circuit)

Initial forward wave:
  V₊ = V_g × Z₀/(Z_g + Z₀) = 100 × 50/100 = 50 V

Timeline:
  0 < t < T:  V_L = 0
  t = T:      V₊ arrives at open end
              V_L = V₊(1 + Γ_L) = 50(1+1) = 100 V
              V₋ = Γ_L V₊ = 50 V returns toward source
  t = 2T:     V₋ arrives at source: Γ_g = 0 → no re-reflection
  t > T:      V_L = 100 V (steady state, no further changes)
```

---

### Problem 11 — Bounce Diagram

Z₀ = 50 Ω, Z_g = 200 Ω, Z_L = ∞ (open), V_g = 100 V step, T = 0.5 μs. Trace voltage at load.

**Solution:**
```
Γ_g = (200-50)/(200+50) = 150/250 = 0.6
Γ_L = 1

V₊₁ = 100 × 50/(200+50) = 20 V

    Time       Event                    V at load
  ─────────────────────────────────────────────────
  t = 0        Step applied             0 V
  t = T        V₊₁=20 arrives          20(1+1) = 40 V
               V₋₁ = 20 returns
  t = 2T       V₋₁ at source → V₊₂ = 0.6×20 = 12 V
  t = 3T       V₊₂=12 arrives          64 V (+24)
               V₋₂ = 12 returns
  t = 4T       V₋₂ at source → V₊₃ = 0.6×12 = 7.2 V
  t = 5T       V₊₃ arrives             78.4 V (+14.4)

Steady state: V_L → 40/(1-0.6) = 100 V  ✓
(all voltage drops across open-circuit load, as expected)
```

---

### Problem 12 — Double-Stub Matching

Z₀ = 50 Ω, Z_L = 25 − j50 Ω, stub separation = λ/4. Find stub lengths (SC stubs).

**Solution:**
```
Normalized load admittance:
  y_L = Z₀/Z_L = 50/(25-j50)
      = 50(25+j50)/3125 = 0.4 + j0.8

For λ/4 stub spacing, stub 1 must set y₁ = 0.4 + jB such that
after λ/4 transform (y → 1/y), Re[y₂] = 1:

  Re[1/(0.4+jB)] = 1  →  0.4/(0.16 + B²) = 1
  B² = 0.24  →  B = ±0.490

Since Im[y_L] = 0.8, stub 1 susceptance b₁ = B - 0.8:
  Case 1: B = +0.490  →  b₁ = 0.490 - 0.8 = -0.310
  Case 2: B = -0.490  →  b₁ = -0.490 - 0.8 = -1.290

Stub 1 (SC, Case 1):  -cot(βl₁) = -0.310  →  l₁ = 0.202λ
Stub 1 (SC, Case 2):  -cot(βl₁) = -1.290  →  l₁ = 0.397λ

For Case 1 — Stub 2 susceptance:
  y₂ = 1/(0.4+j0.490) = 1 - j1.22
  Need b₂ = +1.22
  SC stub: -cot(βl₂) = 1.22  →  l₂ = 0.391λ
```

---

### Problem 13 — Impedance Transformation

Z₀ = 100 Ω, Z_L = 50 Ω, l = 3λ/8. Find Z_in.

**Solution:**
```
βl = (2π/λ)(3λ/8) = 3π/4  →  tan(3π/4) = -1

Z_in = 100 × (50 + j100×(-1))/(100 + j50×(-1))
     = 100 × (50 - j100)/(100 - j50)

Factor 50: = 100 × (1 - j2)/(2 - j)

Multiply by (2+j)/(2+j):
  (1-j2)(2+j) = 2 + j - j4 - j²2 = 2 + j - j4 + 2 = 4 - j3
  (2-j)(2+j) = 5

Z_in = 100 × (4-j3)/5 = 20(4-j3) = 80 - j60 Ω
```

---

### Problem 14 — Power Delivered to Load

Z₀ = 50 Ω, Z_s = 50 Ω, Z_L = 75 Ω, V_s = 100∠0° V (peak), lossless λ/4 line.

**Solution:**
```
Quarter-wave transforms Z_L to:
  Z_in = Z₀²/Z_L = 2500/75 = 33.33 Ω

Input current:
  I_in = V_s/(Z_s + Z_in) = 100/(50 + 33.33) = 100/83.33 = 1.2 A (peak)

Since line is lossless, P_in = P_L:
  P_L = (1/2)|I_in|² Re[Z_in] = 0.5 × 1.44 × 33.33 = 24 W
```

---

### Problem 15 — Return Loss

From Problem 7 (|Γ| = 0.277). Find return loss and mismatch loss.

**Solution:**
```
Return Loss (RL) = -20 log₁₀|Γ|
  = -20 log₁₀(0.277) = -20×(-0.558) = 11.2 dB

Power reflected: |Γ|² = 0.0767 = 7.67%
Power transmitted: 1 - |Γ|² = 92.3%

Mismatch Loss = -10 log₁₀(1 - |Γ|²)
  = -10 log₁₀(0.923) = 0.35 dB
```
