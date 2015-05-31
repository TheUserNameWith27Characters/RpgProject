from Item_Stats import *
from Functions import *
BLACK=(0,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
GREY=(128,128,128)
BASE=(255,0,255)
RAINBOW=RED
font=pygame.font.SysFont("Comic Sans MS",50,True)
font1=pygame.font.SysFont("Comic Sans MS",18,True)
font2=pygame.font.SysFont("Comic Sans MS",10,True)
font3=pygame.font.SysFont("Comic Sans MS",25,True)
hpTitle=font1.render("HP:",1,YELLOW)
meleeTitle=font1.render("Melee:",1,YELLOW)
rangedTitle=font1.render("Ranged:",1,YELLOW)
gameOverTitle=font.render("GAME OVER",1,WHITE)
