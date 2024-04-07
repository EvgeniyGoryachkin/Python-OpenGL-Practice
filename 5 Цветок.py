import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image

def load_texture(file):
    image = Image.open(file)
    image_bytes = image.tobytes('raw', 'RGB', 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_bytes)
    return texture_id


def draw_flower(texture_id):
    
    glBindTexture(GL_TEXTURE_2D, texture_id)
    quadric=gluNewQuadric(); 
    gluQuadricNormals(quadric, GLU_SMOOTH) 
    gluQuadricTexture(quadric, GL_TRUE)
    #Стебель
    glTexCoord1f (1)
    glPushMatrix()
    glTranslatef(-1.1, 0.5, 0.90) # 
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.05, 0.05, 1.0, 10, 10)  
    glPopMatrix()

    #Голова
    glPushMatrix()
    glTranslatef(-1.12, 0.5, 0.9) 
    glRotatef(80, 1, 0, 0)
    gluSphere(gluNewQuadric(), 0.15, 10, 10 )  
    glPopMatrix()

    #Лепестки
    #Первый лепесток
    glPushMatrix()
    glTranslatef(-0.9, 0.5, 0.9) 
    glRotatef(80, 1, 0, 0)
    gluSphere(gluNewQuadric(), 0.14, 10, 10 )  
    glPopMatrix()

    #Второй лепесток
    glPushMatrix()
    glTranslatef(-1.3, 0.5, 0.9) 
    glRotatef(80, 1, 0, 0)
    gluSphere(gluNewQuadric(), 0.14, 10, 10 )  
    glPopMatrix()

    #Третий лепесток
    glPushMatrix()
    glTranslatef(-1.12, 0.5, 1.1) 
    glRotatef(80, 1, 0, 0)
    gluSphere(gluNewQuadric(), 0.14, 10, 10 )  
    glPopMatrix()

    #Четвёртый лепесток
    glPushMatrix()
    glTranslatef(-1.12, 0.5, 0.7) 
    glRotatef(80, 1, 0, 0)
    gluSphere(gluNewQuadric(), 0.14, 10, 10 )  
    glPopMatrix()
    
    return

def display(texture_id):
    glClearColor(0.5, 0.65, 0.9, 1.0) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    draw_flower(texture_id)
    glDisable(GL_TEXTURE_2D)
    pygame.display.flip()

def main():
    pygame.init()
    window_size = (800, 600)
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

    gluPerspective(35, (window_size[0]/window_size[1]), 0.1, 50.0)
    glTranslatef(0.0, -0.0, -5)

    texture_id = load_texture('flower.jpg') 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        display(texture_id)
        pygame.time.wait(30)


main()