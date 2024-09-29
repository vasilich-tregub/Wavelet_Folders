# Wavelet_Folders
This repository is a series of projects to help me (and hopefully other people) understand the internals of modern video codecs.

The first project in the series is based off Tim Cogan's blog post LeGall-Tabatabai wavelet transform (https://tim.cogan.dev/lgt-wavelet/).

I took the liberty of making minor corrections to the code published in this post. The factor 2 in expressions for x\_evens, x\_odds is required to save the brightness of recovered images.
Without this correction, the brightness degrades for levels > 2.
