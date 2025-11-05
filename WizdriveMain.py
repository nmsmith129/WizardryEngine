#!/usr/bin/env python
# coding: utf-8

# In[5]:


## Code for running Wizardry-esque early dungeon crawl games
## by Nicholas Smith
## Copyright (c) 2025


# In[ ]:


## import statements go here
import Graphics
import io
import os
import sys
import pygame


# In[ ]:


## Global constants

WALL    = 0b0
ROOM    = 0b1
VISITED = 0b10
PLAYER  = 0b100
ENEMY   = 0b1000
ITEM    = 0b10000

## Global variables

width = 0
height = 0
currentmap = None                                   # Current level map
savefile = None                                     # Current loaded save file
playerfacing = 0                                    # Direction player is facing (1 for North, 2 for East, 3 for South, 4 for West)
enemies = []                                        # List of all enemy Things
items = []                                          # List of all item Things
VALID_FAMILIES = ['player','enemy','item']          # list of all Thing families in game
VALID_TYPES = ['player','enemy','item']             # List of all Thing types


# In[ ]:


## Main launch method

TEXTMAP = ((1,1,1), (0,1,0), (1,1,1))

def main():
    global currentmap
    Graphics.initialize()
    currentmap = loadMap("MovementTestLevel.lvlmap")
    playerfacing = 1
    Graphics.drawView(currentmap)
    gameLoop()
    print("All good")
    return


# In[ ]:


## Load current map into memory from disk
## Returns a Map object

def loadMap(mapfile):

    global width
    global height

    mapstream = open(mapfile, "r", encoding="utf-8")
    try:
        # Ensure the filetype is correct
        teststring = mapstream.readline()
        if teststring != "Wizdrive map\n":
            raise ValueError("Loaded file was not a valid map.")

        # Split map into a two-dimensional array
        map = mapstream.read()
        map = map.split("\n")
        map[len(map)-1].strip()
        for l, line in enumerate(map):
            map[l] = line.split(",")
    
    # Pop off first line to serve as width and height reference
        height = len(map)
        width = len(map[0])
    # Sanity check; all rows must be the length of width and there must be height rows
        for l in range(height):
            for c in range(width):
                testvar = map[l][c]
                map[l][c] = int(map[l][c])
    except Exception:
        sys.exit(1)
    return map

# In[ ]:


## Main game loop

def gameLoop():
    while True:
        Graphics.getEvents()
    # Draw the player view
    # Poll continuously for keyboard keys
    # When one is found, parse it and perform the action
    # Enemies take turns
    # Repeat
    return


# In[ ]:


## Move player one space forward, left, right, or back
## relative to the current facing direction, if possible

def move(direction):
    return


# In[ ]:


## Turn player 90 degrees to left, 90 to right, or 180 behind them

def turn(direction):
    return


# In[ ]:


## Swing with equipped weapon at square in front of player

def attack():
    return


# In[ ]:


## Pick up item on ground in the player's square and place it in inventory

def pick_up():
    return


# In[ ]:


## Program launch code
if __name__ == '__main__':
    print("Pygame works")
    main()

