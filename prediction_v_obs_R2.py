#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:58:17 2026

@author: nxc045
"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import r2_score

data = pd.read_csv('/Users/nxc045/Documents/Dabigatram Project/DBMonolix/DabigatranMonolixFinal3/predictions.txt')

print(data.loc[data['indivPred_SAEM'].isna(), ['id', 'Observation', 'indivPred_SAEM']])

#outlier = 5000
#print("Outlier Cutoff", outlier)
#print("Number of outliers:", len(data[data['indivPred_SAEM'] > outlier]))
#print("ID of Outliers:", list(data.loc[data['indivPred_SAEM'] > outlier, 'id'].unique()))
#print("Percentage of Outliers:", len(data[data['indivPred_SAEM'] > outlier])/len(data))
#data = data[data['indivPred_SAEM'] <= outlier] #remove extreme outlier predictions
# 1. Set publication style defaults
plt.rcParams.update(
    {
        "font.family": "serif",  # Academic style font
        "font.size": 10,  # Standard journal text size
        "axes.labelsize": 11,  # Legible axis labels
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "figure.dpi": 300,  # High resolution for review
        "savefig.dpi": 300,  # High resolution for final print
    }
)

# 2. Calculate the R^2 value
# Note: r2_score takes (y_true, y_pred) -> (Observation, Prediction)
r2_value = r2_score(data["Observation"], data["indivPred_SAEM"])
print("R^2 value for this cutoff:", r2_value)

# 3. Initialize the plot (Standard 3.5" x 3.5" single-column journal format)
fig, ax = plt.subplots(figsize=(3.5, 3.5))

# 4. Create the scatter plot
sns.scatterplot(
    data=data,
    x="indivPred_SAEM",
    y="Observation",
    color="#1f77b4",  # Clean, professional slate blue
    alpha=0.75,  # Prevents overlapping points from blinding data density
    edgecolor="none",  # Cleaner look without point borders
    s=25,  # Controlled marker size
    ax=ax,
    zorder=3,
)

# 5. Add the identity line (y = x)
# We find the min and max across both axes to draw a perfect diagonal
min_val = min(data["indivPred_SAEM"].min(), data["Observation"].min())
max_val = max(data["indivPred_SAEM"].max(), data["Observation"].max())

ax.plot(
    [min_val, max_val],
    [min_val, max_val],
    color="#d62728",  # Contrasting professional red line
    linestyle="--",  # Dashed line style
    linewidth=1.2,
    zorder=2,
    label="y = x",
)

# 6. Display the R^2 value on the plot
# Using transform=ax.transAxes places the text relative to the box (0,0 is bottom-left, 1,1 is top-right)
ax.text(
    0.05,
    0.90,
    f"$R^2 = {r2_value:.3f}$",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none", alpha=0.8),
)

# 7. Clean up layout and borders
ax.spines["top"].set_visible(False)  # Remove top border clutter
ax.spines["right"].set_visible(False)  # Remove right border clutter
ax.grid(True, linestyle=":", alpha=0.5, zorder=1)  # Subtle layout grid

# Set specific axis labels as requested
ax.set_xlabel("Individual Predictions")
ax.set_ylabel("Observation")
ax.set_title("Predictions vs Observations")

plt.tight_layout()

# 8. Save your figure as a vector PDF for infinite scalability in publications
#plt.savefig(f"saem_model_fit_{outlier}.pdf", bbox_inches='tight')
plt.show()
