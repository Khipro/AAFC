"""
Name: Changing pixel values for raster files.

Description: This script takes a raster file and creates a new raster file with the following conditions
                1. It can change specific pixel value to a new value - (Has to be specified)
                2. Unless specified it will create the same raster file.
                3. It will maintain same projections
                4. It can change any number of pixel/ any range of pixel, to a different pixel values.
                


Requirements:
 1. This code will run with python 3 and their respective gdal libraries
 2. The program was written on Python 3 >
 3. Input raster file and the file location (ex - E:\AAFC\Thierry\clip7.tif)
 4. Specify the output path of the new raster (ex - E:/AAFC/Thierry/raster_output11.tif)

Author- Kshipra Basu
Date- April 2020

Note: This program is work-in progress with possibilities of being fine tuned.
      The program execution time might vary depending on the file sizes. 
      It may take long time for file execution


"""

import os
import warnings
import numpy
import scipy
from osgeo import gdal, ogr, osr
import struct



def changeRasterValues(band):

    fmttypes = {
        "Byte": "B",
        "UInt16": "H",
        "Int16": "h",
        "UInt32": "I",
        "Int32": "i",
        "Float32": "f",
        "Float64": "d",
    }

    data_type = band.DataType

    BandType = gdal.GetDataTypeName(band.DataType)

    raster = []

    for y in range(band.YSize):

        scanline = band.ReadRaster(0, y, band.XSize, 1, band.XSize, 1, data_type)
        values = struct.unpack(fmttypes[BandType] * band.XSize, scanline)
        raster.append(values)

    raster = [list(item) for item in raster]

    # changing raster values
    # The range or the specific pixel values that needs to be changed
    # If more pixel iteration are needed the conditions can be added. 10 initial operations have been made.

    for i, item in enumerate(raster):
        for j, value in enumerate(item):
            if (
                value == 0
            ):  # The value that needs to be changed from the original raster file
                raster[i][
                    j
                ] = 0  # The new assigned pixel value on the output raster file
            if value == 1:
                raster[i][j] = 1
            if value == 2:
                raster[i][j] = 2
            if value == 3:
                raster[i][j] = 3
            if value == 4:
                raster[i][j] = 4
            if value == 5:
                raster[i][j] = 5
            if value == 6:
                raster[i][j] = 6
            if value == 7:
                raster[i][j] = 7
            if value == 100:
                raster[i][j] = 5
            if value > 200:
                raster[i][j] = 10

    # transforming list in array
    raster = numpy.asarray(raster)

    return raster


if __name__ == "__main__":

    # Specifying the Raster File location
    src_data = r"E:\AAFC\Thierry\clip7.tif"

    # Set name of output raster
    output_file = "E:/AAFC/Thierry/raster_output12.tif"

    # Use gdal to extract the data for the specific file.
    dataset = gdal.Open(src_data, gdal.GA_ReadOnly)

    # Data validation of the input file
    if not dataset:
        print("Invalid input")
    dataset = gdal.Open(src_data, gdal.GA_ReadOnly)

    # Get projection
    prj = dataset.GetProjection()

    # setting band
    number_band = 1

    band = dataset.GetRasterBand(number_band)

    # Get raster metadata
    geotransform = dataset.GetGeoTransform()

    # Create gtif file with rows and columns from parent raster
    driver = gdal.GetDriverByName("GTiff")

    raster = changeRasterValues(band)

    dst_ds = driver.Create(
        output_file, band.XSize, band.YSize, number_band, band.DataType
    )

    # writting output raster
    dst_ds.GetRasterBand(number_band).WriteArray(raster)

    # setting extension of output raster
    # top left x, w-e pixel resolution, rotation, top left y, rotation, n-s pixel resolution
    dst_ds.SetGeoTransform(geotransform)

    # setting spatial reference of output raster
    srs = osr.SpatialReference(wkt=prj)
    dst_ds.SetProjection(srs.ExportToWkt())

    # Close output raster dataset
    dst_ds = None

    # Close main raster dataset
    dataset = None
