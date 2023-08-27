from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)

global __BMFRM_DEBUG__
__BMFRM_DEBUG__ = False

global __BMFRM_PARAMS__
__BMFRM_PARAMS__ = dict()

class Beamformer(ABC):
    __bmfrm_id_counter__ = int(0)

    def __init__(self):
        self.id = int(Beamformer.__bmfrm_id_counter__)
        logger.info(f"Generated beamformer with ID: {self.id}")
        __BMFRM_PARAMS__[self.id] = dict()
        Beamformer.__bmfrm_id_counter__ += int(1)

    @abstractmethod
    def __call__(self, data):
        """Form beamformed data"""
        raise NotImplementedError

    def free(self):
        logger.info("Freeing shared memory resources...")
        del __BMFRM_PARAMS__[self.id]
