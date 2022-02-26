# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Modulacion PAM5
# Author: EDWAR_ANDRES
# Copyright: EDWAR_ANDRES
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class Modulo_5(gr.hier_block2):
    def __init__(self, d=10, fs=100000, samp_rate=100000):
        gr.hier_block2.__init__(
            self, "Modulacion PAM5",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.d = d
        self.fs = fs
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 50-d)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fs, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0_0, 0))


    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.blocks_delay_0.set_dly(50-self.d)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.analog_sig_source_x_0.set_frequency(self.fs)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

