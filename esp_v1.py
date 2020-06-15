import numpy as np
import matplotlib.pyplot as plt
from esp_eff import efficiency

eff1 = [[], [], [], [], []]
for n in range(0, 5, 1):
    wk: float = 0.17 + n * 0.01
    sca = np.arange(100, 200, 5)
    eff = efficiency(wk, sca)
    print("wk=", wk, "sca=", sca, "eff=", eff)
    eff1[n] = eff
sca = np.arange(100, 200, 5)
for n in range(0, 5, 1):
    color = ['r', 'g', 'b', 'r--', 'g--']
    marking = ['wk=.17', 'wk=.18', 'wk=.19', ' wk=.2', 'wk=.21']
    plt.plot(sca, eff1[n], color[n], label=marking[n])
plt.xlabel('sca(sq.m/m3/s)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs sca')
plt.grid()
plt.legend()

plt.show()
