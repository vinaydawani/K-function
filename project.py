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

def plot_points(pts, area):
    fig, ax = plt.subplots()
    x, y = [p.x for p in points], [p.y for p in points]
    ax.scatter(x, y, facecolor='#006bb3', edgecolor='#99d6ff', marker='.', alpha='0.45')
    plt.xlim(extent[0]+500000, extent[1]+500000)
    plt.ylim(extent[2]-500000, extent[3]+500000)
    plt.title("Airports in North America")
    # plt.xticks([])
    # plt.yticks([])
    ax.axis('off')
    ax.set_aspect(1)
    plt.show()


if __name__ == '__main__':
    driver = ogr.GetDriverByName("ESRI Shapefile")
    fname = input("Enter complete location of Shapefile:")

    airport_points = driver.Open(fname, 0)
    layer = airport_points.GetLayer(0)

    extent = layer.GetExtent()
    area = area = Extent(extent[0], extent[1], extent[2], extent[3])

    points = []
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        p = feature.GetGeometryRef()
        points.append(Point(p.GetPoint(0)[0], p.GetPoint(0)[1]))

    plot_points(points, area)
