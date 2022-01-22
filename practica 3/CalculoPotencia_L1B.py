#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: CalculoPotencia_L1B
# Author: Edwar_Camargo_Andres_Tarazona
# Copyright: Edwar_Camargo_Andres_Tarazona
# GNU Radio version: v3.8.3.1-16-g9d94c8a6

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from CalculoPotencia_L1B import CalculoPotencia_L1B  # grc-generated hier_block
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class CalculoPotencia_L1B(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "CalculoPotencia_L1B")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("CalculoPotencia_L1B")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "CalculoPotencia_L1B")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.A = A = 1

        ##################################################
        # Blocks
        ##################################################
        self._A_range = Range(0, 10, 1, 1, 200)
        self._A_win = RangeWidget(self._A_range, self.set_A, 'Amplitud', "counter_slider", float)
        self.top_layout.addWidget(self._A_win)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1000, A, 0, 0)
        self.CalculoPotencia_L1B_0 = CalculoPotencia_L1B(
            l_vect=1024,
        )

        self.top_layout.addWidget(self.CalculoPotencia_L1B_0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.CalculoPotencia_L1B_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "CalculoPotencia_L1B")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.analog_sig_source_x_0.set_amplitude(self.A)





def main(top_block_cls=CalculoPotencia_L1B, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
