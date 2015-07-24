import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

import Ui_MainWindow
import GameWorld


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        scene = GameWorld.GameWorld()
        scene.init()
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.show()
        self.timer = self.startTimer(50)
    #
    def timerEvent(self, event):
        scene = self.ui.graphicsView.scene()
        if not scene.advance():
            self.killTimer(self.timer)
    #
    def closeEvent(self, event):
        self.killTimer(self.timer)
        event.accept()
    #
    @QtCore.Slot()
    def on_actionQuitTriggered(self):
        self.killTimer(self.timer)
        self.close()
