import numpy as np
import matplotlib.pyplot as plt


######3 this does not work, fix sometime later, but not now L bozo

def read_eigenval(file_path):
    """Reads the EIGENVAL file and extracts the band structure data."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # VASP EIGENVAL file structure reference:
    num_header_lines = 5  # Skip first 5 lines
    system_info = lines[num_header_lines].split()
    num_kpoints = int(system_info[1])
    num_bands = int(system_info[2])

    kpoints = []
    bands = [[] for _ in range(num_bands)]

    index = num_header_lines + 1
    for _ in range(num_kpoints):
        if index >= len(lines):  # Check if index exceeds available lines
            break

        kpoint_info = lines[index].split()

        if len(kpoint_info) < 4:  # Ensure the k-point data is correctly formatted
            print(f"Skipping malformed line: {lines[index]}")
            index += 1
            continue

        kpoints.append(float(kpoint_info[-1]))  # Take k-point distance
        index += 1

        for band_idx in range(num_bands):
            if index >= len(lines):  # Check if index exceeds available lines
                break

            band_info = lines[index].split()

            if len(band_info) < 2:  # Ensure that band data has enough information
                print(f"Skipping malformed line: {lines[index]}")
                index += 1
                continue

            bands[band_idx].append(float(band_info[1]))  # Energy value
            index += 1

    return np.array(kpoints), np.array(bands)

def plot_band_structure(eigenval_path):
    kpoints, bands = read_eigenval(eigenval_path)

    plt.figure(figsize=(8, 6))
    for band in bands:
        plt.plot(kpoints, band, 'b-')

    plt.xlabel("Wave Vector k")
    plt.ylabel("Energy (eV)")
    plt.title("Band Structure")
    plt.axhline(0, color='k', linestyle='--', linewidth=0.7)  # Fermi level reference
    plt.show()

if __name__ == "__main__":
    eigenval_file = "vasp_files/e03_fcc-Si-band/EIGENVAL"
    plot_band_structure(eigenval_file)
