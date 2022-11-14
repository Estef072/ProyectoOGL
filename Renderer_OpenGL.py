from pickle import TRUE
import pygame
from pygame.locals import *
from shaders import *
from gl import Renderer, Model


pygame.display.set_caption('Proyecto OGL - Estefania Elvira Ramos')
width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -5

face = Model("cala.obj", "cala.bmp")

face.position.z -= 5
face.scale.x = 2
face.scale.y = 2
face.scale.z = 2


rend.scene.append( face )


isRunning = True
isStop = False

zoom = 50
ladox = 200
ladoy = 200


while isRunning:

    keys = pygame.key.get_pressed()
    opcion1 = keys[K_LSHIFT] and keys[K_1]
    opcion2 = keys[K_LSHIFT] and keys[K_2]
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
                    
    ##Movimiento  de las camaras en el eje Y y X
    if keys[K_LEFT]:
        if ladox > 0:
            rend.camPosition.x -= 10 * deltaTime
            ladox -= 10
    elif keys[K_RIGHT]:
        if ladox <= 360:
            rend.camPosition.x += 10 * deltaTime
            ladox += 10
    elif keys[K_UP]:
        if ladoy <= 360:
            rend.camPosition.y += 10 * deltaTime
            ladoy += 10
    elif keys[K_DOWN]:
        if ladoy > 0:
            rend.camPosition.y -= 10 * deltaTime
            ladoy -= 10
    ##Zoom de las camaras y alejar
    if keys[K_z]:
        if zoom <= 100:
            rend.camPosition.z -= 10  * deltaTime
            zoom += 1
    elif keys[K_a]:
        if zoom > 0:
            rend.camPosition.z += 10 * deltaTime
            zoom -= 1
    
    ##Zoom con el mouse
    if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                if zoom <= 100:
                    rend.camPosition.z -= 50 * deltaTime
                    zoom += 10
            elif event.y == -1:
                if zoom > 0:
                    rend.camPosition.z += 50*deltaTime
                    zoom -= 10
    ##SHADERSSSS
    if keys[K_1]: 
        rend.setShaders(vertex_shader, fragment_shader)

    elif keys[K_2]: 
        rend.setShaders(vertex_shader, toon_shader)
    


    ##MENU
    if opcion1:
        rend.scene.clear()
        face = Model("cala.obj", "cala.bmp")

        face.position.z -= 5
        face.scale.x = 2
        face.scale.y = 2
        face.scale.z = 2

        rend.scene.append( face )

    elif opcion2:
        rend.scene.clear()
        face = Model("mask.obj", "mask.bmp")

        face.position.z -= 5
        face.scale.x = 2
        face.scale.y = 2
        face.scale.z = 2

        rend.scene.append( face )
    
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()