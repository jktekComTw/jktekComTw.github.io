# Chapter 8 — Plane Electromagnetic Waves
## Problems and Solutions

---

### Problem 1 — Wave Impedance

Find the intrinsic impedance in (a) free space, (b) a non-magnetic dielectric with εᵣ = 9.

**Solution:**
```
η₀ = √(μ₀/ε₀) = √(4π×10⁻⁷ / 8.85×10⁻¹²) = 377 Ω

For εᵣ = 9, μᵣ = 1:
η = η₀ √(μᵣ/εᵣ) = 377/√9 = 377/3 = 125.7 Ω
```

---

### Problem 2 — Attenuation in a Lossy Dielectric

Medium: εᵣ = 2.5, σ = 0.01 S/m, μᵣ = 1, f = 1 GHz. Find α, β, and skin depth δ.

**Solution:**
```
ω = 2π×10⁹  rad/s
Loss tangent: σ/(ωε) = σ/(ω ε₀ εᵣ)
  = 0.01 / (2π×10⁹ × 8.85×10⁻¹² × 2.5)
  = 0.01 / 0.1390 = 0.0719  << 1  (low-loss dielectric)

Low-loss approximations:
  η ≈ η₀/√εᵣ = 377/1.581 = 238.4 Ω
  α ≈ (σ/2) η = (0.01/2) × 238.4 = 1.19 Np/m
  β ≈ ω√(μ₀ε₀εᵣ) = (2π×10⁹/c)×√2.5 = 20.94×1.581 = 33.1 rad/m

δ = 1/α = 1/1.19 = 0.84 m
```

---

### Problem 3 — Polarization State

Determine the polarization of E = 3 cos(ωt − kz) a_x + 4 sin(ωt − kz) a_y.

**Solution:**
```
Phasor: Ẽ = (3 a_x - j4 a_y) e^(-jkz)
  |E_x| = 3,  |E_y| = 4,  phase difference = -90°

Semi-axes are unequal (3 ≠ 4) → elliptical polarization.

Tracing at z = 0:
  t = 0:    E = 3 a_x
  t = T/4:  E = 4 a_y   (rotates counterclockwise viewed from +z)

→ Left-Hand Elliptical Polarization (LHEP), semi-axes 3 and 4.
```

---

### Problem 4 — Group Velocity in a Plasma

Plasma with ωₚ = 2π×10⁹ rad/s (fₚ = 1 GHz). Find phase and group velocities at f = 3 GHz.

**Solution:**
```
Dispersion relation: ω² = ωₚ² + k²c²

ω  = 2π×3×10⁹  rad/s
ωₚ = 2π×1×10⁹  rad/s

k² = (ω² - ωₚ²)/c² = (9 - 1)(4π²×10¹⁸)/(9×10¹⁶)
   = 8 × 4π² × 100/9 = 3510 rad²/m²
k  = 59.2 rad/m

Phase velocity:
  v_p = ω/k = 2π×3×10⁹ / 59.2 = 3.18×10⁸ m/s  (> c, allowed)

Group velocity:
  v_g = dω/dk = c²k/ω = (9×10¹⁶ × 59.2)/(6π×10⁹) = 2.83×10⁸ m/s

Check: v_p × v_g = 3.18×10⁸ × 2.83×10⁸ = 9.0×10¹⁶ = c²  ✓
```

---

### Problem 5 — Poynting Vector in a Dielectric

E = 50 cos(ωt − kz) a_x V/m propagates in a lossless medium with εᵣ = 4, μᵣ = 1.
Find ⟨S⟩.

**Solution:**
```
η = η₀/√εᵣ = 377/2 = 188.5 Ω

H = (E₀/η) cos(ωt - kz) a_y = (50/188.5) cos(ωt - kz) a_y = 0.265 cos(ωt-kz) a_y  A/m

⟨S⟩ = E₀²/(2η) a_z = 2500/(2×188.5) a_z = 6.63 a_z  W/m²
```

---

### Problem 6 — Reflection Coefficient (Normal Incidence)

Plane wave from air (η₁ = 377 Ω) normally incident on glass (εᵣ = 4, μᵣ = 1, η₂ = 188.5 Ω).
Find Γ, τ, R, T.

**Solution:**
```
Γ = (η₂ - η₁)/(η₂ + η₁) = (188.5 - 377)/(188.5 + 377)
  = -188.5/565.5 = -0.333  (phase reversal on reflection)

τ = 2η₂/(η₂ + η₁) = 2×188.5/565.5 = 0.667

Check: 1 + Γ = τ  →  1 - 0.333 = 0.667  ✓

Power reflectance: R = |Γ|² = 0.111 = 11.1%
Power transmittance: T = 1 - R = 0.889 = 88.9%
```

---

### Problem 7 — Standing Wave Ratio

From Problem 6 (Γ = −0.333), find the SWR in medium 1.

**Solution:**
```
SWR = (1 + |Γ|)/(1 - |Γ|) = (1 + 0.333)/(1 - 0.333) = 1.333/0.667 = 2.0

|E_max| = E₊(1 + |Γ|) = 1.333 E₊
|E_min| = E₊(1 - |Γ|) = 0.667 E₊
```

---

### Problem 8 — Brewster's Angle

Find Brewster's angle for TM (parallel) polarization at an air–glass interface (n₁ = 1, n₂ = 2).
State whether it exists for TE polarization.

**Solution:**
```
TM (parallel) polarization:
  tan(θ_B) = n₂/n₁ = 2
  θ_B = arctan(2) = 63.43°

TE (perpendicular) polarization:
  Brewster's angle does NOT exist for TE in non-magnetic media.
  (The TE reflection coefficient never reaches zero for non-magnetic materials.)
```

