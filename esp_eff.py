import math
import numpy as np


def efficiency(wk_l, sca_l):
    eff2 = 1 - pow(math.e, (-np.sqrt(wk_l * sca_l)))
    return eff2
