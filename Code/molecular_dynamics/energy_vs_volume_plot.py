import numpy as np
import matplotlib.pyplot as plt

# Load the data
volume_dft, energy_dft = np.loadtxt(r"vasp_files\e05_ionic-relaxation-FF\volume_energy_DFT.dat", unpack=True)
volume_mlff, energy_mlff = np.loadtxt(r"vasp_files\e05_ionic-relaxation-FF\volume_energy_MLFF.dat", unpack=True)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(volume_dft, energy_dft, label="DFT", marker='o')
plt.plot(volume_mlff, energy_mlff, label="MLFF", marker='s')

# Labeling
plt.xlabel("Volume (Å³)")
plt.ylabel("Total energy (eV)")
plt.title("Total Energy vs Volume")
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