---

### Problem 9 — Critical Angle for TIR

Glass (n₁ = 1.5) to air (n₂ = 1) interface. Find the critical angle for total internal reflection.

**Solution:**
```
sin(θ_c) = n₂/n₁ = 1/1.5 = 0.667

θ_c = arcsin(0.667) = 41.8°

For θᵢ > 41.8°, total internal reflection occurs (all power reflected).
```

---

### Problem 10 — Transmission Coefficients at Dielectric Interface

Normal incidence from air into medium with εᵣ = 9 (η₂ = 125.7 Ω). Find Γ, τ, R, T.

**Solution:**
```
Γ = (η₂ - η₁)/(η₂ + η₁) = (125.7 - 377)/(125.7 + 377) = -251.3/502.7 = -0.500

τ = 2η₂/(η₂ + η₁) = 251.4/502.7 = 0.500

R = |Γ|² = 0.25 = 25%

T = (η₁/η₂)|τ|² = (377/125.7) × 0.25 = 3 × 0.25 = 0.75 = 75%

Check: R + T = 0.25 + 0.75 = 1  ✓
```

---

### Problem 11 — Oblique Incidence (TE), Fresnel Coefficients

TE wave from air (n₁ = 1) into glass (n₂ = 2) at θᵢ = 30°. Find θₜ, Γ_TE, τ_TE.

**Solution:**
```
Snell's law:  n₁ sinθᵢ = n₂ sinθₜ
  sinθₜ = (1/2) sin30° = 0.25  →  θₜ = 14.5°

cosθᵢ = cos30° = 0.866
cosθₜ = cos14.5° = 0.968

TE Fresnel coefficients (η₁ = 377, η₂ = 188.5 Ω):
  Γ_TE = (η₂ cosθᵢ - η₁ cosθₜ)/(η₂ cosθᵢ + η₁ cosθₜ)
       = (188.5×0.866 - 377×0.968)/(188.5×0.866 + 377×0.968)
       = (163.2 - 364.9)/(163.2 + 364.9)
       = -201.7/528.1 = -0.382

  τ_TE = 2η₂ cosθᵢ/(η₂ cosθᵢ + η₁ cosθₜ)
       = 2×163.2/528.1 = 0.618
```

---

### Problem 12 — Phase and Group Velocities in a Waveguide

Rectangular waveguide with cutoff frequency f_c = 5 GHz, operating at f = 10 GHz. Find v_p, v_g, λ_g.

**Solution:**
```
√(1-(f_c/f)²) = √(1-0.25) = √0.75 = 0.866

Phase velocity:
  v_p = c/√(1-(f_c/f)²) = 3×10⁸/0.866 = 3.46×10⁸  m/s  (> c, ok)

Group velocity:
  v_g = c √(1-(f_c/f)²) = 3×10⁸ × 0.866 = 2.60×10⁸  m/s

Check: v_p × v_g = 3.46×10⁸ × 2.60×10⁸ = 9.0×10¹⁶ = c²  ✓

Guide wavelength:
  λ₀ = c/f = 3×10⁸/10¹⁰ = 0.03 m = 3 cm
  λ_g = λ₀/0.866 = 3/0.866 = 3.46 cm
```

---

### Problem 13 — Power Reflection and Transmission (Oblique TE)

From Problem 11 (Γ_TE = −0.382, θᵢ = 30°, θₜ = 14.5°). Find R and T.

**Solution:**
```
R = |Γ_TE|² = (0.382)² = 0.146 = 14.6%

T = 1 - R = 0.854 = 85.4%

Verify with τ_TE:
  T = (n₂ cosθₜ)/(n₁ cosθᵢ) × |τ_TE|²
    = (2×0.968)/(1×0.866) × (0.618)²
    = 2.236 × 0.382 ≈ 0.854  ✓
```

---

### Problem 14 — TM Polarization at Oblique Incidence

TM (parallel) wave, same geometry as Problem 11 (θᵢ = 30°, air to glass n₂ = 2). Find Γ_TM.

**Solution:**
```
Fresnel TM coefficient (using refractive indices):
  Γ_TM = (n₂ cosθᵢ - n₁ cosθₜ)/(n₂ cosθᵢ + n₁ cosθₜ)
        = (2×0.866 - 1×0.968)/(2×0.866 + 1×0.968)
        = (1.732 - 0.968)/(1.732 + 0.968)
        = 0.764/2.700 = +0.283

Positive Γ_TM means no phase reversal.
At Brewster's angle θ_B = 63.4°, Γ_TM = 0 exactly.
Since 30° < 63.4°, the TM wave has partial reflection with no phase reversal.
```

---

### Problem 15 — Propagation Constant in a Good Conductor

Find α, β, and skin depth in copper (σ = 5.8×10⁷ S/m, μᵣ = 1) at f = 100 MHz.

**Solution:**
```
Good conductor condition: σ/(ωε₀) = 5.8×10⁷/(2π×10⁸×8.85×10⁻¹²) = 1.05×10¹⁰ >> 1  ✓

α = β = √(πfμ₀σ)
  = √(π × 10⁸ × 4π×10⁻⁷ × 5.8×10⁷)
  = √(4π² × 5.8 × 10⁸)
  = √(2.291×10¹⁰)
  = 1.514×10⁵  Np/m (and rad/m)

γ = (1 + j) × 1.514×10⁵  /m

δ = 1/α = 6.61 μm

(Consistent with: δ = 66.1/√f mm = 66.1/√(10⁸) mm = 66.1/10⁴ mm = 6.61 μm ✓)
```
