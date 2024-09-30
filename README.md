# Wavelet_Folders
This repository is a series of projects to help me (and hopefully other people) understand the internals of modern video codecs.

The first project in the series is based off Tim Cogan's blog post LeGall-Tabatabai wavelet transform (https://tim.cogan.dev/lgt-wavelet/).

Besides adding the imports omitted in the blogpost and correcting typos of code excerpts' formatting/truncation, I took the liberty 
of making a minor correction to the code published in this post. The factor 2 in expressions for x\_evens, x\_odds is required 
to maintain the brightness level of recovered images as the decomposition levels parameter grows. Without this correction, the brightness 
degrades for levels > 2.

It may seem untimely to write/use a custom code for wavelet transforms at the times of the actively developing PyWavelet library 
(https://github.com/PyWavelets/pywt). For those inspiring to master the wavelet math, looking into the internals of library code certainly 
help; besides, IMO, PyWavelet library is still in its infancy or, should I say, is on its way to community recognition and therefore lacks 
the wide userforum base. For example, while the library promises the means to create a multilevel wavelet decomposition with 
a custom wavelet packet basis (https://pywavelets.readthedocs.io/en/latest/ref/2d-decompositions-overview.html#wavelet-packet-transform), 
like Le Gall 5/3 5 hor, 2 vert wavelet of JPEG XS, the resulting code using the library functions and utils may become as lengthy as 
the custom implementation without the PyWavelets library. 

The next project in this repository is planned to implement JPEG XS codec wavelet along the pattern of Tim Cogan's WaveletImage class as 
compared to the use of PyWavelets library. 
