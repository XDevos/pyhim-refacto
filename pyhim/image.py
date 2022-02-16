import numpy as np
from skimage import io


class Image():

    def __init__(self):
        self.name = ""
        self.extension = ""
        self.raw_XY = ""
        self.raw_3D = ""
        self.registered_XY = ""
        self.registered_3D = ""
        self.shift_XY = ""
        self.shift_3D = ""
        self.reference = ""

    def load(self, filepath):
        return io.imread(filepath).squeeze()

    def save(self, filepath, data):
        np.save(filepath, data)

    def project(self):
        pass

    def apply_registration(self):
        pass

    def filter(self):
        pass

class Fiducial(Image):
    def __init__(self):
        super(Fiducial, self).__init__()

    def align_XY(self):
        pass

    def align_3D(self):
        pass

class Barcode(Image):
    def __init__(self):
        super(Barcode, self).__init__()

    def detect_XY(self):
        pass

    def detect_3D(self):
        pass


class Dapi(Image):
    def __init__(self):
        super(Dapi, self).__init__()

    def segment_XY(self):
        pass



class Rna(Image):
    def __init__(self):
        super(Rna, self).__init__()