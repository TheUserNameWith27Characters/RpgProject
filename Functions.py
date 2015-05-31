from random import *
from Sounds import *
from Fonts_And_Colours import *
from Enemies import *
import pygame
pygame.init()
def collision(sprite1,sprite2):
    if pygame.sprite.collide_rect(sprite1,sprite2):
        pixels1=[]
        pixels2=[]
        for x in range(sprite1.rect.width):
            for y in range(sprite1.rect.width):
                pixels1.append((x,y,sprite1.rect.x+x,sprite1.rect.y+y))
        for x in range(sprite2.rect.width):
            for y in range(sprite2.rect.width):
                pixels2.append((x,y,sprite2.rect.x+x,sprite2.rect.y+y))
        for pixel1 in pixels1:
            for pixel2 in pixels2:
                if pixel1[2]==pixel2[2] and pixel1[3]==pixel2[3] and sprite1.image.get_at((pixel1[0],pixel1[1]))!=(255,0,255) and sprite2.image.get_at((pixel2[0],pixel2[1]))!=(255,0,255):
                    return True
    return False
def groupCollision(sprite,group):
    collided=[]
    for groupSprite in group:
        if collision(sprite,groupSprite):
            collided.append(groupSprite)
    return collided
def getColour(value):
    if value<1/3:
        return RED
    elif value<2/3:
        return YELLOW
    elif value<=1:
        return GREEN
    return RAINBOW
def mouseOver(minX,maxX,minY,maxY):
    pos=pygame.mouse.get_pos()
    return pos[0]>=minX and pos[0]<=maxX and pos[1]>=minY and pos[1]<=maxY
def critCalc(sharpness,armorRating):
    try:
        if randrange(int(sharpness*10/armorRating),101)==100:
            return 0
        return 1
    except ValueError:
        return 0
def blockCalc(shield,sharpness):
    try:
        if randrange((int(shield-sharpness)),11)==10: 
            return 0
        return 1
    except ValueError:
        return 0
def damageCalc(armorProtection,sharpness,armorRating,weaponDamage,shield):
    damage=int((weaponDamage-armorProtection*critCalc(sharpness,armorRating))*blockCalc(shield,sharpness)*uniform(0.75,1.25))
    if damage>=1:
        return damage
    return 0
def onScreen(surface):
    return surface.rect.left>=0 and surface.rect.right<=704 and surface.rect.top>=0 and surface.rect.bottom<=496
