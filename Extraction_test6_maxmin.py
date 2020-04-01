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
clip = gdal.Translate('E:/AAFC/Thierry/clip4.tif', Raster, projWin=bbox)

print(clip)


