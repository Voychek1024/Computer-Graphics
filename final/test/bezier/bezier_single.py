import math
import sys
import random
from time import sleep
import numpy as np

from final.test.interactionMatrix.mouseInteractor import MouseInteractor

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# animationAngle = 0.0
# frameRate = 60
# animationTime = 0
#
#
# def animationStep():
#     """Update animated parameters.
#     This Function is made active by glutSetIdleFunc"""
#     global animationAngle
#     global frameRate
#     global animationTime
#     animationAngle += 0.3
#     animationTime += 0.1
#     while animationAngle > 360:
#         animationAngle -= 360
#     sleep(1 / float(frameRate))
#     glutPostRedisplay()
#
#
# sigma = 0.5
# twoSigSq = 2. * sigma * sigma
#
#
# def dampedOscillation(u, v, t):
#     """Calculation of a R2 -> R1 function at position u,v at time t.
#     A t-dependent cosine function is multiplied with a 2D gaussian.
#     Both functions depend on the distance of (u,v) to the origin."""
#
#     distSq = u * u + v * v
#     dist = math.pi * 4 * math.sqrt(distSq)
#     global twoSigSq
#     return 0.5 * math.exp(-distSq / twoSigSq) * math.cos(dist - t)


# number of patches in x and y direction
# xMin, xMax, yMin, yMax = -1.0, 1.0, -1.0, 1.0
# xStep = (xMax - xMin) / (nPts - 1)
# yStep = (yMax - yMin) / (nPts - 1)
# initialise a list representing a regular 2D grid of control points.
# controlPoints = []
# The actual surface is divided into patches of 4 by 4 control points
# patch = []
# controlPoints = [[[yMin + y * yStep, xMin + x * xStep, 0.0] for x in range(nPts)] for y in range(nPts)]
# patch = [[[] for x in range(nPts)] for y in range(nPts)]


def generate_control(_nPts: int):
    _xMin, _xMax, _yMin, _yMax = -1.0, 1.0, -1.0, 1.0
    _xStep = (_xMax - _xMin) / (_nPts - 1)
    _yStep = (_yMax - _yMin) / (_nPts - 1)
    _control = [[[_yMin + y * _yStep, _xMin + x * _xStep, 0.0] for x in range(_nPts)] for y in range(_nPts)]
    _patch = [[[] for x in range(_nPts)] for y in range(_nPts)]
    return _control, _patch


nPts = 3
controlPoints, patch = generate_control(nPts)
print(controlPoints, patch)
projectionPoints = []
light_gl = False


def updateControlPoints():
    """Calculate function values for all 2D grid points."""

    for row in controlPoints:
        for coord in row:
            coord[2] = random.random()
    print(controlPoints)


run_once = True


def casteljau_curve(points, t):
    """Use casteljau to compute a point of a Bezier curve given the control
       points and a fixed parametized t"""
    p, n = points, len(points)
    for r in range(1, n):
        for i in range(n - r):
            p[i] = (1 - t) * p[i] + t * p[i + 1]

    return p[0]


def casteljau_surface(points, u, v):
    """Given control points of a surface and fixing u and v, compute an
       interpolated 3d point of the surface"""
    xis = list()
    yis = list()
    zis = list()

    for ps in points:
        xis.append(casteljau_curve([j[0] for j in ps], u))
        yis.append(casteljau_curve([j[1] for j in ps], u))
        zis.append(casteljau_curve([j[2] for j in ps], u))

    return (casteljau_curve(xis, v), casteljau_curve(yis, v),
            casteljau_curve(zis, v))


