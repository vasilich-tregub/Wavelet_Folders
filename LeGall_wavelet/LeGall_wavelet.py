
import numpy as np
from numpy import ndarray
from typing import List, Tuple
from scipy.ndimage import convolve
import imageio
import matplotlib.pyplot as plt
from TimCogan_LeGall_wavelet import WaveletImage

sourceimage = imageio.v3.imread("ducksgrayscale.png")

# high decomposition level of 9
imagedecomp = WaveletImage(np.asarray(sourceimage), levels=9)

plt.figure("9-level decomposition")
plt.imshow(imagedecomp.pixels, cmap="gray")
plt.show()

plt.figure("Recovered grayscale image from 9-level decomp")
recovered = imagedecomp.inverse_transform()
plt.imshow(recovered, cmap="gray")
plt.show()

