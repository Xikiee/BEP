import os
import numpy as np
from ase.io import read
from ase.visualize import view
from ase.build import make_supercell

def find_vasp_file(folder):
    """Finds the first available VASP file in the folder."""
    for filename in ["CONTCAR", "POSCAR", "OUTCAR"]:
        file_path = os.path.join(folder, filename)
        if os.path.exists(file_path):
            return file_path
    return None

def compute_bond_angle(a, b, c):
    """Computes the bond angle between three atoms."""
    ba = a - b
    bc = c - b
    cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))  # Clip to avoid floating-point errors
    return np.degrees(angle)

def visualize_vasp_structure(folder):
    """Opens and visualizes the first available VASP structure file in the folder."""
    vasp_file = find_vasp_file(folder)
    
    if vasp_file:
        atoms = read(vasp_file, format='vasp')  # Ensure correct format
        
        # Convert fractional coordinates to Cartesian explicitly
        if atoms.get_pbc().any():  # Check if the system is periodic
            atoms.set_positions(atoms.get_scaled_positions() @ atoms.cell)  # Convert fractional to Cartesian
            atoms.wrap()  # Wrap atoms correctly into the unit cell
            atoms = atoms.copy()  # Ensure ASE recognizes updates
        
        # Create a supercell with 8 simple lattices (2x2x2 expansion)
        supercell_matrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
        atoms = make_supercell(atoms, supercell_matrix)
        
        # Check for bond length discrepancies if at least 3 atoms are present
        if len(atoms) >= 3:
            d1 = np.linalg.norm(atoms[0].position - atoms[1].position)
            d2 = np.linalg.norm(atoms[0].position - atoms[2].position)
            angle = compute_bond_angle(atoms[1].position, atoms[0].position, atoms[2].position)
            
            print(f"O-H1 distance: {d1:.3f} Å, O-H2 distance: {d2:.3f} Å")
            print(f"H-O-H angle: {angle:.2f}°")
            
            if abs(d1 - d2) > 0.1:
                print("Warning: Significant bond length discrepancy detected!")
            if abs(angle - 105) > 5:
                print("Warning: H-O-H bond angle deviation detected! Possible periodic boundary issue.")
        
        view(atoms)
    else:
        print("No VASP structure file (CONTCAR, POSCAR, OUTCAR) found in the folder.")

if __name__ == "__main__":
    folder = input("Enter the folder path containing VASP files: ")
    visualize_vasp_structure(folder)
