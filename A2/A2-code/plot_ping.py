'''
Plot ping RTTs over time
'''
import os, sys
from helper import *
import plot_defaults

from matplotlib.ticker import MaxNLocator
from pylab import figure

parser = argparse.ArgumentParser()
parser.add_argument('--files', '-f',
                    help="Ping output files to plot",
                    required=True,
                    action="store",
                    nargs='+')

parser.add_argument('--freq',
                    help="Frequency of pings (per second)",
                    type=int,
                    default=10)  # 10 times every second

parser.add_argument('--out', '-o',
                    help="Output png file for the plot.",
                    default=None) # Will show the plot

parser.add_argument('--download_file', '-d',
                    help="Download times file to plot.",
                    required=True)

parser.add_argument('--download_out', '-do',
                    help="Output png file for the download times plot.",
                    default=None)  # Will show the plot


################## functions for ping file ####################

args = parser.parse_args()

def parse_ping(fname):
    ret = []
    lines = open(fname).readlines()
    num = 0
    for line in lines:
        if 'bytes from' not in line:
            continue
        try:
            rtt = line.split(' ')[-2]
            rtt = rtt.split('=')[1]
            rtt = float(rtt)
            ret.append([num, rtt])
            num += 1
        except:
            break
    return ret

def plot_ping_data():

   # The complete implementation on my private repo
