# helper class for mouse interaction
# 
# Copyright (C) 2007  "Peter Roesch" <Peter.Roesch@fh-augsburg.de>
#
# This code is licensed under the PyOpenGL License.
# Details are given in the file license.txt included in this distribution.

import sys
import math

from final.test.interactionMatrix.interactionMatrix import InteractionMatrix

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print(''' Error: PyOpenGL not installed properly !!''')
    sys.exit()


class MouseInteractor(object):
    """Connection between mouse motion and transformation matrix"""

    def __init__(self, translationScale=0.1, rotationScale=.2):
        self.scalingFactorRotation = rotationScale
        self.scalingFactorTranslation = translationScale
        self.rotationMatrix = InteractionMatrix()
        self.translationMatrix = InteractionMatrix()
        self.mouseButtonPressed = None
        self.oldMousePos = [0, 0]
        self.wheelDirection = 0

    def mouseButton(self, button, mode, x, y):
        """Callback function for mouse button."""
        if mode == GLUT_DOWN:
            self.mouseButtonPressed = button
        else:
            self.mouseButtonPressed = None
        self.oldMousePos[0], self.oldMousePos[1] = x, y
        glutPostRedisplay()

    def mouseMotion(self, x, y):
        """Callback function for mouse motion.
        Depending on the button pressed, the displacement of the
        mouse pointer is either converted into a translation vector
        or a rotation matrix."""

        deltaX = x - self.oldMousePos[0]
        deltaY = y - self.oldMousePos[1]
        if self.mouseButtonPressed == GLUT_MIDDLE_BUTTON:
            tZ = deltaY * self.scalingFactorTranslation
            self.translationMatrix.addTranslation(tZ, tZ, tZ)
        elif self.mouseButtonPressed == GLUT_RIGHT_BUTTON:
            rY = deltaX * self.scalingFactorRotation * 0.5
            self.rotationMatrix.addRotation(rY, 0, 0, 1)
            rX = deltaY * self.scalingFactorRotation * 0.5
            self.rotationMatrix.addRotation(rX, -1, 1, 0)
        elif self.mouseButtonPressed == GLUT_LEFT_BUTTON:
            pass
        self.oldMousePos[0], self.oldMousePos[1] = x, y
        glutPostRedisplay()

    def mouseWheel(self, wheel, direction, x, y):
        if self.mouseButtonPressed == GLUT_LEFT_BUTTON:
            self.wheelDirection = direction
        glutPostRedisplay()

    def applyTransformation(self):
        """Concatenation of the current translation and rotation
        matrices with the current OpenGL transformation matrix"""

        glMultMatrixf(self.translationMatrix.getCurrentMatrix())
        glMultMatrixf(self.rotationMatrix.getCurrentMatrix())

    def registerCallbacks(self):
        """Initialise glut callback functions."""
        glutMouseFunc(self.mouseButton)
        glutMotionFunc(self.mouseMotion)
        glutMouseWheelFunc(self.mouseWheel)
