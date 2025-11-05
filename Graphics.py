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
print(pointsone)
# In[ ]:

def initialize(startermap):
    global screen
    global pointsone
    global pointstwo
    global pointsthree
    global pointsfour
    # initialize Pygame
    pygame.init()
    (width, height) = (1280, 720)
    pointsone = ((width*.20, height*.20), (width*.80, height*.20), (width*.2, height*.8),(width*.8, height*.8))
    pointstwo = ((width*.4, height*.40), (width*.60, height*.40), (width*.4, height*.6),(width*.6, height*.6))
    pointsthree = ((width*.45, height*.45), (width*.55, height*.45), (width*.45, height*.55),(width*.55, height*.55))
    pointsfour = ((width*.455, height*.455), (width*.525, height*.455), (width*.455, height*.525),(width*.525, height*.525))

    screen = pygame.display.set_mode(size=(width, height))
    screen.fill("purple")
    pygame.display.flip()


# In[ ]:


## Draw cell for currently occupied space
def __drawZero():
    pygame.draw.line(screen, "black", (0, 0), Graphics.pointsone[0])
    pygame.draw.line(screen, "black", (0, height), pointsone[2])
    pygame.draw.line(screen, "black", (width, 0), pointsone[1])
    pygame.draw.line(screen, "black", (width, height), pointsone[3])
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
    pygame.draw.line(screen, "black", pointsone[1], (width, pointsone[1][1]))
    pygame.draw.line(screen, "black", pointsone[3], (width, pointsone[3][1]))
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
        __drawLeft()
    if localmap[2][2]:
        __drawRight()
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
    
    

