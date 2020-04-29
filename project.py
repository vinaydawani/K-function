#!/usr/bin/env python
# coding: utf-8
import sys
sys.path.append(
    '/Users/vinaydawani/Library/Mobile Documents/com~apple~CloudDocs/SP20/GEOG5222/gisalgs')
import matplotlib.pyplot as plt
import numpy as np
import random
from osgeo import ogr
from math import log10, ceil
from geom.point import *
from indexing.extent import *
from indexing.kdtree1 import *
from indexing.kdtree2b import *
from spatialanalysis.kfunction import *

if __name__ == '__main__':
    driver = ogr.GetDriverByName("ESRI Shapefile")
    fname = input("Enter complete location of Shapefile:")

    airport_points = driver.Open(fname, 0)
    layer = airport_points.GetLayer(0)

    points = []
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        p = layer.GetFeature(i).GetGeometryRef()
        points.append(Point(p.GetPoint(0)[0], p.GetPoint(0)[1]))
