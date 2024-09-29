# Based on Tim Cogen's blog post LeGall-Tabatabai wavelet transform (https://tim.cogan.dev/lgt-wavelet/)
# minor additions and corrections in this version are marked with code comments (###)
### 'imports' added
import numpy as np
from numpy import ndarray
from typing import List, Tuple
from scipy.ndimage import convolve

class WaveletImage:
    def __init__(self, image: ndarray, axis: int = 1, levels: int = 2) -> None:
        self.axis = axis
        self.lo, self.hi = self.transform(image, self.axis, levels)

    @property
    def pixels(self) -> ndarray:
        lo = norm_image(self.lo if isinstance(self.lo, ndarray) else self.lo.pixels)
        hi = norm_image(self.hi if isinstance(self.hi, ndarray) else self.hi.pixels)
        return np.concatenate([lo, hi], axis=self.axis)
    
    @staticmethod
    def convolve(x: ndarray, kernel: List[int], axis: int, index: int) -> ndarray:
        k = np.array([kernel])
        if axis == 0:
            k = k.T
        y = convolve(x, k, mode="mirror")
        if axis == 0:
            return y[index::2]
        elif axis == 1:
            return y[:, index::2]
        else:
            raise ValueError(f"axis '{axis}' must be 0 or 1")
    
    def lowpass(self, x: ndarray, axis: int) -> ndarray:
        return self.convolve(x, [-1, 2, 6, 2, -1], axis, 1)

    def highpass(self, x: ndarray, axis: int) -> ndarray:
        return self.convolve(x, [-1, 2, -1], axis, 0)
    
    def inv_lowpass(self, x: ndarray, axis: int) -> ndarray:
        return self.convolve(x, [-1, 1, -1], axis, 1)
    
    def inv_highpass(self, x: ndarray, axis: int) -> ndarray:
        return self.convolve(x, [-4, 4, 24, 4, -4], axis, 0)
    
    def inverse_transform(self) -> ndarray:
        lo: ndarray = self.lo if isinstance(self.lo, ndarray) else self.lo.inverse_transform()
        hi: ndarray = self.hi if isinstance(self.hi, ndarray) else self.hi.inverse_transform()
        x = interleave(hi, lo, self.axis)
        x_evens = self.inv_highpass(x, self.axis) // 64 * 2 ### factor 2 is required to save the brightness of recovered image
        x_odds = self.inv_lowpass(x, self.axis) // 8 * 2    ### with wavelet levels param value > 3
        return interleave(x_evens, x_odds, self.axis)
    
    def transform(self, x: ndarray, axis: int, levels: int) -> Tuple[ndarray, ndarray]:
        lo = self.lowpass(x / 2, axis)
        hi = self.highpass(x / 2, axis)
        lo = WaveletImage(lo, abs(axis - 1), levels - axis) if levels else lo
        hi = WaveletImage(hi, axis=0, levels=0) if axis == 1 else hi
        return lo, hi

### norm_image, interleave defs added are borrowed from the code found in https://tim.cogan.dev/wavelet/
def norm_image(x: ndarray) -> ndarray:
    return (x - x.min()) / (x.max() - x.min())


def interleave(a: ndarray, b: ndarray, axis: int) -> ndarray:
    rows, cols = a.shape
    rows, cols = (rows * 2, cols) if axis == 0 else (rows, cols * 2)
    out = np.empty((rows, cols), dtype=a.dtype)
    if axis == 0:
        out[0::2] = a
        out[1::2] = b
    elif axis == 1:
        out[:, 0::2] = a
        out[:, 1::2] = b
    else:
        raise ValueError("interleave only supports axis of 0 or 1")
    return out
