from processing import *

import argparse

def cli():
    parser = argparse.ArgumentParser(prog='midas')
    subparsers = parser.add_subparsers(
        title='These are the currently available MIDAS commands',
        metavar='<command>')
    tfft_parser= subparsers.add_parser(
        'tfft',
        help='Convert audio file(s) to temporal FFT (tFFT) bitstream files')
    tfft_parser.add_argument('inpath', metavar='SOURCE', type=str)
    tfft_parser.add_argument('outpath', metavar='DEST', type=str)
    tfft_parser.set_defaults(func=tfft)
    args = parser.parse_args()
    args.func(args)
