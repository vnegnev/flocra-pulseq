#!/usr/bin/env python3
#
# Tests for flocra-pulseq interpreter; similar style to test_flocra_model.py


import external
from test_base import *

class FPTest(unittest.TestCase):
    """Tests out the various flocra-pulseq test .seq files, and compares
    the results to reference CSVs."""

    @classmethod
    def setUpClass(cls):
        # TODO make this check for a file first
        os.system("make -j4 -s -C " + os.path.join(flocra_sim_path, "build"))
        os.system("fallocate -l 516KiB /tmp/marcos_server_mem")
        os.system("killall flocra_sim") # in case other instances were started earlier

        warnings.simplefilter("ignore", fc.FloServerWarning)
        # warnings.simplefilter("ignore", fc.FloRemovedInstructionWarning)

    def setUp(self):
        # start simulation
        if flocra_sim_fst_dump:
            self.p = subprocess.Popen([os.path.join(flocra_sim_path, "build", "flocra_sim"), "both", flocra_sim_csv, flocra_sim_fst],
                                      stdout=subprocess.DEVNULL,
                                      stderr=subprocess.STDOUT)
        else:
            self.p = subprocess.Popen([os.path.join(flocra_sim_path, "build", "flocra_sim"), "csv", flocra_sim_csv],
                                      stdout=subprocess.DEVNULL,
                                      stderr=subprocess.STDOUT)


        # open socket
        time.sleep(0.05) # give flocra_sim time to start up

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip_address, port)) # only connect to local simulator
        self.packet_idx = 0

    def tearDown(self):
        # self.p.terminate() # if not already terminated
        # self.p.kill() # if not already terminated
        self.s.close()

        if flocra_sim_fst_dump:
            # open GTKWave
            os.system("gtkwave " + flocra_sim_fst + " " + os.path.join(flocra_sim_path, "src", "flocra_sim.sav"))

    def test1(self):
        
