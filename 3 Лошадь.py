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


def draw_horse(texture_id):
    
    glBindTexture(GL_TEXTURE_2D, texture_id)
    #Тело
    glPushMatrix()
    glTranslatef(-1.1, 1, 0.90) # 
    glRotatef(90, 1, 20, 0)
    glTexCoord3f(0, 1, 0)
    gluCylinder(gluNewQuadric(), 0.2, 0.2, 1.5, 10, 10)  
    glPopMatrix()

    #Задние ноги
    #Первая нога
    glPushMatrix()
    glTranslatef(-0.9, 0.9, 1) 
    glRotatef(80, 1, 0, 0)
    glTexCoord3f(0, 1, 1)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.7, 20, 20)  
    # радиус первого конца, радиус второго конца, длина 
    glPopMatrix()

    #Вторая нога
    glPushMatrix()
    glTranslatef(-0.9, 0.9, 0.9) 
    glRotatef(110, 1, 0, 0)
    glTexCoord3f(1, 1, 0)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.7, 20, 20)  
    # радиус первого конца, радиус второго конца, длина 
    glPopMatrix()

    #Передние ноги
    # Первая нога
    glPushMatrix()
    glTranslatef(0.2, 0.8, 0.9) 
    glRotatef(110, 1, 0, 0)
    glTexCoord3f(0, 1, 0)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.7, 20, 20)  
    # радиус первого конца, радиус второго конца, длина 
    glPopMatrix()

    # Вторая нога
    glPushMatrix()
    glTranslatef(0.2, 0.8, 0.9) 
    glRotatef(80, 1, 0, 0)
    glTexCoord3f(0, 1, 0)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.7, 20, 20)  
    # радиус первого конца, радиус второго конца, длина 
    glPopMatrix()

    #Голова
    glPushMatrix()
    glTranslatef(0.6, 0.9, 0.9) 
    glRotatef(80, 1, 0, 0)
    glTexCoord3f(0, 1, 0)
    gluSphere(gluNewQuadric(), 0.3, 10, 10 )  
    glPopMatrix()

    # Хвост
    glPushMatrix()
    glTranslatef(-1.5, 1.2, 0.9) # 
    glRotatef(90, 1, 3, 0)
    glTexCoord3f(0, 1, 0)
    gluCylinder(gluNewQuadric(), 0.05, 0.05, 0.7, 10, 10)  
    glPopMatrix()


def display(texture_id):
    glClearColor(0.7, 0.9, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    draw_horse(texture_id)
    glDisable(GL_TEXTURE_2D)
    pygame.display.flip()

def main():
    pygame.init()
    window_size = (800, 600)
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

    gluPerspective(35, (window_size[0]/window_size[1]), 0.1, 50.0)
    glTranslatef(0.0, -0.30, -7)

    texture_id = load_texture('horse.jpg') 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        display(texture_id)
        pygame.time.wait(10)


main()