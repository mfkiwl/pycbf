import numpy as np
from cinpy import copy2c
from interp.engines import IntCub1DSet_Buffer
from pycbf.Beamformer import Beamformer
from pyusel_types import TXType, RXType, Aperture, Data

class GenBeamformer(Beamformer):
    def __init__(self, points:np.ndarray, tx:TXType, rx:RXType, ap:Aperture, taxis='t', txaxis='tx', rxaxis='rx'):
        self.tx = tx
        self.rx = rx
        self.ap = ap
        self.points = points
        self.cpoints, self.cNp, _ = copy2c(points)
        self.taxis = taxis
        self.txaxis = txaxis
        self.rxaxis = rxaxis

        self.tx.c_gen(self.cpoints, self.cNp.value)
        self.rx.c_gen(self.cpoints, self.cNp.value)
        self.ap.c_gen(self.cpoints, self.cNp.value)

    def __call__(self, data):
        """Convert a 3D numpy tensor of channel data to beamformed images
        Uses cubic interpolation
        """
        IntCub1DSet_Buffer(N=self.cNp.value, M=self.rx.Nrx)
        pass
