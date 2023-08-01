import matplotlib.pyplot as plt
import numpy as np

# Sample CVSS v3 metric values
labels = ["AV", "AC", "UI", "S", "C", "I", "A"]
values = [0.85, 0.44, 0.70, 0.50, 0.66, 0.2, 0.56]  # Mock values for demonstration
max_value = max(values)

# Calculate the positions of each point on the plot
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Adding background colors to the radar plot based on the given instructions
# Define the background color ranges
# CVSS v3 metric names and their abbreviations
labels_full = ["Attack Vector", "Attack Complexity**-1", "User Interaction**-1", "Scope",
               "Confidentiality", "Integrity", "Availability"]
labels_abbrev = ["AV", "AC", "UI", "S", "C", "I", "A"]



green_zone_fraction = 6/10
yellow_zone_fraction = 3/10
red_zone_fraction = 1/10

# Calculate the values for each zone
green_radius = max_value * green_zone_fraction
yellow_radius = green_radius + max_value * yellow_zone_fraction
red_radius = yellow_radius + max_value * red_zone_fraction
# Adjust the spider chart to have dodecahedron (12-sided) background zones

# Increase the number of divisions for the dodecahedron shape
num_vars_dodeca = 12
angles_dodeca = np.linspace(0, 2 * np.pi, num_vars_dodeca + 1)

# Define the radii for the dodecahedron background zones
red_radii = [red_radius] * (num_vars_dodeca + 1)
yellow_radii = [yellow_radius] * (num_vars_dodeca + 1)
green_radii = [green_radius] * (num_vars_dodeca + 1)

# Correct the mismatch by excluding the last angle for the CVSS octagon shape

# Plotting
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill the dodecahedron backgrounds
ax.fill(angles_dodeca, red_radii, color='red', alpha=0.2, linestyle='dashed', linewidth=2)
ax.fill(angles_dodeca, yellow_radii, color='yellow', alpha=0.15, linestyle='dashed', linewidth=1)
ax.fill(angles_dodeca, green_radii, color='green', alpha=0.3)

# Plot the CVSS values (octagonal shape)
ax.fill(angles_octagon[:-1], values, color='blue', alpha=0.25)
ax.set_yticklabels([])
ax.set_xticks(angles_octagon[:-1])
ax.set_xticklabels(labels_full)

plt.title("Adjusted CVSS v3 Spider Chart with Dodecahedron Background Zones")
plt.show()
