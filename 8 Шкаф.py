from PIL import Image
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def load_texture(file):
    image = Image.open(file)
    image_bytes = image.tobytes('raw', 'RGB', 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_bytes)
    return texture_id


def draw_func(texture_id):

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    
    #Передняя грань
    glTexCoord3f(-1, 2, 1 )
    glVertex3f(0, 2, 1)  # Слева вверху
    glTexCoord3f(1, 1, 1)
    glVertex3f( 1, 2, 1)  # Справа вверху
    glTexCoord3f(1, -1, 1)
    glVertex3f( 1, -1, 1)  # Справа внизу
    glTexCoord3f(0, -1, 1)
    glVertex3f(0,-1, 1)  # Слева внизу

    #Задняя грань
    glTexCoord3f(0, -1, -1)
    glVertex3f(0, -1, -1) #Лево низ
    glTexCoord3f(1, -1, -1)
    glVertex3f(1, -1, -1) #Право низ
    glTexCoord3f(1, 2, -1)
    glVertex3f(1, 2, -1)   #Право вверх
    glTexCoord3f(0, 2, -1)
    glVertex3f(0, 2, -1)   #Лево вверх
    
    #нижняя грань
    glTexCoord3f(0, -1, -1)
    glVertex3f(0, -1, -1) #Лево вверх
    glTexCoord3f(1, -1, -1) 
    glVertex3f(1, -1, -1) #Право вверх
    glTexCoord3f(1, -1, 1)
    glVertex3f(1, -1, 1)  #Правая нижняя
    glTexCoord3f(0, -1, 1)
    glVertex3f(0, -1, 1) #Левая нижняя

    # #верхяя грань
    glTexCoord3f(0, 2, -1)
    glVertex3f(0,2,-1) #Лево вверх
    glTexCoord3f(0, 2, 1) 
    glVertex3f(0,2,1) #Лево низ
    glTexCoord3f(1, 2, 1)
    glVertex3f(1,2,1)  #Правая нижняя
    glTexCoord3f(1, 2, -1)
    glVertex3f(1,2,-1) #Право вверх

    # # #правая грань
    glTexCoord3f(1, 2, 1)
    glVertex3f(1,2,1) #Лево вверх
    glTexCoord3f(1, -1, 1) 
    glVertex3f(1,-1,1) #Лево низ
    glTexCoord3f(1, -1, -1)
    glVertex3f(1,-1,-1)  #Правая нижняя
    glTexCoord3f(1, 2, -1)
    glVertex3f(1,2,-1) #Право вверх

    # #левая грань
    glTexCoord3f(0, 2, -1)
    glVertex3f(0,2,-1) #Лево вверх
    glTexCoord3f(0, -1, -1) 
    glVertex3f(0,-1,-1) #Лево низ
    glTexCoord3f(0, -1, 1)
    glVertex3f(0, -1, 1)  #Правая нижняя
    glTexCoord3f(0, 2, 1)
    glVertex3f(0, 2, 1) #Право вверх

    glEnd()
    
    glPushMatrix()
    glTranslatef(1, 0.4, -0.3) 
    glRotatef(80, 1, 0, 0)
    glTexCoord3f(0, 1, 0)
    gluSphere(gluNewQuadric(), 0.05, 10, 10 )  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0.4, 0.3) 
    glRotatef(80, 1, 0, 0)
    glTexCoord3f(0, 1, 0)
    gluSphere(gluNewQuadric(), 0.05, 10, 10 )  
    glPopMatrix()

def display(texture_id):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    draw_func(texture_id)
    glDisable(GL_TEXTURE_2D)
    pygame.display.flip()

def main():
    pygame.init()
    window_size = (640, 480)
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
    gluPerspective(45, (window_size[0] / window_size[1]), 0.1, 50.0)
    glTranslatef(0.0, -0.2, -5.0)

    texture_id = load_texture('case.jpg')    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)  # Example rotation
        display(texture_id)  # Render the scene
        pygame.time.wait(20)

main()