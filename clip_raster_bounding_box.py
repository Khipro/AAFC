"""
Name: Raster file extraction of AOI

Description: This script takes a raster file and a shapefile of AOI as an input.
             The output is a Raster file.
             The area of raster file extraction is defined 
             by the max and min of the coordinates of AOI.


Requirements:
 1. Gdal(GDAL-3.0.4-cp38-cp38-win_amd64.whl) libraries
 2. The program was written on Python 3.8.0
 3. Input raster file and the file location (ex - E:/AAFC/Thierry/S2_ON_London2018_v1.tif)
 4. Input Shape file location of the AOI (ex - E:/AAFC/Thierry/AOI.shp)
 5. Specify the output path of the new raster (ex - E:/AAFC/Thierry/clip5.tif)

Author- Kshipra Basu
Date- April 2020

Note: This program is work-in progress with possibilities of being fine tuned.



"""
# Import libraries
from osgeo import gdal, ogr


#Read in datasets
Raster = gdal.Open('E:/AAFC/Thierry/S2_ON_London2018_v1.tif')
VectorDriver = ogr.GetDriverByName('ESRI Shapefile')
Vector = VectorDriver.Open('E:/AAFC/Thierry/AOI.shp', 0)

#Get shapefile bounding box:
layer = Vector.GetLayer()
feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
minX, maxX, minY, maxY = geom.GetEnvelope()
bbox = (minX,maxY,maxX,minY) #Reorder bbox to use with gdal_translate

#Clip raster to shapefile bounding box
clip = gdal.Translate('E:/AAFC/Thierry/clip5.tif', Raster, projWin=bbox)

print(clip)

