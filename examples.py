#!/usr/bin/env python3
# Examples of flocra-pulseq usage

import external
import numpy as np
import matplotlib.pyplot as plt

from local_config import fpga_clk_freq_MHz
import experiment as ex

from flocra_pulseq_interpreter import PSInterpreter

import pdb
st = pdb.set_trace

def test1_example():
    lo_freq = 2 # MHz
    grad_t = 10 # us
    psi = PSInterpreter(rf_center=lo_freq*1e6,
                        rf_amp_max=2500,
                        grad_t=grad_t,
                        grad_max=100) # very large, just for testing

    od, pd = psi.interpret("test_files/test4.seq")

    if True: # debugging
        plt.step(od['grad_vx'][0], od['grad_vx'][1], where='post')
        plt.figure()
        plt.step(od['tx0'][0], od['tx0'][1], where='post')
        plt.show()

    expt = ex.Experiment(lo_freq=lo_freq,
                         rx_t=pd['rx_t'],
                         init_gpa=False)

    expt.add_flodict(od)

    rxd, msgs = expt.run()
    expt.close_server(True)

if __name__ == "__main__":
    test1_example()
