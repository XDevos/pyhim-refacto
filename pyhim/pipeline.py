# -*- coding: utf-8 -*-
"""Schedules successive executions of features according to run arguments and parallelization option.
"""


import run_args
import data_manager


class Pipeline():

    def __init__(self, run_args, manager):
        self.stack = []

        if "makeProjections" in manager.run_parameters["cmd"]:
            self.stack.append("make_projections")
    

    def run(self):
        # TODO see Callable module to exe a pipe stack
        pass
