"""
Name: Pixel data extraction for raster files

Description: Identify unique pixels for specified raster files. The code will print the 
the list of unique cells - count of unique cells.

Requirements:
 1. Numpy, Gdal(GDAL-3.0.4-cp38-cp38-win_amd64.whl) libraries
 2. The program was written on Python 3.8.0
 3. The raster file and the file location (D:\TESTfolder\2019_test_results\BC\LCV_BC_2019.pix)

Author- Kshipra Basu
Date- Mar 2020

Note: This program is work-in progress with possibilities of being fine tuned.
Recommendation: If required then the code can be modified to export results as csv.


"""
import os
import warnings
import numpy
import scipy
from osgeo import gdal, ogr, osr


#Specifying the Raster File location
src_data = r'D:\TESTfolder\2019_test_results\BC\LCV_BC_2019.pix' 

#Use gdal to extract the data for the specific file.
dataset = gdal.Open(src_data, gdal.GA_ReadOnly)

#Data validation of the input file
if not dataset:
    print("Invalid input")

#Count raster pixel data
#Get the unique pixel values
#Count the values of specific pixel per category
ds_ref = gdal.Open(src_data)
ref_data = ds_ref.ReadAsArray()
uni_class, uni_count = numpy.unique(ref_data,return_counts=True)


#Removing the 0's from the results
#Printing the extracted values
Comparison = "\n".join("{} {}".format(x, y) for x, y in zip(uni_class[uni_class != 0], uni_count[uni_count !=0]))
print (Comparison)