#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:53:02 2026

@author: nxc045
"""

import matplotlib.pyplot as plt
import pandas as pd

# 1. Set professional publication-ready style defaults
plt.rcParams.update(
    {
        "font.family": "serif",  # Academic style font (e.g., Times New Roman feel)
        "font.size": 10,  # Standard journal body text size
        "axes.labelsize": 11,  # Legible axis labels
        "axes.titlesize": 11,  # Title size matches layout weight
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "figure.dpi": 300,  # High resolution for review
        "savefig.dpi": 300,  # Print-ready high-resolution saving
    }
)

# Load and clean your data as before
fold_change_data = pd.read_excel(
    "/Users/nxc045/Documents/Dabigatram Project/Data/DabigatranData.xlsx"
)
fold_change_data = fold_change_data.iloc[58:65, 0:5]
fold_change_data.columns = [
    "Days",
    "Combo",
    "DB*PD1",
    "Combo Standard Error",
    "DB*PD1 Standard Error",
]
fold_change_data[["Combo", "DB*PD1"]] = fold_change_data[
    ["Combo", "DB*PD1"]
].astype(float)
fold_change_data = fold_change_data.round(2)
print(fold_change_data)

# 2. Initialize the plot with single-column journal proportions (4.5 x 3.5 inches)
fig, ax = plt.subplots(figsize=(4.5, 3.5))

# 3. Plot DB*PD1 with Y-Error Bars
ax.errorbar(
    x=fold_change_data["Days"],
    y=fold_change_data["DB*PD1"],
    yerr=fold_change_data["DB*PD1 Standard Error"],
    fmt="o--",  # Circle markers with dashed lines
    color="#1f77b4",  # Professional dark slate/black
    markerfacecolor="#2c3e50",
    markeredgecolor="none",
    markersize=5,
    elinewidth=1.2,  # Line width of the error bars
    capsize=3,  # Width of the caps at the end of error bars
    capthick=1.2,  # Thickness of the error bar caps
    label="DB*PD1/Isotype Fold Change",
    zorder=3,
)

# 4. Plot Combo with Y-Error Bars
ax.errorbar(
    x=fold_change_data["Days"],
    y=fold_change_data["Combo"],
    yerr=fold_change_data["Combo Standard Error"],
    fmt="o--",  # Circle markers with dashed lines
    color="#d62728",  # Clean, professional crimson red
    markerfacecolor="#d62728",
    markeredgecolor="none",
    markersize=5,
    elinewidth=1.2,
    capsize=3,
    capthick=1.2,
    label="Combo Fold Change",
    zorder=4,
)

# 5. Clean up borders and formatting
ax.spines["top"].set_visible(False)  # Remove top border clutter
ax.spines["right"].set_visible(False)  # Remove right border clutter
ax.grid(True, linestyle=":", alpha=0.5, zorder=1)  # Subtle layout grid background

# 6. Apply precise text and legends
ax.set_title("Cancer Cell Count Change Between Measurements", pad=12)
ax.set_xlabel("Time Interval (Day t1 to Day t2)", labelpad=6)
ax.set_ylabel("Fold Change over Interval", labelpad=6)

# Places legend neatly without frame borders cluttering data space
ax.legend(frameon=False, loc="upper left", fontsize=9)

# Adjust margins tightly to eliminate dead white space around boundaries
plt.tight_layout()

# 7. Save your figure as an infinitely scalable vector PDF for your manuscript
plt.savefig('/Users/nxc045/Documents/Dabigatram Project/Data/cancer_cell_fold_change.pdf', bbox_inches='tight')
plt.show()