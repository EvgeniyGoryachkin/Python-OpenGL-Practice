from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
import math
import sys

def func():   
    xrot = 100.0                          
    yrot = -66.0                          
    zrot = -30.0                          

    glClearColor(0.2, 0.1, 1.0, 0.0)                
    lightpos = (150.0, 90.0, -20.0)                   
    
    glEnable(GL_LIGHTING)                           
    glEnable(GL_LIGHT0)                             
    glClearDepth ( 1.0 )                            
    glDepthFunc ( GL_LEQUAL )                       
    glEnable ( GL_DEPTH_TEST )                      
    quadric = None
    greencolor = (0.0, 0.0, 0.0, 0.0) 
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) 

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                

    glPushMatrix()                                              

    glRotatef(xrot, 1.0, 1.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)
    
def Snowman():
    quadric=gluNewQuadric(); 
    gluQuadricNormals(quadric, GLU_SMOOTH); 
    gluQuadricTexture(quadric, GL_TRUE); 
    glTexCoord1f (1)
    glTranslatef(-0.5,0.0,0.0)
    gluSphere(quadric,0.300,200,200)
    glTranslatef(0.4,0.0,0.0)
    gluSphere(quadric,0.200,200,200)
    glTranslatef(0.3,0.0,0.0)
    gluSphere(quadric,0.150,200,200)
    glTranslatef(0.03,0.08,0.1)
    gluSphere(quadric,0.04,200,200)
    glTranslatef(0.0,-0.17,0.0)
    gluSphere(quadric,0.04,200,200)
    glTranslatef(0.0,0.09,0.0)
    nose = (1.0, 0.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, nose)
    Cylinder(0.03,0.15)
    return

def Circle(center,radius):
    nvert=50 
    pi=3.1415
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center[0],center[1],center[2]) 
    for i in range (0,nvert+1):
        a = i/nvert*pi*2.0
        glVertex3f(math.cos(a)*radius+center[0],math.sin(a)*radius+center[1],center[2])
    glEnd()
    return

def Cylinder(radius,height):
    nvert=100
    pi=3.1415
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    a = 0
    for i in range (1,nvert+1):
        glBegin(GL_POLYGON)
        b = i/nvert*pi*2.0
        glNormal3f(math.cos((a+b)/2), math.sin((a+b)/2), 0.0 )
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,height)
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,height)
        a=b
        glEnd()
    glNormal3f(0,0,-1)
    Circle((0,0,0),radius)
    glNormal3f(0,0,1)
    Circle((0,0,height),radius)
    glColor(0.8, 0.0, 0.0, 0.0)
    return
def image():
    image = pygame.image.load('snowman.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)    
pygame.init()
resolution = (700,700)
pygame.display.set_mode(resolution,DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotatef(1, 0, 1, 0)  
    func()
    image()
    Snowman()
    clock.tick(1)
    pygame.display.flip()
