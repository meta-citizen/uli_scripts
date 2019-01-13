# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:07:17 2019

This script retrieves information concerning the road network. This data
can help determine a wide range of issues from block size to the appropriateness
of transportation infrastructure.

Sections found in the Chloroplethic Mapping section give options for representation
through the Netwrokx and and matplotlib packages. Additional information can 
be found within their documentation.

@author: lanca
"""

#%%SETUP ENVIRONMENT
import os
import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors

path = "D:/GA_SMART_COMMUNITIES_GRA/src"
os.chdir(path)

place = "chicago_il_41_87"
pt = (41.91351,-87.66099) #This variable sets the center point
dist = 1000 #this sets the distance around the point that will be retrieved

#NOTE: So far as I can tell this sets the sides of a squre thus it goes
#1/2(dist) in each direction from the center point.

#%%GRAB NETWORK

bbox = ox.bbox_from_point(pt, dist, project_utm = True, return_crs = True)
bbox_poly = ox.bbox_to_poly(bbox[0],bbox[1],bbox[2],bbox[3])

grph_road = ox.graph_from_point(pt,
                                dist,
                                distance_type = 'bbox',
                                network_type = 'all'
                                )

#get rail lines, locating stations is proving to be difficult.
grph_rail = ox.graph_from_point(pt,
                           dist,
                           distance_type = 'bbox',
                           network_type = 'all',
                           infrastructure = 'way["railway"]')

fig, ax = ox.plot_graph(grph_road,
                        show = True,
                        save = True,
                        file_format = 'svg',
                        filename = place +"_network",
                        dpi = 300,
                        node_color = '#000000',
                        node_size = 7
                        )
ox.save_graph_shapefile(grph, filename = place+"_network", folder = path)

#%% GRAB NETWORK STATS

S = ox.stats.basic_stats(grph_road, area = bbox_poly.area)
ES = ox.stats.extended_stats(grph_road, anc = True)
avg_blk_edge = S['street_length_avg']

#%% GENERATE CHLOROPLETHIC MAP
edge_centrality = nx.closeness_centrality(nx.line_graph(G))
ev = [edge_centrality[edge + (0,)] for edge in G.edges()]

norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
cmap = cm.ScalarMappable(norm=norm, cmap=cm.cool)
ec = [cmap.to_rgba(cl) for cl in ev]

fig, ax = ox.plot_graph(G, bgcolor = 'white', axis_off = True, node_size=0,
                        edge_color = ec, edge_linewidth = 1, edge_alpha = 1,
                        filename = grf_out, file_format = frmt,
                        save = True)
