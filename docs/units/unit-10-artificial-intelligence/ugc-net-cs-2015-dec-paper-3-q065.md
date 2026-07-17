# Question 65

*UGC NET CS · 2015 Dec Paper 3 · Fuzzy Sets · Standard Additive Model and Centroid Defuzzification*

A standard additive fuzzy model has rules: IF x is Aᵢ AND y is Bᵢ THEN z is Cᵢ. For crisp inputs x=x₀ and y=y₀, which expression gives the crisp model output?

- **1.** z = Σᵢ μ_Aᵢ(x₀) μ_Bᵢ(y₀) μ_Cᵢ(z)
- **2.** z = Σᵢ μ_Aᵢ(x₀) μ_Bᵢ(y₀)
- **3.** z = centroid(Σᵢ μ_Aᵢ(x₀) μ_Bᵢ(y₀) μ_Cᵢ(z))
- **4.** z = centroid(Σᵢ μ_Aᵢ(x₀) μ_Bᵢ(y₀))

> [!TIP]
> **Correct answer: 3. z = centroid(Σᵢ μ_Aᵢ(x₀) μ_Bᵢ(y₀) μ_Cᵢ(z))**

## Solution

Rule i fires with strength αᵢ=μ_Aᵢ(x₀)μ_Bᵢ(y₀) when product is used for AND. The standard additive model combines the scaled consequent sets into μ_out(z)=Σᵢ αᵢμ_Cᵢ(z). This is still a fuzzy set over z, so a crisp output requires defuzzification; applying the centroid to that aggregated set gives option 3.

## Key Points

- Fuzzy inference: compute rule strengths, aggregate the weighted consequents, then centroid-defuzzify the resulting output set.

## Why the other options are incorrect

Option 1 is the aggregated membership expression but labels it directly as a crisp z without defuzzification. Option 2 sums only firing strengths and contains no consequent sets. Option 4 takes a centroid of scalar firing strengths rather than of an output membership function over z.
