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
    #  
    ##MODELO1
    opcionM1s1 = keys[K_m] and keys[K_1]
    opcionM1s2 = keys[K_m] and keys[K_2]
    opcionM1s3= keys[K_m] and keys[K_3]
    opcionM1s4= keys[K_m] and keys[K_4]
    ##MODELO 2
    opcionM2s1=  keys[K_n] and keys[K_1]
    opcionM2s2=  keys[K_n] and keys[K_2]
    opcionM2s3=  keys[K_n] and keys[K_3]
    opcionM2s4=  keys[K_n] and keys[K_4]

    ##MODEL 3   
    opcionM3s1=  keys[K_b] and keys[K_1]
    opcionM3s2=  keys[K_b] and keys[K_2]
    opcionM3s3=  keys[K_b] and keys[K_3]
    opcionM3s4=  keys[K_b] and keys[K_4]

    ##MODEL 4
    opcionM4s1=  keys[K_v] and keys[K_1]
    opcionM4s2=  keys[K_v] and keys[K_2]
    opcionM4s3=  keys[K_v] and keys[K_3]
    opcionM4s4=  keys[K_v] and keys[K_4]
    
    ##MODEL 5
    opcionM5s1=  keys[K_c] and keys[K_1]
    opcionM5s2=  keys[K_c] and keys[K_2]
    opcionM5s3=  keys[K_c] and keys[K_3]
    opcionM5s4=  keys[K_c] and keys[K_4]


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
    ##Menu Modelo2
    elif opcionM2s1:
        rend.scene.clear()
        face = Model("spider.obj", "spider.bmp")
        face.position.z -= .8
        face.scale.x = .0009
        face.scale.y = .009
        face.scale.z = .0009
        rend.scene.append( face )
    
    elif opcionM2s2:
        rend.scene.clear()
        face = Model("spider.obj", "spider.bmp")
        face.position.z -= .8
        face.scale.x = .0009
        face.scale.y = .009
        face.scale.z = .0009
        rend.scene.append( face )
    elif opcionM2s3:
        rend.scene.clear()
        face = Model("spider.obj", "spider.bmp")
        face.position.z -= .8
        face.scale.x = .0009
        face.scale.y = .009
        face.scale.z = .0009
        rend.scene.append( face )
    
    elif opcionM2s4:
        rend.scene.clear()
        face = Model("spider.obj", "spider.bmp")
        face.position.z -= .8
        face.scale.x = .0009
        face.scale.y = .009
        face.scale.z = .0009
        rend.scene.append( face )

    ##Menu Modelo3
    elif opcionM3s1:
        rend.scene.clear()
        face = Model("skull.obj", "skull.bmp")
        face.position.z -= 5
        face.scale.x = 12
        face.scale.y = 12
        face.scale.z =12
        rend.scene.append( face )

    elif opcionM3s2:
        rend.scene.clear()
        face = Model("skull.obj", "skull.bmp")
        face.position.z -= 5
        face.scale.x = 12
        face.scale.y = 12
        face.scale.z = 12
        rend.scene.append( face )

    elif opcionM3s3:
        rend.scene.clear()
        face = Model("skull.obj", "skull.bmp")
        face.position.z -= 5
        face.scale.x =12
        face.scale.y = 12
        face.scale.z = 12
        rend.scene.append( face )
    elif opcionM3s4:
        rend.scene.clear()
        face = Model("skull.obj", "skull.bmp")
        face.position.z -= 5
        face.scale.x = 12
        face.scale.y = 12
        face.scale.z = 12
        rend.scene.append( face )


    ##MODEL 4
    elif opcionM4s1:
        rend.scene.clear()
        face = Model("Ghost.obj", "ghost.bmp")
        face.position.z -=6
        face.scale.x = .021111
        face.scale.y = .021111
        face.scale.z = .021111
        rend.scene.append( face )
    elif opcionM4s2:
        rend.scene.clear()
        face = Model("Ghost.obj", "ghost.bmp")
        face.position.z -=6
        face.scale.x = .021111
        face.scale.y = .021111
        face.scale.z = .021111
        rend.scene.append( face )
    elif opcionM4s3:
        rend.scene.clear()
        face = Model("Ghost.obj", "ghost.bmp")
        face.position.z -=6
        face.scale.x = .021111
        face.scale.y = .021111
        face.scale.z = .021111
        rend.scene.append( face )
    elif opcionM4s4:
        rend.scene.clear()
        face = Model("Ghost.obj", "ghost.bmp")
        face.position.z -=6
        face.scale.x = .021111
        face.scale.y = .021111
        face.scale.z = .021111
        rend.scene.append( face )

    deltaTime = clock.tick(60) / 1000
    

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()