######  Import required libraries #########
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import pandas as pd
from pathlib import Path as Path
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt, dates
import numpy as np
import numpy as np
from matplotlib import gridspec
import os
import glob
import dataframe_image as dfi
import itertools
import matplotlib.patheffects as pe
import matplotlib.dates as mdates
# from matplotlib.dates import DateFormatter
from matplotlib.dates import YearLocator, DateFormatter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

import warnings
warnings.filterwarnings('ignore')


################## Reading data for Stations  ###############
dat = pd.read_fwf('file path', 
                  names = ['Station', 'Longitude', 'Latitude', 'St'])

##### Functoin to Draw a zebra border around maps ############

crs = ccrs.PlateCarree()
def add_zebra_frame(ax, lw=4, crs="pcarree", zorder=None):

    ax.spines["geo"].set_visible(False)
    left, right, bot, top = ax.get_extent()
    
    # Alternate black and white line segments
    bws = itertools.cycle(["k", "white"])

    xticks = sorted([left, *ax.get_xticks(), right])
    xticks = np.unique(np.array(xticks))
    yticks = sorted([bot, *ax.get_yticks(), top])
    yticks = np.unique(np.array(yticks))
    for ticks, which in zip([xticks, yticks], ["lon", "lat"]):
        for idx, (start, end) in enumerate(zip(ticks, ticks[1:])):
            bw = next(bws)
            if which == "lon":
                xs = [[start, end], [start, end]]
                ys = [[bot, bot], [top, top]]
            else:
                xs = [[left, left], [right, right]]
                ys = [[start, end], [start, end]]

            # For first and lastlines, used the "projecting" effect
            capstyle = "butt" if idx not in (0, len(ticks) - 2) else "projecting"
            for (xx, yy) in zip(xs, ys):
                ax.plot(
                    xx,
                    yy,
                    color=bw,
                    linewidth=lw,
                    clip_on=False,
                    transform=crs,
                    zorder=zorder,
                    solid_capstyle=capstyle,
                    # Add a black border to accentuate white segments
                    path_effects=[
                        pe.Stroke(linewidth=lw + 1, foreground="black"),
                        pe.Normal(),
                    ],
                )
                
                
#####################  Plot for  study Area ###########################
plt.figure(figsize=(10,9))                         ###### Specifying the size of the figure
ax = plt.axes(projection = ccrs.PlateCarree())       ###### Specifying the type of geopatial plot
ax.add_feature(cf.COASTLINE,alpha=0.8)             
ax.add_feature(cf.BORDERS)
#ax.add_feature(cf.LAND)
ax.set_extent([-3.2,0.8,11.2,4.5])                   #### setting the map boundaries
#ax.stock_img()
ax.add_feature(cf.STATES, alpha= 0.1)               ####  adding territorial boundaries

ax.plot(dat.Longitude,                            
        dat.Latitude, 
        'ro',                                       ##### plotting the longitudes and latitudes of the station
        ms=7, 
        color = 'k')#,
# for longitude, latitude, name in zip(dat.Longitude, dat.Latitude, dat.Station):
#     if name in ['Damongo', 'Kete_Krachi', 'Wa', 'Bole', 'Tamale', 'Yendi']:
#         ax.plot(dat.Longitude,                            
#                 dat.Latitude, 
#                 'ro',                                       ##### plotting the longitudes and latitudes of the station
#                 ms=7, 
#                 color = 'k')
        #transform=ccrs.Geodetic(),label='Synoptic stations')  

s_stations = np.asarray(dat.Station)
                          
for longitude, latitude, name in zip(dat.Longitude, dat.Latitude, dat.Station):
#     if name in ['Damongo', 'Kete_Krachi', 'Wa', 'Bole', 'Tamale', 'Yendi']:
#         ax.text(longitude + .05, latitude + .15, 
#                 name, 
#                 va='center',
#                 ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '7')
#     if name in ['Navrongo']:
#         ax.text(longitude - 0.4, latitude, 
#                 name, 
#                 va='center',
#                 ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '15')
    if name in ['Zuarungu']:
        ax.text(longitude , latitude-0.1, 
                name, 
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '7')
    # else:    
    #     ax.text(longitude + .05, latitude + .12,     
    else:    
        ax.text(longitude + .05, latitude + .12, 
                name, 
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '7')


ax.set_xticks([-3.5,-3,-2.5,-2.0,-1.5,-1.0,-0.5,0,0.5, 1.0, 1.5], crs=ccrs.PlateCarree())
ax.set_yticks([11,10.5,10,9.5,9.0,8.5,8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
add_zebra_frame(ax, lw=4, crs=crs)

plt.title('GHANA MAP', fontweight='bold', fontsize='40')

# #plt.savefig('Synoptic Stations.pdf',bbox_inches = 'tight')
# plt.savefig('Graphs/graphs/Study_Area.JPEG',bbox_inches = 'tight')
