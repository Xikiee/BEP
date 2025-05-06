from pymatgen.core import Structure

my_structure = Structure.from_file("vasp_files\e03_monitoring\Si_mp-149_conventional_standard.cif", primitive = True)

# create a 2x2x2 supercell 
supercell = my_structure * (2,2,2)

#write to POSCAR format
supercell.to(fmt="poscar", filename="vasp_files\e03_monitoring\POSCAR")