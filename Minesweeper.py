# notes
# Add clickable buttons to home screen
# Difficuly select --> Noob(6x6, 5 mines), Easy(9x9, 10 mines), Medium(16x16, 40 mines), Expert(30x16, 99 mines)
# Level select --> pick level 1,2,3,4,5
# Quit --> Exit game

# New Game Coordinates =
# Level Select Coordinates =
# Quir Coordinates =
# //////////////////////////////////////////////////////////////////////////////////////

# https://www.reddit.com/r/pygame/comments/2laqft/switching_background_colors_within_a_loop/
import random, pygame, sys, os
from pygame.locals import *

# set constants
FPS = 30
windowWidth = 1200
windowHeight = 650
boxSize = 25
gapSize = 5

# assign colors
LIGHTGRAY = (225, 225, 225)
DARKGRAY = (160, 160, 160)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
HOTPINK = (244, 66, 182)
GREY = (73, 73, 73)
YELLOW = (255, 251, 35)
LIGHTBLUE = (66, 134, 244)
FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
FLOURESCENTGREEN = (63, 255, 0)
BIGRED = (206, 16, 16)

# set up major colors
BGCOLOR = ORANGE
FIELDCOLOR = BLACK
BOXCOLOR_COV = DARKGRAY  # covered box color
BOXCOLOR_REV = LIGHTGRAY  # revealed box color
MINECOLOR = BLACK
TEXTCOLOR_1 = BLUE
TEXTCOLOR_2 = RED
TEXTCOLOR_3 = BLACK
HILITECOLOR = RED
RESETBGCOLOR = LIGHTGRAY
MINEMARK_COV = RED

# set up font
FONTTYPE = 'Comic Sans MS'
FONTSIZE = 18


def mainScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        timer = 0
        if pygame.time.get_ticks() - timer > 300:  # change the number value to change how long a color lasts on the page
            timer = pygame.time.get_ticks()
            bg = (random.randint(100, 220), random.randint(100, 220),
                  random.randint(100, 220) != (0, 0, 0) != (255, 255, 255))
        pygame.display.update()
        clock.tick(
            30)  # fps (30 is fine but could be reduced if lagging because minesweeper doesn't really refresh a lot
        screen.fill(bg)
        rectx = 5
        recty = 11
        rectchangex = 5
        rectchangey = 5
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, BLACK, [rectx, recty, 250, 159], 2)  # selection screen
        pygame.draw.rect(screen, LIGHTGRAY, [35, 20, 185, 44], 0)  # new game
        pygame.draw.rect(screen, LIGHTGRAY, [40, 70, 175, 44], 0)  # creators
        pygame.draw.rect(screen, LIGHTGRAY, [80, 119, 97, 44], 0)  # Quit

        if 80 + 97 > mouse[0] > 80 and 119 + 44 > mouse[1] > 119:  # QUIT button
            pygame.draw.rect(screen, WHITE, (80, 119, 97, 44))
            if click[0] == 1:
                pygame.quit()
                sys.exit()

        if 40 + 175 > mouse[0] > 40 and 70 + 44 > mouse[1] > 70:  # creators button
            pygame.draw.rect(screen, WHITE, (40, 70, 175, 44))
            if click[0] == 1:
                clicksound.play()
                creators()

        if 35 + 185 > mouse[0] > 35 and 20 + 44 > mouse[1] > 20:  # new game
            pygame.draw.rect(screen, WHITE, (35, 20, 185, 44))
            if click[0] == 1:
                clicksound.play()
                newgame()

        font = pygame.font.SysFont("comicsansms", 35)
        text = font.render("New Game", True, BLACK)
        screen.blit(text, (211 - text.get_width(), 66 - text.get_height()))
        text = font.render("Creators", True, BLACK)
        screen.blit(text, (200 - text.get_width(), 115 - text.get_height()))
        text = font.render("Quit", True, BLACK)
        screen.blit(text, (165 - text.get_width(), 163 - text.get_height()))
        text = font.render("Minesweeper Feat.", True, BLACK)
        screen.blit(text, (753 - text.get_width(), 100 - text.get_height()))
        text = font.render("Kim Jong Un", True, BLACK)
        screen.blit(text, (695 - text.get_width(), 140 - text.get_height()))
        # text = font.render("A PC Production", True, BLACK)
        # screen.blit(text, (727 - text.get_width(), 650 - text.get_height()))
        screen.blit(bomb, (10, 10))
        screen.blit(KJ, (5, 180))
        screen.blit(nuke, (800, 50))
        screen.blit(nuke2, (220, 50))
        screen.blit(kim2, (490, 500))
        screen.blit(funnykim, (400, 150))
        pygame.display.update()


