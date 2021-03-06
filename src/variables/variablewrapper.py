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

from PyQt4.QtCore import QObject, SIGNAL
import filters


class VariableWrapper(QObject):
    """ Parent of all Variable-Wrapper-Classes """

    def __init__(self, variable):
        """ Constructor
        @param variable    variables.variable.Variable, Variable to wrap with the new DataGraphVW
        """
        QObject.__init__(self)
        self.variable = variable
        self.connect(self.variable, SIGNAL('changed()'), self.varChanged)
        self.connect(self.variable, SIGNAL('replace(PyQt_PyObject)'), self.varReplace)

        self.filter = filters.Empty

    def varChanged(self):
        self.emit(SIGNAL('changed()'))

    def varReplace(self, var):
        self.emit(SIGNAL('replace(PyQt_PyObject, PyQt_PyObject)'), self, var)

    def getExp(self):
        return self.variable.getExp()

    def getType(self):
        return self.variable.getType()

    def getUnfilteredValue(self):
        return self.variable.getValue()

    def getValue(self):
        return self.filter.toDisplay(self.getUnfilteredValue())

    def setValue(self, value):
        self.variable.setValue(value)

    def getInScope(self):
        return self.variable.getInScope()

    def getAccess(self):
        return self.variable.getAccess()

    def setFilter(self, f):
        self.filter = f

    def getFilter(self):
        return self.filter
