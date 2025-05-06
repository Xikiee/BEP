import numpy as np
import matplotlib.pyplot as plt


# fill the list of volume in the same order as the temperature
volume = [ 319.0671143570013442, 319.1860034993332533  , 319.4367905743336564 ]
temperature = [200, 300, 400]

plt.plot(temperature, volume)
plt.xlabel('temperature')
plt.ylabel('volume')
plt.show()

# finding the thermal expansion 
alpha_v = (1./volume[2]* (volume[2]-volume[0])/(temperature[2]-temperature[0]))
print(f"thermal expansion: {alpha_v}")

print(f"linear expansion coefficient of si, is thermal expansion/3 : {alpha_v/3}")

######## alternatively the same can be done by measuring the lengths of lattice vectors

lattice_vectors = [7.6709362918889177, 7.6723234856666895, 7.6730585861110878]
temp = [200,300,400]
alpha_l = 1./lattice_vectors[1] * (lattice_vectors[2]-lattice_vectors[0])/(temp[2]-temp[0])
print(f'linear expansion coefficient of Si is: {alpha_l}')
plt.plot(temp, lattice_vectors)
plt.show()