from osgeo import gdal, ogr

OutTile = gdal.Warp('E:/AAFC/Thierry/cut.tif', #the outputfile
                     'E:/AAFC/Thierry/S2_ON_London2018_v1.tif', #the input raster
                    cutlineDSName='E:/AAFC/Thierry/AOI.shp', #the shapefile
                    cropToCutline=True,
                    dstNodata = 0)

OutTile = None 