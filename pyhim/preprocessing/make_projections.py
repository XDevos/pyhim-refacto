# -*- coding: utf-8 -*-
"""Project 3D images to 2D"""


import glob
import os

from skimage import io
import numpy as np


def make_projections(image_path, param):

    # creates image object
    img = Image(param)
    # loads image
    img.load_image(image_path)

    # find the correct range for the projection
    if param["zProject"]["zmax"] > img.size[0]:
        # printLog("$ Setting z max to the last plane")
        param["zProject"]["zmax"] = img.size[0]

    if param["zProject"]["mode"] == "automatic":
        # printLog("> Calculating planes...")
        z_range = calculate_zrange(img, param)

    elif param["zProject"]["mode"] == "full":
        (zmin, zmax) = (0, img.size[0])
        z_range = (round((zmin + zmax) / 2), range(zmin, zmax))

    if param["zProject"]["mode"] == "laplacian":
        # printLog("Stacking using Laplacian variance...")
        (
            img.data_2D,
            img.focal_plane_matrix,
            img.z_range,
        ) = reinterpolates_focal_plane(img, param)
        img.focus_plane = img.z_range[0]

    else:
        # Manual: reads from parameters file
        (zmin, zmax) = (
            param["zProject"]["zmin"],
            param["zProject"]["zmax"],
        )
        if zmin >= zmax:
            raise SystemExit("zmin is equal or larger than zmax in configuration file. Cannot proceed.")
        z_range = (round((zmin + zmax) / 2), range(zmin, zmax))

    if "laplacian" not in param["zProject"]["mode"]:
        img.data_2D = projects_image_2D(img, z_range, param["zProject"]["zProjectOption"])
        img.focus_plane = z_range[0]
        img.z_range = z_range[1]


def full_projection(image_path: str, compteur_todelete: int, outdir: str = ""):
    data = io.imread(image_path).squeeze()
    imageSize = data.shape
    (zmin, zmax) = (1, 59)
    zRange = (round((zmin + zmax) / 2), range(zmin, zmax))

    I_collapsed = np.zeros((imageSize[1], imageSize[2]))

    # Sums selected planes
    print("zRange[1] = ", zRange[1])
    for i in zRange[1]:
        I_collapsed += data[i]

    fileName = "/home/xdevos/Documents/testtodelete/try4/" + str(compteur_todelete) + "_2d"
    # print("filename = ", fileName)
    np.save(fileName, I_collapsed)