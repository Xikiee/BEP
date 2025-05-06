import matplotlib.pyplot as plt

def read_doscar(filepath):
    """
    Reads a DOSCAR file and extracts the total energy and ion energy values for each step.
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Skip the header lines (first 5 lines)
    data_lines = lines[5:]

    total_energies = []
    ion_energies = []
    
    for line in data_lines:
        if line.strip():  # Skip empty lines
            parts = line.split()
            if len(parts) >= 3:  # Ensure there are enough columns
                try:
                    total_energy = float(parts[1])  # Assuming the second column is the total energy
                    ion_energy = float(parts[2])    # Assuming the third column is the ion energy
                    total_energies.append(total_energy)
                    ion_energies.append(ion_energy)
                except ValueError:
                    continue  # Skip lines that don't have valid float values

    return total_energies, ion_energies

def plot_energies(total_energies, ion_energies):
    """
    Plots total energy and ion energy vs step.
    """
    steps = range(1, len(total_energies) + 1)
    
    plt.figure(figsize=(8, 6))
    
    plt.plot(steps, total_energies, linestyle='-', color='b', label='Total Energy')
    plt.plot(steps, ion_energies, linestyle='--', color='r', label='Ion Energy')
    plt.xlim(0,100)
    plt.xlabel('Step')
    plt.ylabel('Energy (eV)')
    plt.title('Total Energy and Ion Energy vs Step')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    doscar_path = input("Enter the path to the DOSCAR file: ")
    try:
        total_energies, ion_energies = read_doscar(doscar_path)
        if total_energies and ion_energies:
            plot_energies(total_energies, ion_energies)
        else:
            print("No energy data found in the DOSCAR file.")
    except FileNotFoundError:
        print(f"File not found: {doscar_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
