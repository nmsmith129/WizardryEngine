#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Graphics code for Wizdrive
## by Nicholas Smith
## Copyright 2025

# In[ ]:

## Import statements

import pygame


# In[ ]:

screen = None
pointsone = "TEST"
pointstwo = None
pointsthree = None
pointsfour = None
screenHeight = 0
screenWidth = 0

# In[ ]:

def initialize():
    global screen
    global pointsone
    global pointstwo
    global pointsthree
    global pointsfour
    global screenWidth
    global screenHeight
    # initialize Pygame
    pygame.init()
    (screenWidth, screenHeight) = (800, 800)
    pointsone = ((screenWidth*.20, screenHeight*.20), (screenWidth*.80, screenHeight*.20), (screenWidth*.2, screenHeight*.8),(screenWidth*.8, screenHeight*.8))
    pointstwo = ((screenWidth*.4, screenHeight*.40), (screenWidth*.60, screenHeight*.40), (screenWidth*.4, screenHeight*.6),(screenWidth*.6, screenHeight*.6))
    pointsthree = ((screenWidth*.45, screenHeight*.45), (screenWidth*.55, screenHeight*.45), (screenWidth*.45, screenHeight*.55),(screenWidth*.55, screenHeight*.55))
    pointsfour = ((screenWidth*.455, screenHeight*.455), (screenWidth*.525, screenHeight*.455), (screenWidth*.455, screenHeight*.525),(screenWidth*.525, screenHeight*.525))

    screen = pygame.display.set_mode(size=(screenWidth, screenHeight))
    screen.fill("purple")
    pygame.display.flip()


# In[ ]:


## Draw cell for currently occupied space
def __drawZero():
    pygame.draw.line(screen, "black", (0, 0), pointsone[0])
    pygame.draw.line(screen, "black", (0, screenHeight), pointsone[2])
    pygame.draw.line(screen, "black", (screenWidth, 0), pointsone[1])
    pygame.draw.line(screen, "black", (screenWidth, screenHeight), pointsone[3])
    pygame.draw.line(screen, "black", pointsone[0], pointsone[1])
    pygame.draw.line(screen, "black", pointsone[0], pointsone[2])
    pygame.draw.line(screen, "black", pointsone[1], pointsone[3])
    pygame.draw.line(screen, "black", pointsone[2], pointsone[3])
    return

## Draw cell to left of player
def __drawZeroLeft():
    pygame.draw.line(screen, "black", pointsone[0], (0, pointsone[0][1]))
    pygame.draw.line(screen, "black", pointsone[2], (0, pointsone[2][1]))
    return

## Draw cell to right of player
def __drawZeroRight():
    pygame.draw.line(screen, "black", pointsone[1], (screenWidth, pointsone[1][1]))
    pygame.draw.line(screen, "black", pointsone[3], (screenWidth, pointsone[3][1]))
    return

## Draw cell one space ahead of player
def __drawOne():
    pygame.draw.line(screen, "black", pointsone[0], pointstwo[0])
    pygame.draw.line(screen, "black", pointsone[2], pointstwo[2])
    pygame.draw.line(screen, "black", pointsone[1], pointstwo[1])
    pygame.draw.line(screen, "black", pointsone[3], pointstwo[3])
    pygame.draw.line(screen, "black", pointstwo[0], pointstwo[1])
    pygame.draw.line(screen, "black", pointstwo[0], pointstwo[2])
    pygame.draw.line(screen, "black", pointstwo[1], pointstwo[3])
    pygame.draw.line(screen, "black", pointstwo[2], pointstwo[3])
    return

## Draw cell one left
def __drawOneLeft():
    pygame.draw.line(screen, "black", pointstwo[0], (pointsone[0][0], pointstwo[0][1]))
    pygame.draw.line(screen, "black", pointstwo[2], (pointsone[2][0], pointstwo[2][1]))
    return

## Draw cell one right
def __drawOneRight():
    pygame.draw.line(screen, "black", pointstwo[1], (pointsone[1][0], pointstwo[1][1]))
    pygame.draw.line(screen, "black", pointstwo[3], (pointsone[3][0], pointstwo[3][1]))
    return

## Draw cell two spaces ahead of player
def __drawTwo():
    pygame.draw.line(screen, "black", pointstwo[0], pointsthree[0])
    pygame.draw.line(screen, "black", pointstwo[2], pointsthree[2])
    pygame.draw.line(screen, "black", pointstwo[1], pointsthree[1])
    pygame.draw.line(screen, "black", pointstwo[3], pointsthree[3])
    pygame.draw.line(screen, "black", pointsthree[0], pointsthree[1])
    pygame.draw.line(screen, "black", pointsthree[0], pointsthree[2])
    pygame.draw.line(screen, "black", pointsthree[1], pointsthree[3])
    pygame.draw.line(screen, "black", pointsthree[2], pointsthree[3])
    return

## Draw cell two left
def __drawTwoLeft():
    pygame.draw.line(screen, "black", pointsthree[0], (pointstwo[0][0], pointsthree[0][1]))
    pygame.draw.line(screen, "black", pointsthree[2], (pointstwo[2][0], pointsthree[2][1]))
    return

## Draw cell two right
def __drawTwoRight():
    pygame.draw.line(screen, "black", pointsthree[1], (pointstwo[1][0], pointsthree[1][1]))
    pygame.draw.line(screen, "black", pointsthree[3], (pointstwo[3][0], pointsthree[3][1]))
    return


# In[ ]:


## Draw the first-person view of the current Player location and directional orientation
## based on a submitted local map

def drawView(localmap):
    __drawZero()
    if localmap[2][0]:
        __drawZeroLeft()
    if localmap[2][2]:
        __drawZeroRight()
    if localmap[1][1]:
        __drawOne()
        if localmap[1][0]:
            __drawOneLeft()
        if localmap[1][2]:
            __drawOneRight()
        if localmap[0][1]:
            __drawTwo()
            if localmap[0][0]:
                __drawTwoLeft()
            if localmap[0][2]:
                __drawTwoRight()
    pygame.display.flip()


def getEvents():
    return pygame.event.get()
    
    

