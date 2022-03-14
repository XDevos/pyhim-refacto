"""Manage the data reading and writing, checks also existence and consistency.
"""


import os

from enum import Enum


class DataManager():
    """Store and check all parameters"""
    def __init__(self, run_args):
        """Take and check run arguments to initiate a DataManager object

        Args:
            run_args (ArgumentParser.args): Product of parse_args() method from an ArgumentParser object initiate with run arguments of pyhim_runtime 

        Raises:
            SystemExit: Thread number should be 1 or more
            SystemExit: Unknown command
        """
        # TODO printLog ==> print_log
        #print_log("\n--------------------------------------------------------------------------")
        
        self._AVAILABLE_COMMANDS = ["makeProjections", "appliesRegistrations","alignImages","alignImages3D", "segmentMasks",\
                        "segmentSources3D","refitBarcodes3D","localDriftCorrection","projectBarcodes","buildHiMmatrix"]

        self._DEFAULT_COMMANDS = ["makeProjections", "appliesRegistrations","alignImages","alignImages3D", "segmentMasks",\
                        "segmentSources3D","buildHiMmatrix"]
        self.run_parameters = {}

        # TODO log(...) & session(...) system
        # self.sessionName = sessionName
        # self.log1 = log(rootFolder=self.rootFolder, parallel=self.parallel)
        # self.session1 = session(self.rootFolder, self.sessionName)

        if run_args.rootFolder:
            self.run_parameters["rootFolder"] = run_args.rootFolder
        else:
            if "docker" in os.environ.keys():
                self.run_parameters["rootFolder"] = "/data"
                #print_log("\n\n$ Running in docker, HiMdata: {}".format(self.run_parameters["rootFolder"]))
            else:
                #print_log("\n\n# HiMdata: NOT FOUND")
                self.run_parameters["rootFolder"] = os.getenv("PWD")  # os.getcwd()

        if run_args.threads >= 1:
            self.run_parameters["threads"] = run_args.threads
            self.run_parameters["parallel"] = run_args.threads != 1
        else:
            raise SystemExit    # Thread number should be 1 or more

        if run_args.cmd:
            self.run_parameters["cmd"] = run_args.cmd.split(",")
        else:
            self.run_parameters["cmd"] = self._DEFAULT_COMMANDS

        # Check consistency of command list
        for cmd in self.run_parameters["cmd"]:
            if cmd not in self._AVAILABLE_COMMANDS:
                # TODO: print log msg error
                raise SystemExit    # Unknown command

        # TODO printDict ==> print_dict
        # printDict(self.run_parameters)



    def check_consistency(self):
        """[summary]
        """
        pass

def extract_images(dirname: str, extensions = (".tif")):
    """Extract filepaths of all images with accepted extensions into a given directory 

    Parameters
    ----------
    dirname : str
        The name of root directory
    extensions : tuple, optional
        The accepted filename extensions, by default (".tif")

    Returns
    -------
    list[str]
        The list of image filepaths
    """
    images = []
    # Iterate into dirname and each subdirectories
    for root, subdirs, filenames in os.walk(dirname):
        for filename in filenames:
            # Check extension file
            if(filename.endswith(extensions)):
                
                images.append(os.path.join(root, filename))
    return images
