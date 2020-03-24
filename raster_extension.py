import os
import warnings
import numpy
import scipy
from osgeo import gdal, ogr, osr

#Importing the raster file form location and validation
src_shp = r'D:\TESTfolder\2019_test_results\BC\LCV_BC_2019.pix' 
dataset = gdal.Open(src_shp, gdal.GA_ReadOnly)
if not dataset:
    print("Invalid input")

#raster data count
ds_ref = gdal.Open(src_shp)
crop_ref_data = ds_ref.ReadAsArray()
uni_class, uni_count = numpy.unique(crop_ref_data,return_counts=True)


#formatting the comparison output
Comparison = "\n".join("{} {}".format(x, y) for x, y in zip(uni_class[uni_class != 0], uni_count[uni_count !=0]))
print (Comparison)