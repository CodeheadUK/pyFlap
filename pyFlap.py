import os, sys
import pygame

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

pipeLocation = []
cloudPos = []
buildingPos = []
grassPos = []

birdPosX = 100
birdPosY = 100
birdRot = 0
pipeGap = 0

def main():
    global birdPosX, birdPosY, birdRot, pipeGap

    pygame.init()
    gameInit()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('PyGme Test')
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((150, 150, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Load Textures
    birdImg = pygame.image.load('assets/bird1.png')
    birdImg = pygame.transform.scale(birdImg, (128, 128))

    cloudImg = pygame.image.load('assets/clouds.png')
    pipeTmp = pygame.image.load('assets/pipe.png')
    pipeImg = pygame.transform.scale(pipeTmp, (128, 512))
    pipeCapImg = pygame.image.load('assets/pipe_cap.png')
    pipeCapImg2 = pygame.transform.flip(pipeCapImg, False, True)
    buildingImg = pygame.image.load('assets/buildings.png')
    grassImg = pygame.image.load('assets/grass.png')

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                birdPosY = 100

        # Clear screen
        screen.blit(background, (0, 0))

        # Draw clouds
        for cloud in cloudPos:
            screen.blit(cloudImg, (cloud[0], cloud[1]))
            cloud[0] -= 0.25
            if(cloud[0] < -255):
                cloud[0] = 1024

        # Draw buildings
        for building in buildingPos:
            screen.blit(buildingImg, (building[0], building[1]))
            building[0] -= 0.5
            if(building[0] < -255):
                building[0] = 1024

        # Draw grass
        for grass in grassPos:
            screen.blit(grassImg, (grass[0], grass[1]))
            grass[0] -= 1
            if(grass[0] < -255):
                grass[0] = 1024

        # Draw bird
        orig_rect = birdImg.get_rect()
        birdRotImg = pygame.transform.rotate(birdImg, birdRot)
        rot_rect = orig_rect.copy()
        rot_rect.center = birdRotImg.get_rect().center
        birdRotImg = birdRotImg.subsurface(rot_rect).copy()
        screen.blit(birdRotImg, (birdPosX, birdPosY))
        birdPosY += 1
        birdRot += 5

        # Draw pipes
        for pipe in pipeLocation:
                # Pipe Stem
                screen.blit(pipeImg, (pipe[0], pipe[2]))
                screen.blit(pipeImg, (pipe[0], pipe[2]-pipeGap-550))

                # Pipe Caps
                screen.blit(pipeCapImg, (pipe[0], pipe[2]-10))#
                screen.blit(pipeCapImg2, (pipe[0], pipe[2]-pipeGap-68))

                pipe[0] -= 3
                if(pipe[0] < -400):
                    pipe[0] = 800

        # Update screen
        pygame.display.flip()
        clock.tick(60)


def gameInit():
    global birdPosX, birdPosY, birdRot, pipeGap

    # Set up pipe locations
    pipeLocation.append([800,  False, 400])
    pipeLocation.append([1200, False, 450])
    pipeLocation.append([1600, False, 500])

    # Set up cloud, building and foreground locations
    for x in range(0, 1025, 256):
        cloudPos.append([x, 315])
        buildingPos.append([x, 600-255])
        grassPos.append([x, 600-255])

    birdPosX = 100
    birdPosY = 100

    pipeGap = 150



if __name__ == "__main__":
    main()
