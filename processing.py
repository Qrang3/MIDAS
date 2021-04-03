import os
import numpy as np
import wave

import matplotlib.pyplot as plt

def file_tfft(inpath, outpath):
    ifile = wave.open(inpath)
    samples = ifile.getnframes()
    audio = ifile.readframes(samples)
    print(ifile.getparams())
    npaudio = np.frombuffer(audio, dtype=np.int16)

    # save .wav plot
    x = np.arange(npaudio.size)
    plt.plot(x, npaudio)
    plt.savefig(outpath+"_wavplot.png")

    ifile.close()

def tfft(args):
    #if os.path.isdir(args.inpath):
    #    for filename in os.listdir(args.inpath):
    #        file_tfft
    #else:
    #    ins = [read(args.inpath)]
    file_tfft(args.inpath, args.outpath)
