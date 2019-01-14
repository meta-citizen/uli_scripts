# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 21:08:25 2019

This file retrieves building data from OSM using OSMNX

To update the location change the X/Y in the pt variable. To find the the
coordinates for this point reference the end of an OSM URL.

https://www.openstreetmap.org/relation/122604#map=19/41.91393/-87.65972

the numbers you are looking for in this case are 41.91393/-87.65972
replace the / with a ,

@author: Zachary Lancaster
"""

#%% SETUP ENVIRONMENT
import os
import osmnx as ox
import overpass as op

path = "D:/GA_SMART_COMMUNITIES_GRA/src"
os.chdir(path)

place = "cincinnati_uli_2019"
pt = (39.09453,-84.51416) #This variable sets the center point
dist = 1500 #this sets the distance around the point that will be retrieved

#NOTE: So far as I can tell this sets the sides of a squre thus it goes
#1/2(dist) in each direction from the center point.

#%% GET BUILDINGS
bldg = ox.buildings_from_point(pt, dist, retain_invalid = True)

fig, bx = ox.plot_buildings(bldg,
                            show = True,
                            save = True,
                            filename = place,
                            file_format = 'svg',
                            dpi = 300)


#%%EXPORT SHAPE
ox.save_gdf_shapefile(bldg, filename = place, folder = path)