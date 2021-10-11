# import packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

os.chdir('E:\Coding\Python\Earth Data Analytics')
# print(os.getcwd())

# Define path to file
plot_centroid_path = os.path.join("Data", "spatial-vector-lidar", 
                                  "california", "neon-sjer-site", 
                                  "vector_data", "SJER_plot_centroids.shp")
# print(plot_centroid_path)
# Import shapefile using geopandas
sjer_plot_locations = gpd.read_file(plot_centroid_path)

sjer_plot_locations.head(6)