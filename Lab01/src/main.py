import sys

from PyQt5 import QtCore, QtWidgets


from MainApp import MainApp



def main(*args, **kwargs):
	if(sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
		app = MainApp()
		app.start()




if __name__ == "__main__":
	main()