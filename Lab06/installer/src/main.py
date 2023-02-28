

import PyInstaller.__main__
import os
import sys

from PyQt5 import QtCore
from InstallerApp import InstallerApp
    


def main(*args, **kwargs):
	if(sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):

		app = InstallerApp()
		app.start()


if __name__ == '__main__':
    main()