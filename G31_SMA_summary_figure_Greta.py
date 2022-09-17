import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
from numpy import genfromtxt

# spectral lines
CH3CCH1211 = [205.081, 205.076, 205.065, 205.045, 205.018]
H2CS65 = [205.987, 206.054, 206.159, 206.053, 206.053, 206.002, 206.002]
CH3OH54 = [241.791, 241.767, 241.700, 241.879, 241.905, 241.904, 241.842, 241.887, 241.844, 241.833,
           241.833, 241.852, 241.807, 241.807, 241.813, 241.830, 241.203, 241.192, 241.196, 241.206, 241.180, 241.180]
CH3CN1312 = [239.138, 239.133, 239.119, 239.096, 239.064, 239.023]
CH3CCH1413 = [239.252, 239.248, 239.234, 239.211, 239.179]
H2CS76 = [240.267, 240.382, 240.392, 240.393, 240.332, 240.332]
CH3CCH1514 = [256.337, 256.331, 256.317, 256.292, 256.258]
CH3OH76 = [338]
CH3OCHO = [360]
C2H5CN = [355]
C2H5OH = [330]

# array storing all molecules
molecules = [CH3CCH1211, H2CS65, CH3OH54, CH3CN1312, CH3CCH1413,
             H2CS76, CH3CCH1514, CH3OH76, CH3OCHO, C2H5CN, C2H5OH]

# high freq
lo070810 = [[337.4, 333.4, 333.4, 337.4], [3, 3, 5, 5]]
up070810 = [[345.4, 349.4, 349.4, 345.4], [3, 3, 5, 5]]
# low freq
lo070515 = [[225.3-8, 225.3-4, 225.3-4, 225.3-8], [3, 3, 5, 5]]
up070515 = [[225.3+8, 225.3+4, 225.3+4, 225.3+8], [3, 3, 5, 5]]

lo070709 = [[225.3-8, 225.3-4, 225.3-4, 225.3-8], [6, 6, 8, 8]]
up070709 = [[225.3+8, 225.3+4, 225.3+4, 225.3+8], [6, 6, 8, 8]]

lo080518 = [[221.4-8, 221.4-4, 221.4-4, 221.4-8], [9, 9, 11, 11]]
up080518 = [[221.4+8, 221.4+4, 221.4+4, 221.4+8], [9, 9, 11, 11]]

lo080714 = [[221.4-8, 221.4-4, 221.4-4, 221.4-8], [12, 12, 14, 14]]
up080714 = [[221.4+8, 221.4+4, 221.4+4, 221.4+8], [12, 12, 14, 14]]

lo160404 = [[232.7-12, 232.7-4, 232.7-4, 232.7-12], [15, 15, 17, 17]]
up160404 = [[232.7+12, 232.7+4, 232.7+4, 232.7+12], [15, 15, 17, 17]]

lo170611 = [[200.5-12, 200.5-4, 200.5-4, 200.5-12], [18, 18, 20, 20]]
up170611 = [[200.5+12, 200.5+4, 200.5+4, 200.5+12], [18, 18, 20, 20]]

lo170828 = [[200.5-12, 200.5-4, 200.5-4, 200.5-12], [21, 21, 23, 23]]
up170828 = [[200.5+12, 200.5+4, 200.5+4, 200.5+12], [21, 21, 23, 23]]

# Defining colors so it is easier to set facecolor for the polygons
VE = 'green'
E = 'blue'
S = 'orange'
C = 'red'

# Plotting bandwidth; some are assigned to a variable for plotting legend
fig, ax = plt.subplots(figsize=(12, 9))
ext, = ax.fill(lo070810[0], lo070810[1], facecolor=E)
ax.fill(up070810[0], up070810[1], facecolor=E)
vext, = ax.fill(lo070515[0], lo070515[1], facecolor=VE)
ax.fill(up070515[0], up070515[1], facecolor=VE)
com, = ax.fill(lo070709[0], lo070709[1], facecolor=C)
ax.fill(up070709[0], up070709[1], facecolor=C)
ax.fill(lo080518[0], lo080518[1], facecolor=C)
ax.fill(up080518[0], up080518[1], facecolor=C)
ax.fill(lo080714[0], lo080714[1], facecolor=E)
ax.fill(up080714[0], up080714[1], facecolor=E)
ax.fill(lo160404[0], lo160404[1], facecolor=E)
ax.fill(up160404[0], up160404[1], facecolor=E)
sub, = ax.fill(lo170611[0], lo170611[1], facecolor=S)
ax.fill(up170611[0], up170611[1], facecolor=S)
ax.fill(lo170828[0], lo170828[1], facecolor=C)
ax.fill(up170828[0], up170828[1], facecolor=C)

# Legend
vext.set_label('Very Extended')
ext.set_label('Extended')
sub.set_label('Subcompact')
com.set_label('Compact')
ax.legend(loc=2)
plt.ylim([0, 50])

# Plotting spectral lines
ax2 = ax.twinx()
for n in molecules:
    ax2.bar(n, height=30, width=0.5)
# Legend
ax2.legend(['CH3CCH 12-11', 'H2CS 6-5', 'CH3OH 5-4', 'CH3CN 13-12', 'CH3CCH 14-13',
           'H2CS 7-6', 'CH3CCH 15-14', 'CH3OH 7-6', 'CH3OCHO', 'C2H5CN', 'C2H5OH'], loc=1)
plt.ylim([0, 50])

ax.get_yaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax.set_xlabel('frequency [GHz]')
ax.set_title('G31')
plt.show()
