import numpy as np
import matplotlib.pyplot as plt
from efficiency_wm import efficiency_wm
import sys

# wk_min = float(sys.argv[1])
# wk_max = float(sys.argv[2])
# wk_steps = int(sys.argv[3])

# number of option for wk, give wkmin, wkmax and number of steps as arguments
wm_min = input(" enter wk_min, eg: 0.04, =  ")
wm_max = input("Enter wk_max, eg: 0.065, =   ")
wm_steps = input("enter wk_step, eg: 5, =  ")
sca_min = input("enter SCA_min, eg: 100, =  ")
sca_max = input("enter SCA_max, eg: 200, =  ")
sca_steps = input("SCA_steps, eg: 10, =   ")

m1 = int(wm_steps)
wm_min = float(wm_min)
wm_max = float(wm_max)
sca_min = float(sca_min)
sca_max = float(sca_max)
# number of sca options
n1 = int(sca_steps)
m1_eff = np.zeros(m1 * n1).reshape(m1, n1)
wm_step = (wm_max - wm_min) / m1
sca_step = (sca_max - sca_min) / n1
k = 0
for m in range(m1):
    wm = wm_min + wm_step * m
    for n in range(n1):
        sca = sca_min + n * sca_step

        m1_eff[m, n] = efficiency_wm(wm, sca)

print(m1_eff)

wm1 = np.zeros(m1)
for n in range(0, m1, 1):
    wm1[n] = wm_min + n * wm_step
print(wm1)

sca1 = np.zeros(n1)
for n in range(0, n1, 1):
    sca1[n] = sca_min + n * sca_step
print(sca1)

for n in range(0, m1, 1):
    plt.plot(sca1, m1_eff[n], label=round(wm1[n], 4))
plt.xlabel('sca(sq.m/m3/s)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs sca')
plt.grid()
plt.legend()
plt.show()

y = np.zeros(m1)
for n in range(0, m1, 1):
    y[n] = m1_eff[n, 0]
# plt.plot(wk1, y)
# plt.show()

m2_eff = np.transpose(m1_eff)

for n in range(0, n1, 1):
    plt.plot(wm1, m2_eff[n], label=sca1[n])
plt.xlabel('wm(m/s)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs wm')
plt.grid()
plt.legend()

plt.show()
