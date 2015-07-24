import math
from enum import Enum

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class Status(Enum):
    UNKNOWN = 0
    ACTIVE =  1
    ACTIVE2 = 2
    INACTIVE = 3
    DISABLED = 4


class GravitationalObject(QtGui.QGraphicsEllipseItem):
    s_grav_constant = 10
    #
    def __init__(self):
        super(GravitationalObject, self).__init__()
        self.status = Status.UNKNOWN
    def init(self, pos):
        r = self.ball_radius()
        self.setPos(pos.x(), pos.y())
        self.setRect(-r, -r, 2*r, 2*r)
        self.setup_paint(Status.UNKNOWN)
        
    def setup_paint(self, status):
        pass
    def acceleration_between(self, other):
        pass
    def change_status(self, other):
        oldstatus = self.status
        gap = other.scenePos() - self.scenePos()
        dist2 = gap.x()*gap.x() + gap.y()*gap.y()
        band = math.sqrt(dist2)/self.ball_radius()
        if band <= self.inner_radius():
            self.status = Status.ACTIVE2
        elif band <= self.outer_radius():
            self.status = Status.ACTIVE
        else:
            self.status = Status.INACTIVE

        if self.status != oldstatus:
            self.setup_paint( self.status )
            self.update()

    def ball_radius(self):
        pass
    def outer_radius(self):
        pass
    def inner_radius(self):
        return self.outer_radius()


class RepulsorBlock(GravitationalObject):
    def __init__(self):
        super(RepulsorBlock, self).__init__()
    def setup_paint(self, status):
        if status in [Status.ACTIVE, Status.ACTIVE2]:
            self.setBrush(QtCore.Qt.red)
            self.setPen(QtGui.QPen(QtCore.Qt.magenta))
        else:
            self.setBrush(QtCore.Qt.magenta)
            self.setPen(QtGui.QPen(QtCore.Qt.red))
    def ball_radius(self):
        return 15
    def outer_radius(self):
        return 5
    def inner_radius(self):
        return 1
    def acceleration_between(self, other):
        self.change_status(other)
        gap = other.scenePos() - self.scenePos();
        dist2 = gap.x()*gap.x() + gap.y()*gap.y();
        if self.status == Status.ACTIVE:
            acc = GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap)
        elif (self.status == Status.ACTIVE2):
            acc = GravitationalObject.s_grav_constant/(self.ball_radius()*self.ball_radius()*self.inner_radius()*self.inner_radius());
            return QtCore.QPointF(acc*gap);
        else:
            return QtCore.QPointF();


class AttractorBlock(GravitationalObject):
    def __init__(self):
        super(AttractorBlock, self).__init__()
    def setup_paint(self, status):
        if status in [Status.ACTIVE, Status.ACTIVE2]:
            self.setBrush(QtCore.Qt.cyan)
            self.setPen(QtGui.QPen(QtCore.Qt.green))
        else:
            self.setBrush(QtCore.Qt.green)
            self.setPen(QtGui.QPen(QtCore.Qt.cyan))
    def ball_radius(self):
        return 15
    def outer_radius(self):
        return 5
    def inner_radius(self):
        return 1
    def acceleration_between(self, other):
        self.change_status(other)
        gap = other.scenePos() - self.scenePos();
        dist2 = gap.x()*gap.x() + gap.y()*gap.y();
        if self.status == Status.ACTIVE:
            acc = -GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap)
        elif (self.status == Status.ACTIVE2):
            acc = -GravitationalObject.s_grav_constant/(self.ball_radius()*self.ball_radius()*self.inner_radius()*self.inner_radius());
            return QtCore.QPointF(acc*gap);
        else:
            return QtCore.QPointF();


class LightBlock(GravitationalObject):
    def __init__(self):
        super(LightBlock, self).__init__()
    def setup_paint(self, status):
        if status in [Status.ACTIVE, Status.ACTIVE2]:
            self.setBrush(QtCore.Qt.blue)
            self.setPen(QtGui.QPen(QtCore.Qt.cyan))
        else:
            self.setBrush(QtCore.Qt.cyan)
            self.setPen(QtGui.QPen(QtCore.Qt.blue))
    def ball_radius(self):
        return 15
    def outer_radius(self):
        return 5
    def inner_radius(self):
        return 2
    def acceleration_between(self, other):
        self.change_status(other)
        gap = other.scenePos() - self.scenePos();
        dist2 = gap.x()*gap.x() + gap.y()*gap.y();
        if self.status == Status.ACTIVE:
            acc = -GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap)
        elif (self.status == Status.ACTIVE2):
            acc = 2*GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap);
        else:
            return QtCore.QPointF();
