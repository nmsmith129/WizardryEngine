#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Code for running Wizardry-esque early dungeon crawl games
## by Nicholas Smith
## Copyright (c) 2025


# In[ ]:


## import statements go here
import io
import sys
import WizdriveGraphics
import


# In[ ]:


## Global constants

TEXTMAP = ((1,1,1), (0,1,0), (1,1,1))

## Global variables

currentmap = None                                   # Current level map
savefile = None                                     # Current loaded save file
enemies = []                                        # List of all enemy Things
items = []                                          # List of all item Things
VALID_FAMILIES = ['player','enemy','item']           # list of all Thing families in game
VALID_TYPES = []                                     # List of all Thing types


# In[ ]:


## Main launch method

# def main():
#     # Load map from absolute path and initialize with enemies, items, and player
#     mapfile = input("Enter absolute path of map file to load: ")
#     load_map(mapfile)

#     # Begin main game loop
#     game_loop()

# def main():
def main():
    global currentmap
    currentmap = TEXTMAP
    Graphics.initialize(currentmap)
    game_loop()
    return


# In[ ]:


## Load current map into memory from disk

def load_map(mapfile):
    mapfile = open("mapfile.csv", "r", encoding="utf-8")
    try:
        teststring = mapfile.readline()
        if teststring != "Wizdrive map":
            raise ValueError("Loaded file was not a valid map.")
    except Exception as e:
        print(e)
        

    return


# In[ ]:


## Main game loop

def game_loop():
    # Draw the player view
    # Poll continuously for keyboard keys
    # When one is found, parse it and perform the action
    # Enemies take turns
    # Repeat
    return


# In[ ]:


## Draw the segmented false-3d first-person player view

def draw_view():
    return


# In[ ]:


## Move player one space forward, left, right, or back relative to the current facing direction if possible

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
    main()

