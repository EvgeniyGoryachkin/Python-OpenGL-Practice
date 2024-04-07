import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

def func():
    global xrot         
    global yrot            
    global lightpos     

    xrot = 100.0                          
    yrot = 66.0                          
    zrot = -50.0                          

    glClearColor(0.25, 0.56, 0.5, 0.95)           
    lightpos = (-90.0, 10.0, 100.0)        

    glEnable(GL_LIGHTING)                         
    glEnable(GL_LIGHT0)                 
    glClearDepth ( 1.0 )                
    glDepthFunc ( GL_LEQUAL )          
    glEnable ( GL_DEPTH_TEST )            
    quadric = None 
    greencolor = (1.0, 0.36, 0.0, 0.7) 
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                
    glPushMatrix()
    
    glRotatef(xrot, 1.0, 1.0, 0.0) # Наша камера                           
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)
    
def Human():
    #Голова
    quadric=gluNewQuadric(); 
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    glTexCoord1f (1)
    glTranslatef(0.2,0.0,-0.2)
    gluSphere(quadric,0.12,100,100)
    #Тело
    Cylinder (0.03,0.5)
    #Ноги
    glTranslatef(0.0,0.0, 0.5)
    glRotatef(40, 1.0, 0.0, 0.0)
    Cylinder(0.02,0.40)
    glRotatef(-60, 1.0, 0.0, 0.0)
    Cylinder(0.02,0.40)
    #Руки
    glTranslatef(0.0,0.1,-0.3)
    glRotatef(135, 1.0, 0.0, 0.0)
    Cylinder(0.01,0.30)
    glRotatef(135, 1.0, 0.0, 0.0)
    Cylinder(0.01,0.30)
  
def image():
    image = pygame.image.load('human.jpeg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)    

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
        glTexCoord3f (math.cos((a+b)/2), math.sin((a+b)/2), 0.0 )
        glNormal3f(math.cos((a+b)/2), math.sin((a+b)/2), 0.0 )
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,height)
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,height)
        a=b
        glEnd()
    glNormal3f(0,0,1)
    Circle((0,0,0),radius)
    glNormal3f(0,0,-1)
    Circle((0,0,height),radius)
    glColor(0.5, 0.25, 0.25, 1.0)
    return

pygame.init()
display = (700, 700)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    glRotatef(0, 0, 0, 0)  
    func()
    image()
    Human()
    clock.tick(1)
    pygame.display.flip()

