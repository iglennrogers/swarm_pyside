#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QWidget>

#public:
#    QAction *actionQuit
#    QWidget *centralWidget
#    QGraphicsView *graphicsView
#    QMenuBar *menuBar
#    QMenu *menuSwarm
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

Qt = QtCore.Qt


class Ui_MainWindow:
    def __init__(self):
        pass
    def setupUi(self, main_window):
        if main_window.objectName() == "":
            main_window.setObjectName("MainWindow")
        main_window.setWindowModality(Qt.WindowModal)
        main_window.resize(810, 630)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        
        self.actionQuit = QtGui.QAction(main_window)
        self.actionQuit.setObjectName("actionQuit")
        centralWidget = QtGui.QWidget(main_window)
        centralWidget.setObjectName("centralWidget")
        
        self.graphicsView = QtGui.QGraphicsView(centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(QtCore.QRect(5, 5, 800, 600))
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMaximumSize(QtCore.QSize(800, 600))
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_window.setCentralWidget(centralWidget)
        
        menuBar = QtGui.QMenuBar(main_window)
        menuBar.setObjectName("menuBar")
        menuBar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menuSwarm = QtGui.QMenu(menuBar)
        self.menuSwarm.setObjectName("menuSwarm")
        main_window.setMenuBar(menuBar)

        menuBar.addAction(self.menuSwarm.menuAction())
        self.menuSwarm.addAction(self.actionQuit)

        self.retranslateUi(main_window)

        self.menuSwarm.triggered.connect(main_window.on_actionQuitTriggered)
        #
    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow"))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit"))
        self.menuSwarm.setTitle(QtGui.QApplication.translate("MainWindow", "Swarm"))
