import math
import numpy as np


def efficiency_wm(wk_l, sca_l):
    eff2 = 1 - pow(math.e, (-(wk_l * sca_l)))
    return eff2