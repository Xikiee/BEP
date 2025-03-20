import os
import numpy as np
import matplotlib.pyplot as plt

def main(): 
    # Use absolute path to ensure the correct file location
    doscar = r"D:\UNI_year_3\BEP\vasp_files\e07_CO-partial-dos\DOSCAR"

    print(f"Looking for DOSCAR file at: {doscar}")

    if not os.path.exists(doscar):
        print(f"Error: File {doscar} not found. Check if the path is correct!")
        return    

    e, d, i = import_dos(doscar)

    plt.figure(figsize=(2, 5))
    plt.plot(e, d, label="DOS")
    plt.plot(e, i, label="Integrated DOS")
    plt.xlabel(r"Energy E-E$_{\mathcal{f}}$ [eV]")
    plt.ylabel("DOS [-]")
    plt.minorticks_on()
    plt.grid(which="major", linewidth = 0.5 )
    plt.grid(which = 'minor', linewidth = 0.2)
    plt.legend()
    plt.show()

def import_dos(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"Error: The file {file} does not exist.")

    try:
        nr_pts = int(np.loadtxt(file, skiprows=5, max_rows=1)[2])
        data = np.loadtxt(file, skiprows=6, max_rows=nr_pts)
    except Exception as e:
        print(f"Error reading {file}: {e}")
        return None, None, None

    e_fermi = np.loadtxt(file, skiprows=5, max_rows=1)[3]
    
    e = data[:, 0] - e_fermi  # Energy
    d = data[:, 1]  # Total DOS
    i = data[:, 2]  # Integrated DOS
    
    return e, d, i

if __name__ == "__main__":
    main()
