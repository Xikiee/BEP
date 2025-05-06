import py4vasp
mycalc = py4vasp.Calculation.from_path( "vasp_files\e03_fcc-Si-band\EIGENVAL" )

mycalc.band.plot()