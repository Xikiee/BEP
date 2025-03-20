import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ase.io import read
from ase import Atoms
from ase.neighborlist import NeighborList

def read_vasprun(filepath):
    """Read atomic positions from vasprun.xml using ASE."""
    try:
        atoms = read(filepath, format='vasp-xml')
        return atoms
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def calculate_bond_lengths(atoms, cutoff=2.0):
    """Calculate bond lengths using ASE's NeighborList."""
    nl = NeighborList(cutoffs=[cutoff / 2] * len(atoms), self_interaction=False, bothways=True)
    nl.update(atoms)
    bond_lengths = []
    for i in range(len(atoms)):
        indices, offsets = nl.get_neighbors(i)
        for j, offset in zip(indices, offsets):
            if j > i:  # Avoid double counting
                distance = np.linalg.norm(atoms.positions[j] - atoms.positions[i] + np.dot(offset, atoms.get_cell()))
                bond_lengths.append(distance)
    return bond_lengths

def plot_3d_model(atoms, bond_lengths):
    """Plot a 3D model of the molecule with bond lengths."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot atoms
    positions = atoms.positions
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='b', s=100, label='Atoms')
    
    # Plot bonds
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            distance = np.linalg.norm(positions[j] - positions[i])
            if distance < 2.0:  # Adjust cutoff as needed
                ax.plot([positions[i][0], positions[j][0]],
                        [positions[i][1], positions[j][1]],
                        [positions[i][2], positions[j][2]], 'k-')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D Model of the Molecule')
    plt.legend()
    plt.show()

def main(folder_path):
    """Main function to process VASP files and generate 3D model."""
    vasprun_path = os.path.join(folder_path, 'vasprun.xml')
    if not os.path.exists(vasprun_path):
        print(f"Error: {vasprun_path} not found!")
        return
    
    atoms = read_vasprun(vasprun_path)
    if atoms is None:
        return
    
    bond_lengths = calculate_bond_lengths(atoms)
    if not bond_lengths:
        print("No bonds found within the cutoff distance.")
        return
    
    # Print average bond length
    average_bond_length = np.mean(bond_lengths)
    print(f"Average Bond Length: {average_bond_length:.3f} Å")
    
    # Plot 3D model
    plot_3d_model(atoms, bond_lengths)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python vasp_visualizer.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        main(folder_path)

main(f"vasp_files\e08_H2O-relaxation")