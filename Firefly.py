import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

import GravitionalObject as go


class Firefly(go.GravitationalObject):
    def __init__(self):
        super(Firefly, self).__init__()
        self._acc = QtCore.QPointF()
        self._vel = QtCore.QPointF()
        self._pos = QtCore.QPointF()
    #
    def init(self, pos):
        super(Firefly, self).init(pos)
        self._pos = self.pos()
    #
    def set_velocity(self, vel):
        self._vel = vel
    #
    def adjust_acceleration(self, acc):
        self._acc += acc
    #
    def update_pos(self, rc):
        oldpos = QtCore.QPointF(self._pos)
        self._vel += self._acc
        if (self._pos.x() < rc.left()):
            self._vel.setX(abs(self._vel.x()))
        elif (self._pos.x() > rc.right()):
            self._vel.setX(-abs(self._vel.x()))
        if (self._pos.y() < rc.top()):
            self._vel.setY(abs(self._vel.y()))
        elif (self._pos.y() > rc.bottom()):
            self._vel.setY(-abs(self._vel.y()))
        self._pos += self._vel
        self.setPos(self._pos)
        self._acc.setX(0)
        self._acc.setY(0)
        #self.scene().addLine(oldpos.x(), oldpos.y(), self._pos.x(), self._pos.y(), QtGui.QPen(QtCore.Qt.gray))
    #
    def setup_paint(self, status):
        self.setBrush(QtCore.Qt.yellow)
        self.setPen(QtGui.QPen(QtCore.Qt.green))
    #
    def acceleration_between(self, other):
        self.change_status(other)
        gap = other.scenePos() - self.scenePos();
        dist2 = gap.x()*gap.x() + gap.y()*gap.y();
        if self.status == go.Status.ACTIVE:
            acc = -go.GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap)
        elif (self.status == go.Status.ACTIVE2):
            acc = 2*go.GravitationalObject.s_grav_constant/dist2
            return QtCore.QPointF(acc*gap);
        else:
            return QtCore.QPointF();
    #
    def ball_radius(self):
        return 10
    def outer_radius(self):
        return 10
    def inner_radius(self):
        return 2

