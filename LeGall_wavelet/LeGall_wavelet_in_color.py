
import numpy as np
import imageio
import matplotlib.pyplot as plt
from TimCogan_LeGall_wavelet import WaveletImage
import PIL.Image

sourceimage = imageio.v3.imread("ducks.png")
plt.figure("Source image")
plt.imshow(sourceimage)
plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])
ax3.set_xticks([])
ax3.set_yticks([])

fig.suptitle("Wavelet decomposition")

lvls=3

red = sourceimage.flatten()[0::3].reshape(sourceimage.shape[0:2])
reddecomp = WaveletImage(np.asarray(red), levels=lvls)

ax1.imshow(reddecomp.pixels, cmap="Reds")

green = sourceimage.flatten()[1::3].reshape(sourceimage.shape[0:2])
greendecomp = WaveletImage(np.asarray(green), levels=lvls)

ax2.imshow(greendecomp.pixels, cmap="Greens")

blue = sourceimage.flatten()[2::3].reshape(sourceimage.shape[0:2])
bluedecomp = WaveletImage(np.asarray(blue), levels=lvls)

ax3.imshow(bluedecomp.pixels, cmap="Blues")

plt.tight_layout()
plt.show()

plt.figure("Recovered image")
redrecovered = reddecomp.inverse_transform().astype(np.uint8)
greenrecovered = greendecomp.inverse_transform().astype(np.uint8)
bluerecovered = bluedecomp.inverse_transform().astype(np.uint8)
colorimagedata = np.dstack([redrecovered, greenrecovered, bluerecovered])
recoveredimage = PIL.Image.fromarray(colorimagedata, "RGB")
plt.imshow(recoveredimage)
plt.show()