def show_axis():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -15.0, 0.0)
    glVertex3f(0.0, 15.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()


def display_control():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    for row in controlPoints:
        for coord in row:
            glVertex3f(float(coord[0]), float(coord[1]), float(coord[2]))
    glEnd()
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    for row in controlPoints:
        for i in range(0, nPts - 1):
            glVertex3f(float(row[i][0]), float(row[i][1]), float(row[i][2]))
            glVertex3f(float(row[i + 1][0]), float(row[i + 1][1]), float(row[i + 1][2]))
    glEnd()
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    for j in range(0, nPts):
        for i in range(0, nPts - 1):
            glVertex3f(float(controlPoints[i][j][0]), float(controlPoints[i][j][1]), float(controlPoints[i][j][2]))
            glVertex3f(float(controlPoints[i + 1][j][0]), float(controlPoints[i + 1][j][1]),
                       float(controlPoints[i + 1][j][2]))
    glEnd()


def display_surface():
    position = [0.0, 0.0, 1.0, 1.0]
    if light_gl:
        print("GL")
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glPushMatrix()
        glRotated(spin, spin, 1, 0.0)
        glLightfv(GL_LIGHT0, GL_POSITION, position)
        glDisable(GL_LIGHTING)
        glColor3f(0.0, 1.0, 1.0)
        glutWireCube(0.1)
        glPopMatrix()
        glEnable(GL_LIGHTING)

    cp = controlPoints
    xas = list()
    yas = list()
    zas = list()

    interval = 16
    for u in np.linspace(0.0, 1.0, interval):
        for v in np.linspace(0.0, 1.0, interval):
            p = casteljau_surface(cp, u, v)
            xas.append(p[0])
            yas.append(p[1])
            zas.append(p[2])

    # Draw the two aproximated surfaces
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(0, len(xas)):
        if (i + 1) % interval == 0:
            continue
        try:
            # OpenGL 3d Line
            glVertex3f(float(xas[i]), float(yas[i]), float(zas[i]))
            glVertex3f(float(xas[i + 1]), float(yas[i + 1]), float(zas[i + 1]))
        except IndexError:
            continue
    glEnd()

    for j in range(0, len(xas)):
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        for k in range(j, interval * interval, interval):
            try:
                # OpenGL 3d Line
                glVertex3f(float(xas[k]), float(yas[k]), float(zas[k]))
                glVertex3f(float(xas[k + interval]), float(yas[k + interval]), float(zas[k + interval]))
            except IndexError:
                continue
        glEnd()

    glBegin(GL_QUADS)
    for j in range(len(xas)):
        if (j + 1) % interval == 0:
            continue
        try:
            glColor3f(np.linspace(1.0, 0.0, len(xas))[j], np.linspace(0.5, 0.5, len(xas))[j],
                      np.linspace(0.0, 1.0, len(xas))[j])
            glVertex3f(xas[j], yas[j], zas[j])
            glVertex3f(xas[j + 1], yas[j + 1], zas[j + 1])
            glVertex3f(xas[j + interval + 1], yas[j + interval + 1], zas[j + interval + 1])
            glVertex3f(xas[j + interval], yas[j + interval], zas[j + interval])
        except IndexError:
            continue
    glEnd()


spin = 0.0
index_i, index_j = 0, 0


def drag_control(i: int, j: int, mouse):
    if mouse.mouseButtonPressed == GLUT_LEFT_BUTTON:
        glPointSize(25)
        glBegin(GL_POINTS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(controlPoints[i][j][0], controlPoints[i][j][1], controlPoints[i][j][2])
        glEnd()
        glPushMatrix()
        controlPoints[i][j][2] += mouse.wheelDirection * 0.1
        mouse.wheelDirection = 0
        # gluProject()
        """
        print(mouse.oldMousePos)
        print(glGetFloatv(GL_PROJECTION_MATRIX))
        print(glGetFloatv(GL_MODELVIEW_MATRIX))
        print(glGetIntegerv(GL_VIEWPORT))
        """
        glPopMatrix()
    elif mouse.mouseButtonPressed == GLUT_MIDDLE_BUTTON:
        pass


def keyboard(key, x, y):
    global index_i, index_j
    global spin, light_gl
    if key == b'q':
        light_gl = True
        glutPostRedisplay()
        spin += 5.0
        if spin == 360.0:
            spin = 0.0

    elif key == b'e':
        light_gl = False
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glutPostRedisplay()

    elif key == b'k':
        if index_i - 1 >= 0:
            index_i -= 1
        else:
            index_i = nPts - 1
        glutPostRedisplay()

    elif key == b'l':
        if index_j + 1 < nPts:
            index_j += 1
        else:
            index_j = 0
        glutPostRedisplay()

    elif key == b'r':
        print("draw initiated")


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    """OpenGL display function."""
    global controlPoints, patch
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    gluLookAt(3, 3, 3,  # eye position
              0, 0, 0,  # aim position
              0, 0, 1)  # up direction

    global mouseInteractor
    mouseInteractor.applyTransformation()
    global run_once
    show_axis()
    if run_once:
        updateControlPoints()
        run_once = False
    display_control()
    display_surface()
    global index_i, index_j
    drag_control(index_i, index_j, mouseInteractor)
    glPopMatrix()
    global nPts
    glutSwapBuffers()


def init():
    """Glut init function."""
    glClearColor(0, 0, 0, 1)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MAP2_VERTEX_3)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_POINT_SMOOTH)
    global mouseInteractor
    mouseInteractor = MouseInteractor(.01, 1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow(sys.argv[0])
init()
mouseInteractor.registerCallbacks()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
# glutIdleFunc(animationStep)
glutMainLoop()
