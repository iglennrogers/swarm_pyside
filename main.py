import PySide.QtGui as QtGui

import MainWindow


if __name__ == "__main__":
    try:
        app = QtGui.QApplication([])
    except RuntimeError:
        app = QtGui.QApplication.instance()
    mw = MainWindow.MainWindow()
    mw.show()
    app.exec_()
