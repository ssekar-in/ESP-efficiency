import numpy as np
import matplotlib.pyplot as plt
from esp_eff import efficiency
import sys

#wk_min = float(sys.argv[1])
#wk_max = float(sys.argv[2])
#wk_steps = int(sys.argv[3])

# number of option for wk, give wkmin, wkmax and number of steps as arguments
wk_min = input(" enter wk_min, eg: 0.17, =  ")
wk_max = input("Enter wk_max, eg: 0.22, =   ")
wk_steps = input("enter wk_step, eg: 5, =  ")
sca_min = input("enter SCA_min, eg: 100, =  ")
sca_max = input("enter SCA_max, eg: 200, =  ")
sca_steps = input("SCA_steps, eg: 10, =   ")

m1 = int(wk_steps)
wk_min = float(wk_min)
wk_max = float(wk_max)
sca_min = float(sca_min)
sca_max= float(sca_max)
# number of sca options
n1 = int(sca_steps)
m1_eff = np.zeros(m1 * n1).reshape(m1, n1)
wk_step = (wk_max - wk_min)/m1
sca_step = (sca_max - sca_min)/n1
k = 0
for m in range(m1):
    wk = wk_min + wk_step * m
    for n in range(n1):
        sca = sca_min + n * sca_step

        m1_eff[m, n] = efficiency(wk, sca)

print(m1_eff)

wk1 = np.zeros(m1)
for n in range(0, m1, 1):
    wk1[n] = wk_min + n * wk_step
print(wk1)

sca1 = np.zeros(n1)
for n in range(0, n1, 1):
    sca1[n] = sca_min + n * sca_step
print(sca1)

for n in range(0, m1, 1):
    plt.plot(sca1, m1_eff[n],label=round(wk1[n], 2))
plt.xlabel('sca(sq.m/m3/s)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs sca')
plt.grid()
plt.legend()
plt.show()

y = np.zeros(m1)
for n in range(0, m1, 1):
    y[n] = m1_eff[n, 0]
#plt.plot(wk1, y)
#plt.show()

m2_eff = np.transpose(m1_eff)

for n in range(0, n1, 1):
    plt.plot(wk1, m2_eff[n], label=sca1[n])
plt.xlabel('wk(m/s)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs wk')
plt.grid()
plt.legend()

plt.show()
