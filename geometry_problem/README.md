# Pyramid and Cone Geometry Solver

A Python script designed to solve a geometry problem that calculates the lateral surface area of a regular triangular pyramid based on the parameters of a related cone.

## Problem Statement

The slant height of a cone and the lateral edge of a regular triangular pyramid are both 25 cm. The apothem of the pyramid is equal to the radius of the base of the cone. Calculate the lateral surface area of the pyramid (in $\text{cm}^2$), given that the lateral surface area of the cone is $500\pi \text{ cm}^2$.

## Features

The script provides two methods of execution:
*   **Static Solution:** An immediate calculation using the fixed values provided in the problem statement.
*   **Interactive Calculator:** A dynamic CLI tool allowing custom inputs with real-time geometric validation.

## Installation & Usage

Ensure you have Python 3.x installed. No external dependencies or libraries are required.

```bash
python main.py
```

### Interactive CLI Inputs

When running the interactive mode, the script prompts for:
1.  **L** — Slant height of the cone.
2.  **b** — Lateral edge of the pyramid.
3.  The coefficient of the cone's lateral area before $\pi$ (e.g., enter `500` for $500\pi$).

## Formulas & Mathematical Logic

*   **Cone Radius (Pyramid Apothem):** $R = S_{\text{cone lateral}} / (\pi \cdot L)$
*   **Pyramid Base Side:** $a = 2 \cdot \sqrt{b^2 - R^2}$
*   **Pyramid Lateral Area:** $S_{\text{pyramid lateral}} = \frac{3 \cdot a \cdot R}{2}$