def mainScreen2():
    onMain = True
    while onMain:
        screen.fill(HOTPINK)
        pygame.draw.rect(screen, WHITE, [0, 600, 100, 50], 0)
        text = font.render("Back", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Back", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onMain = False
                mainScreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def newgame():
    onNew = True
    while onNew:
        screen.fill(LIGHTBLUE)
        pygame.draw.rect(screen, BLACK, [942, 410, 250, 235], 2)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, BLACK, [1023, 473, 88, 36], 2)  # 6x6
        pygame.draw.rect(screen, BLACK, [1023, 514, 88, 36], 2)  # 9x9
        pygame.draw.rect(screen, BLACK, [1013, 554, 108, 36], 2)  # 16x16
        pygame.draw.rect(screen, BLACK, [1013, 593, 108, 36], 2)  # 30x16
        font = pygame.font.SysFont("comicsansms", 35)
        text = font.render("If You Beat Level 3 You Are Legally Skilled", True, BLACK)
        screen.blit(text, (949 - text.get_width(), 66 - text.get_height()))
        screen.blit(minefield, (100, 100))
        screen.blit(bomblogo, (1000, 475))
        screen.blit(bomblogo, (1000, 517))
        screen.blit(bomblogo, (1118, 517))
        screen.blit(bomblogo, (990, 556))
        screen.blit(bomblogo, (1127, 556))
        screen.blit(bomblogo, (965, 556))
        screen.blit(bomblogo, (990, 596))
        screen.blit(bomblogo, (1127, 596))
        screen.blit(bomblogo, (965, 596))
        screen.blit(bomblogo, (1150, 596))
        if 1023 + 88 > mouse[0] > 1023 and 473 + 36 > mouse[1] > 473:  # 6x6
            pygame.draw.rect(screen, WHITE, (1023, 473, 89, 37))
            if click[0] == 1:
                clicksound.play()
                sixXsix()

        if 1023 + 88 > mouse[0] > 1023 and 514 + 36 > mouse[1] > 514:  # 9x9
            pygame.draw.rect(screen, WHITE, (1023, 514, 89, 37))
            if click[0] == 1:
                clicksound.play()
                nineXnine()

        if 1013 + 108 > mouse[0] > 1013 and 554 + 36 > mouse[1] > 554:  # 16x16
            pygame.draw.rect(screen, WHITE, (1013, 554, 109, 37))
            if click[0] == 1:
                clicksound.play()
                sixteenXsixteen()

        if 1013 + 108 > mouse[0] > 1013 and 593 + 36 > mouse[1] > 593:  # 30x16
            pygame.draw.rect(screen, WHITE, (1013, 593, 109, 37))
            if click[0] == 1:
                clicksound.play()
                thirtyXsixteen()
        font = pygame.font.SysFont("comicsansms", 35)
        text = font.render("Level Select", True, BLACK)
        screen.blit(text, (1169 - text.get_width(), 466 - text.get_height()))
        text = font.render("6x6", True, BLACK)
        screen.blit(text, (1100 - text.get_width(), 515 - text.get_height()))
        text = font.render("9x9", True, BLACK)
        screen.blit(text, (1100 - text.get_width(), 555 - text.get_height()))
        text = font.render("16x16", True, BLACK)
        screen.blit(text, (1116 - text.get_width(), 595 - text.get_height()))
        text = font.render("30x16", True, BLACK)
        screen.blit(text, (1116 - text.get_width(), 635 - text.get_height()))
        pygame.draw.rect(screen, WHITE, [0, 600, 100, 50], 0)
        text = font.render("Back", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Back", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onNew = False
                clicksound.play()
                mainScreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def creators():
    onscreen = True
    while onscreen:
        screen.fill(YELLOW)
        screen.blit(PeterPic, (10, 10))
        screen.blit(AndrewPic, (650, 10))
        text = font.render("Peter 'voz' Chuchra", True, BLACK)
        screen.blit(text, (370 - text.get_width(), 455 - text.get_height()))
        text = font.render("Andrew 'parkaz' Park", True, BLACK)
        screen.blit(text, (1085 - text.get_width(), 450 - text.get_height()))
        pygame.draw.rect(screen, WHITE, [0, 600, 100, 50], 0)
        text = font.render("Back", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Back", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onscreen = False
                clicksound.play()
                mainScreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def deathScreen():
    onDeath = True
    while onDeath:
        screen.fill(BIGRED)
        screen.blit(KimSerious, (100, 100))
        text = font.render("Back", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Back", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onDeath = False
                clicksound.play()
                mainScreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def LevelOneFirstLine():
    onOne = True
    while onOne:
        screen.fill(RED)
        screen.blit(bricks, (0, 0))
        pygame.draw.rect(screen, WHITE, (300, 450, 600, 200))
        font2 = pygame.font.SysFont("comicsansms", 20)
        text = font2.render("You are sick of Kim Jong Un's rule and you decide to make", True, BLACK)
        screen.blit(text, (875 - text.get_width(), 500 - text.get_height()))
        text = font2.render("an escape. You make your way from your house in Northern", True, BLACK)
        screen.blit(text, (864 - text.get_width(), 540 - text.get_height()))
        text = font2.render("North Korea to the KumKangSan Mountains to take refuge.", True, BLACK)
        screen.blit(text, (870 - text.get_width(), 580 - text.get_height()))
        text = font2.render("As you're riding your cow south, you encounter a minefield!", True, BLACK)
        screen.blit(text, (855 - text.get_width(), 620 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text = font.render("Next", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Next", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onOne = False
                clicksound.play()
                sixgame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def LevelTwoFirstLine():
    onTwo = True
    while onTwo:
        screen.fill(RED)
        screen.blit(bricks, (0, 0))
        pygame.draw.rect(screen, WHITE, (300, 450, 600, 200))
        font2 = pygame.font.SysFont("comicsansms", 20)
        text = font2.render("You evade the minefield however, now there is a roadblock", True, BLACK)
        screen.blit(text, (865 - text.get_width(), 500 - text.get_height()))
        text = font2.render("blocking your way. You are forced to run through a forest", True, BLACK)
        screen.blit(text, (864 - text.get_width(), 540 - text.get_height()))
        text = font2.render("to avoid being caught by the ruthless North Korean Military.", True, BLACK)
        screen.blit(text, (870 - text.get_width(), 580 - text.get_height()))
        text = font2.render("Avoid all of the nuke mines that the North Koreans planted!", True, BLACK)
        screen.blit(text, (875 - text.get_width(), 620 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text = font.render("Next", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Next", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onTwo = False
                clicksound.play()
                ninegame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def LevelThreeFirstLine():
    onThree = True
    while onThree:
        screen.fill(RED)
        screen.blit(bricks, (0, 0))
        pygame.draw.rect(screen, WHITE, (300, 450, 600, 200))
        font2 = pygame.font.SysFont("comicsansms", 20)
        text = font2.render("You manage to make your way through the forest with many", True, BLACK)
        screen.blit(text, (865 - text.get_width(), 500 - text.get_height()))
        text = font2.render("close calls! As you approach the DMZ, you prepare to sprint", True, BLACK)
        screen.blit(text, (864 - text.get_width(), 540 - text.get_height()))
        text = font2.render("to the other side. There are many guards prepared to shoot", True, BLACK)
        screen.blit(text, (870 - text.get_width(), 580 - text.get_height()))
        text = font2.render("RUN!!!!!", True, BLACK)
        screen.blit(text, (630 - text.get_width(), 620 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text = font.render("Next", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Next", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onThree = False
                clicksound.play()
                sixteengame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def LevelFourFirstLine():
    onFour = True
    while onFour:
        screen.fill(RED)
        screen.blit(bricks, (0, 0))
        pygame.draw.rect(screen, WHITE, (300, 450, 600, 200))
        font2 = pygame.font.SysFont("comicsansms", 20)
        text = font2.render("You managed to arrive at the South Korean side of the DMZ", True, BLACK)
        screen.blit(text, (865 - text.get_width(), 500 - text.get_height()))
        text = font2.render("but the South Koreans also adopted the Nuke Mine technology", True, BLACK)
        screen.blit(text, (864 - text.get_width(), 540 - text.get_height()))
        text = font2.render("you prepare for the last sprint, which will get you safely to South Korea", True, BLACK)
        screen.blit(text, (870 - text.get_width(), 580 - text.get_height()))
        text = font2.render("RUN!!!!!", True, BLACK)
        screen.blit(text, (630 - text.get_width(), 620 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text = font.render("Next", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Next", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onFour = False
                clicksound.play()
                lastgame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def sixXsix():  # six by six level function
    fieldHeight = 6
    fieldWidth = 6
    minesTotal = 10
    LevelOneFirstLine()


def nineXnine():  # nine by nine level function
    fieldHeight = 9
    fieldWidth = 9
    minesTotal = 10
    LevelTwoFirstLine()


def sixteenXsixteen():  # sixteen by sixteen level function
    fieldHeight = 16
    fieldWidth = 16
    minesTotal = 50
    LevelThreeFirstLine()


def thirtyXsixteen():  # thirty by sixteen level function
    fieldHeight = 16
    fieldWidth = 30
    minesTotal = 100
    LevelFourFirstLine()


def sixgame():
    # initialize global variables & pygame module, set caption
    global FPSCLOCK, screen, BASICFONT, fieldWidth, fieldHeight, marginX, marginY, minesTotal
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    BASICFONT = pygame.font.SysFont(FONTTYPE, FONTSIZE)
    fieldWidth = 6
    fieldHeight = 6
    marginX = int((windowWidth - (fieldWidth * (boxSize + gapSize))) / 2)
    marginY = int((windowHeight - (fieldHeight * (boxSize + gapSize))) / 2)
    minesTotal = 8

    # stores XY of mouse events
    mouse_x = 0
    mouse_y = 0

    # set up data structures and lists
    mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

    # set background color
    screen.fill(BGCOLOR)

    # main game loop
    while True:

        # check for quit function
        checkForKeyPress()

        # initialize input booleans
        mouseClicked = False
        spacePressed = False

        # draw field
        screen.fill(BGCOLOR)
        pygame.draw.rect(screen, FIELDCOLOR, (
        marginX - 5, marginY - 5, (boxSize + gapSize) * fieldWidth + 5, (boxSize + gapSize) * fieldHeight + 5))
        drawField()
        drawMinesNumbers(mineField)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    spacePressed = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    spacePressed = False

        # draw covers
        drawCovers(revealedBoxes, markedMines)

        # mine marker tip
        tipFont = pygame.font.SysFont(FONTTYPE, 16)  ## not using BASICFONT - too big
        drawText('Tip: Highlight a box and press space', tipFont, TEXTCOLOR_3, screen,
                 windowWidth / 2, windowHeight - 60)
        drawText('to mark areas that you think contain nukes.', tipFont, TEXTCOLOR_3, screen, windowWidth / 2,
                 windowHeight - 40)

        # determine boxes at clicked areas
        box_x, box_y = getBoxAtPixel(mouse_x, mouse_y)

        # mouse not over a box in field
        if (box_x, box_y) == (None, None):

            pass

        # mouse currently over box in field
        else:

            # highlight unrevealed box
            if not revealedBoxes[box_x][box_y]:
                highlightBox(box_x, box_y)

                # mark mines
                if spacePressed:
                    markedMines.append([box_x, box_y])

                # reveal clicked boxes
                if mouseClicked:
                    revealedBoxes[box_x][box_y] = True

                    # when 0 is revealed, show relevant boxes
                    if mineField[box_x][box_y] == '[0]':
                        showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY)

                    # when mine is revealed, show mines
                    if mineField[box_x][box_y] == '[X]':
                        deathscreen()
        # check if player has won
        if gameWon(revealedBoxes, mineField):
            victoryscreen()

        # redraw screen, wait clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def ninegame():
    # initialize global variables & pygame module, set caption
    global FPSCLOCK, screen, BASICFONT, fieldWidth, fieldHeight, marginX, marginY, minesTotal
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    BASICFONT = pygame.font.SysFont(FONTTYPE, FONTSIZE)

    # stores XY of mouse events
    mouse_x = 0
    mouse_y = 0

    fieldWidth = 9
    fieldHeight = 9
    marginX = int((windowWidth - (fieldWidth * (boxSize + gapSize))) / 2)
    marginY = int((windowHeight - (fieldHeight * (boxSize + gapSize))) / 2)
    minesTotal = 20

    # set up data structures and lists
    mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

    # set background color
    screen.fill(BGCOLOR)

    # main game loop
    while True:

        # check for quit function
        checkForKeyPress()

        # initialize input booleans
        mouseClicked = False
        spacePressed = False

        # draw field
        screen.fill(BGCOLOR)
        pygame.draw.rect(screen, FIELDCOLOR, (
        marginX - 5, marginY - 5, (boxSize + gapSize) * fieldWidth + 5, (boxSize + gapSize) * fieldHeight + 5))
        drawField()
        drawMinesNumbers(mineField)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    spacePressed = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    spacePressed = False

        # draw covers
        drawCovers(revealedBoxes, markedMines)

        # mine marker tip
        tipFont = pygame.font.SysFont(FONTTYPE, 16)  ## not using BASICFONT - too big
        drawText('Tip: Highlight a box and press space (rather than click the mouse)', tipFont, TEXTCOLOR_3, screen,
                 windowWidth / 2, windowHeight - 60)
        drawText('to mark areas that you think contain mines.', tipFont, TEXTCOLOR_3, screen, windowWidth / 2,
                 windowHeight - 40)

        # determine boxes at clicked areas
        box_x, box_y = getBoxAtPixel(mouse_x, mouse_y)

        # mouse not over a box in field
        if (box_x, box_y) == (None, None):

            pass

        # mouse currently over box in field
        else:

            # highlight unrevealed box
            if not revealedBoxes[box_x][box_y]:
                highlightBox(box_x, box_y)

                # mark mines
                if spacePressed:
                    markedMines.append([box_x, box_y])

                # reveal clicked boxes
                if mouseClicked:
                    revealedBoxes[box_x][box_y] = True

                    # when 0 is revealed, show relevant boxes
                    if mineField[box_x][box_y] == '[0]':
                        showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY)

                    # when mine is revealed, show mines
                    if mineField[box_x][box_y] == '[X]':
                        deathscreen()
        # check if player has won
        if gameWon(revealedBoxes, mineField):
            victoryscreen()

        # redraw screen, wait clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def sixteengame():
    # initialize global variables & pygame module, set caption
    global FPSCLOCK, screen, BASICFONT, fieldWidth, fieldHeight, marginX, marginY, minesTotal
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    BASICFONT = pygame.font.SysFont(FONTTYPE, FONTSIZE)

    fieldWidth = 16
    fieldHeight = 16
    marginX = int((windowWidth - (fieldWidth * (boxSize + gapSize))) / 2)
    marginY = int((windowHeight - (fieldHeight * (boxSize + gapSize))) / 2)
    minesTotal = 40

    # stores XY of mouse events
    mouse_x = 0
    mouse_y = 0

    # set up data structures and lists
    mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

    # set background color
    screen.fill(BGCOLOR)

    # main game loop
    while True:

        # check for quit function
        checkForKeyPress()

        # initialize input booleans
        mouseClicked = False
        spacePressed = False

        # draw field
        screen.fill(BGCOLOR)
        pygame.draw.rect(screen, FIELDCOLOR, (
        marginX - 5, marginY - 5, (boxSize + gapSize) * fieldWidth + 5, (boxSize + gapSize) * fieldHeight + 5))
        drawField()
        drawMinesNumbers(mineField)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    spacePressed = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    spacePressed = False

        # draw covers
        drawCovers(revealedBoxes, markedMines)

        # mine marker tip
        tipFont = pygame.font.SysFont(FONTTYPE, 16)  ## not using BASICFONT - too big
        drawText('Tip: Highlight a box and press space (rather than click the mouse)', tipFont, TEXTCOLOR_3, screen,
                 windowWidth / 2, windowHeight - 60)
        drawText('to mark areas that you think contain mines.', tipFont, TEXTCOLOR_3, screen, windowWidth / 2,
                 windowHeight - 40)

        # determine boxes at clicked areas
        box_x, box_y = getBoxAtPixel(mouse_x, mouse_y)

        # mouse not over a box in field
        if (box_x, box_y) == (None, None):

            pass

        # mouse currently over box in field
        else:

            # highlight unrevealed box
            if not revealedBoxes[box_x][box_y]:
                highlightBox(box_x, box_y)

                # mark mines
                if spacePressed:
                    markedMines.append([box_x, box_y])

                # reveal clicked boxes
                if mouseClicked:
                    revealedBoxes[box_x][box_y] = True

                    # when 0 is revealed, show relevant boxes
                    if mineField[box_x][box_y] == '[0]':
                        showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY)

                    # when mine is revealed, show mines
                    if mineField[box_x][box_y] == '[X]':
                        deathscreen()
        # check if player has won
        if gameWon(revealedBoxes, mineField):
            victoryscreen()

        # redraw screen, wait clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def lastgame():
    # initialize global variables & pygame module, set caption
    global FPSCLOCK, screen, BASICFONT, fieldWidth, fieldHeight, marginX, marginY, minesTotal
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    BASICFONT = pygame.font.SysFont(FONTTYPE, FONTSIZE)

    fieldWidth = 30
    fieldHeight = 16
    marginX = int((windowWidth - (fieldWidth * (boxSize + gapSize))) / 2)
    marginY = int((windowHeight - (fieldHeight * (boxSize + gapSize))) / 2)
    minesTotal = 60

    # stores XY of mouse events
    mouse_x = 0
    mouse_y = 0

    # set up data structures and lists
    mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

    # set background color
    screen.fill(BGCOLOR)

    # main game loop
    while True:

        # check for quit function
        checkForKeyPress()

        # initialize input booleans
        mouseClicked = False
        spacePressed = False

        # draw field
        screen.fill(BGCOLOR)
        pygame.draw.rect(screen, FIELDCOLOR, (
        marginX - 5, marginY - 5, (boxSize + gapSize) * fieldWidth + 5, (boxSize + gapSize) * fieldHeight + 5))
        drawField()
        drawMinesNumbers(mineField)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    spacePressed = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    spacePressed = False

        # draw covers
        drawCovers(revealedBoxes, markedMines)

        # mine marker tip
        tipFont = pygame.font.SysFont(FONTTYPE, 16)  ## not using BASICFONT - too big
        drawText('Tip: Highlight a box and press space (rather than click the mouse)', tipFont, TEXTCOLOR_3, screen,
                 windowWidth / 2, windowHeight - 60)
        drawText('to mark areas that you think contain mines.', tipFont, TEXTCOLOR_3, screen, windowWidth / 2,
                 windowHeight - 40)

        # determine boxes at clicked areas
        box_x, box_y = getBoxAtPixel(mouse_x, mouse_y)

        # mouse not over a box in field
        if (box_x, box_y) == (None, None):

            pass

        # mouse currently over box in field
        else:

            # highlight unrevealed box
            if not revealedBoxes[box_x][box_y]:
                highlightBox(box_x, box_y)

                # mark mines
                if spacePressed:
                    markedMines.append([box_x, box_y])

                # reveal clicked boxes
                if mouseClicked:
                    revealedBoxes[box_x][box_y] = True

                    # when 0 is revealed, show relevant boxes
                    if mineField[box_x][box_y] == '[0]':
                        showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY)

                    # when mine is revealed, show mines
                    if mineField[box_x][box_y] == '[X]':
                        deathscreen()
        # check if player has won
        if gameWon(revealedBoxes, mineField):
            victoryscreen()

        # redraw screen, wait clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def blankField():
    # creates blank fieldWidth x fieldHeight data structure

    field = []
    for x in range(fieldWidth):
        field.append([])
        for y in range(fieldHeight):
            field[x].append('[ ]')
    return field


def placeMines(field):
    # places mines in fieldWidth x fieldHeight data structure
    # requires blank field as input

    mineCount = 0
    xy = []
    while mineCount < minesTotal:
        x = random.randint(0, fieldWidth - 1)
        y = random.randint(0, fieldHeight - 1)
        xy.append([x, y])
        if xy.count([x, y]) > 1:
            xy.remove([x, y])
        else:
            field[x][y] = '[X]'
            mineCount += 1


def isThereMine(field, x, y):
    # checks if mine is located at specific box on field

    return field[x][y] == '[X]'


def placeNumbers(field):
    # places numbers in fieldWidth x fieldHeight data structure
    # requires field with mines as input

    for x in range(fieldWidth):
        for y in range(fieldHeight):
            if not isThereMine(field, x, y):
                count = 0
                if x != 0:
                    if isThereMine(field, x - 1, y):
                        count += 1
                    if y != 0:
                        if isThereMine(field, x - 1, y - 1):
                            count += 1
                    if y != fieldHeight - 1:
                        if isThereMine(field, x - 1, y + 1):
                            count += 1
                if x != fieldWidth - 1:
                    if isThereMine(field, x + 1, y):
                        count += 1
                    if y != 0:
                        if isThereMine(field, x + 1, y - 1):
                            count += 1
                    if y != fieldHeight - 1:
                        if isThereMine(field, x + 1, y + 1):
                            count += 1
                if y != 0:
                    if isThereMine(field, x, y - 1):
                        count += 1
                if y != fieldHeight - 1:
                    if isThereMine(field, x, y + 1):
                        count += 1
                field[x][y] = '[%s]' % (count)


def blankRevealedBoxData(val):
    # returns fieldWidth x fieldHeight data structure different from the field data structure
    # each item in data structure is boolean (val) to show whether box at those fieldWidth & fieldHeight coordinates should be revealed

    revealedBoxes = []
    for i in range(fieldWidth):
        revealedBoxes.append([val] * fieldHeight)
    return revealedBoxes


def gameSetup():
    # set up mine field data structure, list of all zeros for recursion, and revealed box boolean data structure

    mineField = blankField()
    placeMines(mineField)
    placeNumbers(mineField)
    zeroListXY = []
    markedMines = []
    revealedBoxes = blankRevealedBoxData(False)

    return mineField, zeroListXY, revealedBoxes, markedMines


def drawField():
    # draws field GUI and reset button

    for box_x in range(fieldWidth):
        for box_y in range(fieldHeight):
            left, top = getLeftTopXY(box_x, box_y)
            pygame.draw.rect(screen, BOXCOLOR_REV, (left, top, boxSize, boxSize))


def drawMinesNumbers(field):
    # draws mines and numbers onto GUI
    # field should have mines and numbers

    half = int(boxSize * 0.5)
    quarter = int(boxSize * 0.25)
    eighth = int(boxSize * 0.125)

    for box_x in range(fieldWidth):
        for box_y in range(fieldHeight):
            left, top = getLeftTopXY(box_x, box_y)
            center_x, center_y = getCenterXY(box_x, box_y)
            if field[box_x][box_y] == '[X]':
                pygame.draw.circle(screen, MINECOLOR, (left + half, top + half), quarter)
                pygame.draw.circle(screen, WHITE, (left + half, top + half), eighth)
                pygame.draw.line(screen, MINECOLOR, (left + eighth, top + half),
                                 (left + half + quarter + eighth, top + half))
                pygame.draw.line(screen, MINECOLOR, (left + half, top + eighth),
                                 (left + half, top + half + quarter + eighth))
                pygame.draw.line(screen, MINECOLOR, (left + quarter, top + quarter),
                                 (left + half + quarter, top + half + quarter))
                pygame.draw.line(screen, MINECOLOR, (left + quarter, top + half + quarter),
                                 (left + half + quarter, top + quarter))
            else:
                for i in range(1, 9):
                    if field[box_x][box_y] == '[' + str(i) + ']':
                        if i in range(1, 3):
                            textColor = TEXTCOLOR_1
                        else:
                            textColor = TEXTCOLOR_2
                        drawText(str(i), BASICFONT, textColor, screen, center_x, center_y)


def showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY):
    # modifies revealedBox data strucure if chosen box_x & box_y is [0]
    # show all boxes using recursion

    revealedBoxes[box_x][box_y] = True
    revealAdjacentBoxes(revealedBoxes, box_x, box_y)
    for i, j in getAdjacentBoxesXY(mineField, box_x, box_y):
        if mineField[i][j] == '[0]' and [i, j] not in zeroListXY:
            zeroListXY.append([i, j])
            showNumbers(revealedBoxes, mineField, i, j, zeroListXY)


def showMines(revealedBoxes, mineField, box_x, box_y):
    # modifies revealedBox data strucure if chosen box_x & box_y is [X]

    for i in range(fieldWidth):
        for j in range(fieldHeight):
            if mineField[i][j] == '[X]':
                revealedBoxes[i][j] = True


def revealAdjacentBoxes(revealedBoxes, box_x, box_y):
    # modifies revealedBoxes data structure so that all adjacent boxes to (box_x, box_y) are set to True

    if box_x != 0:
        revealedBoxes[box_x - 1][box_y] = True
        if box_y != 0:
            revealedBoxes[box_x - 1][box_y - 1] = True
        if box_y != fieldHeight - 1:
            revealedBoxes[box_x - 1][box_y + 1] = True
    if box_x != fieldWidth - 1:
        revealedBoxes[box_x + 1][box_y] = True
        if box_y != 0:
            revealedBoxes[box_x + 1][box_y - 1] = True
        if box_y != fieldHeight - 1:
            revealedBoxes[box_x + 1][box_y + 1] = True
    if box_y != 0:
        revealedBoxes[box_x][box_y - 1] = True
    if box_y != fieldHeight - 1:
        revealedBoxes[box_x][box_y + 1] = True


def getAdjacentBoxesXY(mineField, box_x, box_y):
    # get box XY coordinates for all adjacent boxes to (box_x, box_y)

    adjacentBoxesXY = []

    if box_x != 0:
        adjacentBoxesXY.append([box_x - 1, box_y])
        if box_y != 0:
            adjacentBoxesXY.append([box_x - 1, box_y - 1])
        if box_y != fieldHeight - 1:
            adjacentBoxesXY.append([box_x - 1, box_y + 1])
    if box_x != fieldWidth - 1:
        adjacentBoxesXY.append([box_x + 1, box_y])
        if box_y != 0:
            adjacentBoxesXY.append([box_x + 1, box_y - 1])
        if box_y != fieldHeight - 1:
            adjacentBoxesXY.append([box_x + 1, box_y + 1])
    if box_y != 0:
        adjacentBoxesXY.append([box_x, box_y - 1])
    if box_y != fieldHeight - 1:
        adjacentBoxesXY.append([box_x, box_y + 1])

    return adjacentBoxesXY


def drawCovers(revealedBoxes, markedMines):
    # uses revealedBox fieldWidth x fieldHeight data structure to determine whether to draw box covering mine/number
    # draw red cover instead of gray cover over marked mines

    for box_x in range(fieldWidth):
        for box_y in range(fieldHeight):
            if not revealedBoxes[box_x][box_y]:
                left, top = getLeftTopXY(box_x, box_y)
                if [box_x, box_y] in markedMines:
                    pygame.draw.rect(screen, MINEMARK_COV, (left, top, boxSize, boxSize))
                else:
                    pygame.draw.rect(screen, BOXCOLOR_COV, (left, top, boxSize, boxSize))


def drawText(text, font, color, surface, x, y):
    # function to easily draw text and also return object & rect pair

    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)


def drawButton(text, color, bgcolor, center_x, center_y):
    # similar to drawText but text has bg color and returns obj & rect

    butSurf = BASICFONT.render(text, True, color, bgcolor)
    butRect = butSurf.get_rect()
    butRect.centerx = center_x
    butRect.centery = center_y

    return (butSurf, butRect)


def getLeftTopXY(box_x, box_y):
    # get left & top coordinates for drawing mine boxes

    left = marginX + box_x * (boxSize + gapSize)
    top = marginY + box_y * (boxSize + gapSize)
    return left, top


def getCenterXY(box_x, box_y):
    # get center coordinates for drawing mine boxes

    center_x = marginX + boxSize / 2 + box_x * (boxSize + gapSize)
    center_y = marginY + boxSize / 2 + box_y * (boxSize + gapSize)
    return center_x, center_y


def getBoxAtPixel(x, y):
    # gets coordinates of box at mouse coordinates

    for box_x in range(fieldWidth):
        for box_y in range(fieldHeight):
            left, top = getLeftTopXY(box_x, box_y)
            boxRect = pygame.Rect(left, top, boxSize, boxSize)
            if boxRect.collidepoint(x, y):
                return (box_x, box_y)
    return (None, None)


def highlightBox(box_x, box_y):
    # highlight box when mouse hovers over it

    left, top = getLeftTopXY(box_x, box_y)
    pygame.draw.rect(screen, HILITECOLOR, (left, top, boxSize, boxSize), 4)


def highlightButton(butRect):
    # highlight button when mouse hovers over it

    linewidth = 4
    pygame.draw.rect(screen, HILITECOLOR, (
        butRect.left - linewidth, butRect.top - linewidth, butRect.width + 2 * linewidth,
        butRect.height + 2 * linewidth),
                     linewidth)


def gameWon(revealedBoxes, mineField):
    # check if player has revealed all boxes

    notMineCount = 0

    for box_x in range(fieldWidth):
        for box_y in range(fieldHeight):
            if revealedBoxes[box_x][box_y] == True:
                if mineField[box_x][box_y] != '[X]':
                    notMineCount += 1

    if notMineCount >= (fieldWidth * fieldHeight) - minesTotal:
        return True
    else:
        return False


def terminate():
    # simple function to exit game

    pygame.quit()
    sys.exit()


def checkForKeyPress():
    # check if quit or any other key is pressed

    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def victoryscreen():
    onVicotry = True
    while onVicotry:
        screen.fill(YELLOW)
        screen.blit(kimclap, (100, 100))
        text = font.render("I have been defeated :(", True, BLACK)
        screen.blit(text, (1085 - text.get_width(), 249 - text.get_height()))
        text = font.render("Next", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Back", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                onVicotry = False
                clicksound.play()
                newgame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def deathscreen():
    onDeath = True
    while onDeath:
        screen.fill(BIGRED)
        nukesound.play()
        screen.blit(KimSerious, (75, 100))
        screen.blit(redButton, (900, 65))
        screen.blit(KimFinger, (1005, 300))
        screen.blit(smallbomb, (220, 20))
        text = font.render("Mission Failed, we'll get'em next time", True, BLACK)
        screen.blit(text, (920 - text.get_width(), 649 - text.get_height()))
        text = font.render("GeT nUkEd By KiM jOgN uN", True, BLACK)
        screen.blit(text, (850 - text.get_width(), 600 - text.get_height()))
        text = font.render("Fail", True, BLACK)
        screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 100 > mouse[0] > 0 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREEN, (0, 600, 100, 50))
            text = font.render("Fail", True, BLACK)
            screen.blit(text, (85 - text.get_width(), 649 - text.get_height()))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


bricks = pygame.image.load("bricks.jpg")
funnykim = pygame.image.load("funnykim.jpg")
KJ = pygame.image.load("KJ.png")
bomb = pygame.image.load("bomb.png")
nuke = pygame.image.load("nuke.png")
nuke2 = pygame.image.load("nuke2.png")
minefield = pygame.image.load("minefield2.jpg")
minefield = pygame.transform.scale(minefield, (834, 418))
kim2 = pygame.image.load("kim2.png")
bomblogo = pygame.image.load("bomblogo.png")
bomblogo = pygame.transform.scale(bomblogo, (20, 25))
PeterPic = pygame.image.load("MeLOL.JPG")
PeterPic = pygame.transform.scale(PeterPic, (400, 400))
AndrewPic = pygame.image.load("AndrewPark.jpeg")
AndrewPic = pygame.transform.scale(AndrewPic, (515, 386))
AndrewPic = pygame.transform.rotate(AndrewPic, 180)
KimFinger = pygame.image.load("kimfinger.jpg")
KimSmile = pygame.image.load("kimsmile.jpg")
KimSerious = pygame.image.load("kimserious.png")
KimSerious = pygame.transform.scale(KimSerious, (273, 374))
redButton = pygame.image.load("Button.png")
smallbomb = pygame.image.load("smallbomb.jpg")

# run code
if __name__ == '__main__':
    running = True
    pygame.init()
    screen = pygame.display.set_mode((1200, 650))
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()

    clicksound = pygame.mixer.Sound("click.wav")
    nukesound = pygame.mixer.Sound("nukesound.wav")

    font = pygame.font.SysFont("comicsansms", 35)

    rectx = 475
    recty = 250
    rectchangex = 5
    rectchangey = 5
    pygame.draw.rect(screen, BLACK, [rectx, recty, 250, 151], 2)  # selection screen
    pygame.display.set_caption("Mine Sweeper Feat. Kim Jong Un")
    mainScreen()
