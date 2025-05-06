import os
from pymatgen.core import Structure

# Ensure the output directory exists
output_dir = "./e01_solid-cd-Si"
os.makedirs(output_dir, exist_ok=True)  # Creates directory if it doesn't exist

# Read CIF file
my_struc = Structure.from_file("vasp_files/e01_solid-cd-Si/Si_mp-149_conventional_standard.cif")

# Make a 2x2x2 supercell
my_struc.make_supercell(2)

# Write supercell to POSCAR format
output_file = os.path.join(output_dir, "POSCAR")
my_struc.to(fmt="poscar", filename=output_file)

print(f"POSCAR file successfully written to: {output_file}")
