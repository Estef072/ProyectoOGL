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

fondo = pygame.image.load("fondo.jpeg")
screen.blit(fondo,(0,0))

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -5

face = Model("cala.obj", "cala.bmp")

face.position.z -= 5
face.scale.x = 5
face.scale.y = 2
face.scale.z = 5

##Sonido 
pygame.mixer.music.load("hallowen.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
rend.scene.append( face )


isRunning = True
isStop = False

zoom = 50
ladox = 200
ladoy = 200


while isRunning:

    keys = pygame.key.get_pressed()
    ##Valores de los Keys para poder ver los modelos 
    ##MODELO1
    opcionM1s1 = keys[K_m] and keys[K_1]
    opcionM1s2 = keys[K_m] and keys[K_2]
    opcionM1s3= keys[K_m] and keys[K_3]
    opcionM1s4= keys[K_m] and keys[K_4]

    ##MODELO 2
    
    

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
    ## DOCUMENTACION: https://pythonprogramming.altervista.org/pygame-and-mouse-events/
    if event.type == pygame.MOUSEWHEEL:
    
        if zoom <= 100:
            rend.camPosition.z -= 10 * deltaTime
            zoom += 1
    
        elif zoom > 0:
            rend.camPosition.z += 10*deltaTime
            zoom -= 1
    ##SHADERSSSS
    if keys[K_1]: 
        rend.setShaders(vertex_shader, fragment_shader)

    elif keys[K_2]: 
        rend.setShaders(vertex_shader, toon_shader)
    elif keys[K_3]: 
        rend.setShaders(vertex_shader, electry_shader )

    elif keys[K_4]:
        rend.setShaders(vertex_shader,multicolor_shader)
  
    
    
    ##MENU MODELO 1
    if opcionM1s1:
        rend.scene.clear()
        face = Model("cala.obj", "cala.bmp")

        face.position.z -= 5
        face.scale.x = 5
        face.scale.y = 3
        face.scale.z = 5
        rend.scene.append( face )

    elif opcionM1s2:
        rend.scene.clear()
        face = Model("cala.obj", "cala.bmp")

        face.position.z -= 5
        face.scale.x = 5
        face.scale.y = 3
        face.scale.z = 5

        rend.scene.append( face )

    elif opcionM1s3:
        rend.scene.clear()
        face = Model("cala.obj", "cala.bmp")
        face.position.z -= 5
        face.scale.x = 5
        face.scale.y = 3
        face.scale.z = 5
        rend.scene.append( face )

    elif opcionM1s4:
        rend.scene.clear()
        face = Model("cala.obj", "cala.bmp")

        face.position.z -= 5
        face.scale.x = 5
        face.scale.y = 3
        face.scale.z = 5

        rend.scene.append( face )
    
    
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()