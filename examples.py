#!/usr/bin/env python3
# Examples of flocra-pulseq usage

import external
import numpy as np
import matplotlib.pyplot as plt

from local_config import fpga_clk_freq_MHz
import experiment as exp

from flocra_pulseq_interpreter import PSInterpreter

import pdb
st = pdb.set_trace

def test1_example():
    psi = PSInterpreter(rf_center=2e6,
                        grad_t = 10,
                        grad_max=1e11) # very large, just for testing

    od, pd = psi.interpret("test_files/test2.seq")

    st()


if __name__ == "__main__":
    test1_example()
