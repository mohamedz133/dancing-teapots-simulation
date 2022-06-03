import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

init_position_x=.1
init_position_y=.1
init_position_z=.1
position_ang=[0,15,30,45,60]
Width=200
Height=220
Rot_Step=20

def Dancing_of_teapots():
    global position_ang
    global init_position_x
    global init_position_y
    global init_position_z
    global Rot_Step

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor(1,1,1)
    glTranslate(0, -3, -5)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(4, 1, 360, 1)


    glRotate(-90, 1, 0, 0)
    glPushMatrix()
    ##################################### TEAPOT WITH CYLINDER (1)
    glColor3d(1, 0, 1)
    glPushMatrix()
    x = 3.2 * math.cos(position_ang[0])
    Z = 3.2 * math.sin(position_ang[0])

    glTranslate(x, 0,Z )
    glTranslate(0, 1, 0)
    glRotate(Rot_Step,0,1,0)

    glutWireTeapot(.45)

    glRotate(90,1,0,0)
    glutSolidCylinder(.03, 1.5, 360, 1)


    glPopMatrix()
    ##################################### TEAPOT WITH CYLINDER (2)

    glPushMatrix()
    x =3.2* math.cos(position_ang[1])
    Z= 3.2 * math.sin(position_ang[1])
    glTranslate(x, 0,Z )
    glTranslate(0, 1, 0)
    glRotate(Rot_Step, 0, 1, 0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, 1.5, 360, 1)
    glPopMatrix()
    ##################################### TEAPOT WITH CYLINDER (3)


    glPushMatrix()
    x = 3.2 * math.cos(position_ang[2])
    Z = 3.2 * math.sin(position_ang[2])
    glTranslate(x, 0,Z )
    glTranslate(0, 1, 0)
    glRotate(Rot_Step, 0, 1, 0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, 1.5, 360, 1)
    glPopMatrix()
    ##################################### TEAPOT WITH CYLINDER (4)

    glPushMatrix()
    x = 3.2 * math.cos(position_ang[3])
    Z = 3.2 * math.sin(position_ang[3])
    glTranslate(x, 0,Z )
    glTranslate(0, 1, 0)
    glRotate(Rot_Step, 0, 1, 0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, 1.5, 360, 1)
    glPopMatrix()
    ##################################### TEAPOT WITH CYLINDER (5)

    glPushMatrix()
    x = 3.2 * math.cos(position_ang[4])
    Z = 3.2 * math.sin(position_ang[4])
    glTranslate(x, 0, Z)
    glTranslate(0, 1, 0)
    glRotate(Rot_Step, 0, 1, 0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, 1.5, 360, 1)

    ##################################### TEAPOTS AND CYLINDERS    TRANSFORMATIONS


    glRotate(Rot_Step, 1, 0, 0)
    glPopMatrix()

    glPopMatrix()

    Rot_Step+=1
    for i in range (0,5):
        #position_ang[i]+=.007      #  when using glut timer function

        position_ang[i] += .004     # when using idle function

    if(position_ang==360):
        position_ang=0



def draw ():
    global angle

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width) / float(Height), 1, 20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 1, 6, 0, 0, 0, 0, 1, 0)

    Dancing_of_teapots()
    glutSwapBuffers()

def game_timer(v):                ###########   optional to use or idle function
    draw()
    glutTimerFunc(3, game_timer, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(250, 50)
    glutCreateWindow(b"practical assign .* dansing pots *  ")
    glutDisplayFunc(draw)
    glEnable(GL_DEPTH_TEST)
    glutIdleFunc(draw)
    #glutTimerFunc(1000, game_timer, 1)     # try this with line 106
    glutMainLoop()

if __name__ == "__main__":
    main()