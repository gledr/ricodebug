# ricodebug - A GDB frontend which focuses on visually supported
# debugging using data structure graphs and SystemC features.
#
# Copyright (C) 2011  The ricodebug project team at the
# Upper Austrian University Of Applied Sciences Hagenberg,
# Department Embedded Systems Design
#
# This file is part of ricodebug.
#
# ricodebug is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# For further information see <http://syscdbg.hagenberg.servus.at/>.

from PyQt4.QtCore import QObject


class StlVectorParser(QObject):
    def __init__(self, distributedObjects):
        QObject.__init__(self)
        self.distributedObjects = distributedObjects
        self.signalProxy = distributedObjects.signalProxy

    def getSize(self, vector):
        size = None
        size_var = self.signalProxy.gdbEvaluateExpression("(" + vector + ").size()")

        if size_var is not None:
            size = int(size_var)

        return size

    def getContent(self, vector):
        size = self.getSize(vector)

        if size is None:
            return None

        content = []

        for i in range(0, size):
            res = self.signalProxy.gdbEvaluateExpression("(" + vector + ").begin()._M_current+" + str(i))
            if res is not None:
                content.append(res)

        return content
