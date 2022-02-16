# -*- coding: utf-8 -*-
"""Parse command-line options, arguments and sub-commands"""


from argparse import ArgumentParser


def _parse_args():
    """Parse run aruments of pyhim_runtime

    Returns:
        ArgumentParser.args: An accessor of run arguments
    """
    parser = ArgumentParser()

    # Root folder, rootFolder ==> folderpath ?
    parser.add_argument("-F", "--rootFolder", help="Folder with images")
    # Optionnal routines
    parser.add_argument("-C", "--cmd", help="Comma-separated list of routines to run (order matters !): makeProjections alignImages \
                        appliesRegistrations alignImages3D segmentMasks \
                        segmentSources3D refitBarcodes3D \
                        localDriftCorrection projectBarcodes buildHiMmatrix")
    # Number of threads
    parser.add_argument("--threads", type=int, default=1, help="Number of threads to run in parallel mode. If none, then it will run with one thread.")

    return parser.parse_args()
