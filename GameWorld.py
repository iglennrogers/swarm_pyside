import random

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

import GravitionalObject as go
import Firefly

QGraphicsScene = QtGui.QGraphicsScene
QPen = QtGui.QPen
Qt = QtCore.Qt


def rand_pos():
    x = random.randint(1, 15)*50
    y = random.randint(1, 11)*50
    return QtCore.QPointF(x, y)


def is_gravital(obj):
    return isinstance(obj, go.GravitationalObject)


class GameWorld(QGraphicsScene):
    def __init__(self):
        super(GameWorld, self).__init__()
    #
    def init_backdrop(self):
        for i in range(0, 801, 50):
            self.addLine(i, 0, i, 600, QPen(Qt.gray))
        for j in range(0, 601, 50):
            self.addLine(0, j, 800, j, QPen(Qt.gray))
    #
    def init(self):
        self.init_backdrop()
        #
        for _ in range(10):
            x = random.randint(1, 16)*50
            y = random.randint(1, 12)*50
            ff = Firefly.Firefly()
            ff.init(QtCore.QPointF(x, y))
            ff.set_velocity(QtCore.QPointF(random.randint(0, 10) - 5, random.randint(0, 10) - 5))
            self.addItem(ff)
        #
        self.setSceneRect(0, 0, 800, 600)
    #
    def advance(self):
        rc = QtCore.QRectF(self.sceneRect())
        for ff in filter(is_gravital, self.items()):
            for other in filter(is_gravital, self.items()):
                if other != ff:
                    acc = other.acceleration_between(ff)
                    ff.adjust_acceleration(acc)
            ff.update_pos(rc)
        return True
