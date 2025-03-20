import os
import sys
from visualization_vasp.vasp2xsf import main

# Define folder path
folder = r"vasp_files\e08_H2O-relaxation"

# Change working directory to the VASP files directory
os.chdir(folder)

# Debugging: Print current directory and check if files exist
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

if not os.path.exists("OUTCAR") or not os.path.exists("POSCAR"):
    raise FileNotFoundError("ERROR: Missing required VASP files (OUTCAR or POSCAR).")

# Pass arguments explicitly as strings
sys.argv = ["visualization_for_water.py", "-i", "OUTCAR", "-p", "POSCAR", "-m", "0", "-s", str(1.0)]

# Run the script
main(sys.argv[1:])
