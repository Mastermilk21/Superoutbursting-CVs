import numpy as np
import matplotlib.pyplot as plt

from boundry_analysis import BoundryLightCurve

sector = "13"
object_name = "2019krj"

filename = f"c:/Users/eitan/code repos/data/extracted tarballs/sector{sector}/lc_{object_name}_cleaned.txt"


x_min = 2959.5
x_max = 2964.6
height = 0.009
analyze = BoundryLightCurve(filename, x_min=x_min, x_max=x_max, height=height)
analyze.plot_lightcurve()
analyze.newfastplot()
#analyze.phasefold(0.0583597)  # Example period, adjust as needed
#analyze.plot_combined()
#analyze.phasefold()
#analyze.plotposter()
#analyze.bounded_lightcurve()

