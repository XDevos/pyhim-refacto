#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main file of pyHiM execution, include the top-level mechanism of pyHiM."""


import os


from run_args import _parse_args
from data_manager import DataManager, extract_images
from pipeline import Pipeline
from preprocessing.make_projections import full_projection


if __name__ == "__main__":
    run_args = _parse_args()

    manager = DataManager(run_args)
    # manager.check_consistency()
    os.makedirs("/home/xdevos/Documents/testtodelete/try4", exist_ok=True)

    images = extract_images(manager.run_parameters["rootFolder"])

    compteur_todelete = 0
    for img in images:
        print("img = ", img)
        full_projection(img, compteur_todelete)
        compteur_todelete += 1
    # pipe = Pipeline(run_args, manager)
    # pipe.run()