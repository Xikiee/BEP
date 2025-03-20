import os
from ase.io import read
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def load_structure(folder_path):
    """Load atomic structure from POSCAR or CONTCAR file in the specified folder."""
    poscar_path = os.path.join(folder_path, 'POSCAR')
    contcar_path = os.path.join(folder_path, 'CONTCAR')
    
    if os.path.exists(poscar_path):
        atoms = read(poscar_path, format='vasp')
    elif os.path.exists(contcar_path):
        atoms = read(contcar_path, format='vasp')
    else:
        raise FileNotFoundError(f"Neither POSCAR nor CONTCAR found in {folder_path}.")
    
    # Ensure correct atomic composition
    symbols = atoms.get_chemical_symbols()
    num_O = symbols.count("O")
    num_H = symbols.count("H")
    
    if num_O != 1 or num_H != 2:
        raise ValueError("Error: The structure does not match H2O (1 Oxygen, 2 Hydrogens). Check the input file.")
    
    return atoms

def plot_structure(atoms):
    """Plot a 3D visualization of the H2O molecule with correct bonding."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    positions = atoms.get_positions()
    symbols = atoms.get_chemical_symbols()
    
    # Identify the oxygen and hydrogen atoms
    oxygen_index = symbols.index("O")
    hydrogen_indices = [i for i, s in enumerate(symbols) if s == "H"]
    
    # Plot atoms with color-coding
    color_map = {"H": "white", "O": "red"}
    for i, (x, y, z) in enumerate(positions):
        ax.scatter(x, y, z, color=color_map.get(symbols[i], 'gray'), s=200, edgecolors='black')
        ax.text(x, y, z, symbols[i], fontsize=10, ha='center', va='center')
    
    # Draw bonds only between oxygen and hydrogens
    bond_lengths = []
    for h_index in hydrogen_indices:
        dist = np.linalg.norm(positions[oxygen_index] - positions[h_index])
        ax.plot([positions[oxygen_index][0], positions[h_index][0]],
                [positions[oxygen_index][1], positions[h_index][1]],
                [positions[oxygen_index][2], positions[h_index][2]],
                color='black', linestyle='-', linewidth=2)
        bond_lengths.append(dist)
        print(f"Bond between O-H: {dist:.2f} Å")
    
    # Calculate and print average bond length
    avg_bond_length = np.mean(bond_lengths)
    print(f"Average O-H bond length: {avg_bond_length:.2f} Å")
    
    # Set aspect ratio for a proper 3D representation
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel("X (Å)")
    ax.set_ylabel("Y (Å)")
    ax.set_zlabel("Z (Å)")
    ax.set_title("3D Visualization of H2O with Correct Bonding")
    plt.show()

def main(folder_path):
    """Main function to load and visualize the structure from a specified folder."""
    try:
        atoms = load_structure(folder_path)
        plot_structure(atoms)
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing VASP files: ")
    main(folder_path)