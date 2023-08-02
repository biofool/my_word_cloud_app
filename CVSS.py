import numpy as np
import matplotlib.pyplot as plt

# CVSS Metrics
labels_full = ["Attack Vector", "Attack Complexity", "Privileges Required", "User Interaction",
               "Scope", "Confidentiality", "Integrity", "Availability"]

# Sample CVSS values for demonstration purposes (values typically range between 0 and 1)
values = [0.9, 0.6, 0.3, 0.7, 0.5, 0.8, 0.9, 0.7]

# Convert to an angle for the polar plot (octagonal shape)
num_vars = len(labels_full)
angles_octagon = np.linspace(0, 2 * np.pi, num_vars + 1)

# Define the radii for each of the zones
green_radius = 0.6
yellow_radius = 0.9
red_radius = 1.0

# For the dodecahedron zones
num_vars_dodeca = 12
angles_dodeca = np.linspace(0, 2 * np.pi, num_vars_dodeca + 1)
red_radii = [red_radius] * (num_vars_dodeca + 1)
yellow_radii = [yellow_radius] * (num_vars_dodeca + 1)
green_radii = [green_radius] * (num_vars_dodeca + 1)

# Generate the Spider/Radar chart
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
