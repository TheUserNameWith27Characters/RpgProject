from time import *
from math import *
from Enemies import *
screen=pygame.display.set_mode((704,596))
pygame.display.set_caption("The RPG Alpha")
clock=pygame.time.Clock()
hud=pygame.Surface()
statuses=[[pygame.image.load(path.join("Sprites" ,"Burn_Status.png")),"Burn: Gradually deals damage."],
[pygame.image.load(path.join("Sprites" ,"Stun_Status.png")),"Stun: Disorients movement."],
[pygame.image.load(path.join("Sprites" ,"Electricity_Status.png")),"Electricity: Cannot attack."],
[pygame.image.load(path.join("Sprites" ,"Broken_Shield_Status.png")),"Broken Shield: Self explanatory."],
[pygame.image.load(path.join("Sprites" ,"Blinded_Status.png")),"Blinded: Cannot see."],
[pygame.image.load(path.join("Sprites" ,"Toxic_Status.png")),"Toxic: Deals damage and reduces healing effects."],
[pygame.image.load(path.join("Sprites" ,"Goo_Status.png")),"Goo: Cannot move."],
[pygame.image.load(path.join("Sprites" ,"Acid_Status.png")),"Acid: Defense is reduced."],
[pygame.image.load(path.join("Sprites" ,"Frozen_Status.png")),"Frozen: Attack damage and movement speed are reduced. (Stop singing Let It Go...)"],
[pygame.image.load(path.join("Sprites" ,"Darkness_Status.png")),"Darkness: HUD cannot be seen."],
[pygame.image.load(path.join("Sprites" ,"Drowzy_Status.png")),"Drowzy: Attack damage,movement speed and defense are reduced."],
[pygame.image.load(path.join("Sprites" ,"Magic'd_Status.png")),"Magic'd: Screen is flipped"]]
for effect in statuses:
    effect[0]=effect[0].convert()
    effect[0].set_colorkey(BASE)
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        super().__init__()
        self.image=pygame.image.load(path.join("Sprites",sprite)).convert()
        self.rect=self.image.get_rect()
        self.image.set_colorkey(BASE)
        self.rect.y=y
        self.rect.x=x
class Item(pygame.sprite.Sprite):
    def __init__(self,x,y,pickup,sprite,code):
        super().__init__()
        self.pickupAble=pickup
        self.image=sprite
        self.image.set_colorkey(BASE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.code=code
class Weapon(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,damage,weaponList,sharpness,facing,knockback,effect):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.damage=damage
        self.sharpness=sharpness
        self.timer=15
        self.facing=facing
        self.knockback=knockback
        self.effect=effect
        self.projectile=False
        pygame.draw.rect(screen,RED,(x,y,width,height))
        weaponList.add(self)
    def update(self,weaponLists,enemyList,player,unused):
        enemyHitList=pygame.sprite.spritecollide(self,enemyList,False)
        for enemy in enemyHitList:
            enemy.hp-=damageCalc(enemy.defense,self.sharpness,2,self.damage,enemy.block)
            if self.facing=="right":
                enemy.knockback=["+","x"]
            elif self.facing=="left":
                enemy.knockback=["-","x"]
            elif self.facing=="up":
                enemy.knockback=["-","y"]
            else:
                enemy.knockback=["+","y"]
            enemy.knockbackCounter=self.knockback
            if self.effect:
                if random()<=self.effect["effectChance"]:
                    enemy.effects[self.effect["id"]]=self.effect["duration"]*30
        if enemyHitList:
            player.reset(weaponLists,False,self.projectile)
            self.timer=0
            if self.projectile:
                self.kill()
        self.timer-=1
        if self.timer<=0:
            if not self.projectile:
                self.kill()
            player.spriteDelay=True
class Projectile(Weapon):
    def __init__(self,x,y,damage,weaponList,sharpness,facing,knockback,effect,velocity,sprite,small=False):
        super().__init__(x,y,1,1,damage,weaponList,sharpness,facing,knockback,effect)
        self.image=pygame.image.load(path.join("Sprites",sprite)).convert()
        self.image.set_colorkey(BASE)
        self.rect=self.image.get_rect()
        if small:
            self.image=pygame.transform.scale(self.image,(int(self.rect.width*3/4),int(self.rect.height*3/4)))
        self.rect.x=x
        self.rect.y=y
        self.velocity=velocity
        self.projectile=True
    def update(self,weaponLists,enemyList,player,wallList):
        if self.facing=="right":
            self.rect.x+=self.velocity
        elif self.facing=="left":
            self.rect.x-=self.velocity
        elif self.facing=="up":
            self.rect.y-=self.velocity
        else:
            self.rect.y+=self.velocity
        super().update(weaponLists,enemyList,player,wallList)
        if not onScreen(self)or pygame.sprite.spritecollide(self,wallList,False):
            self.kill()
class Door(pygame.sprite.Sprite):
    def __init__(self,x,y,tpX,tpY,sprite):
        super().__init__()
        self.image=pygame.image.load(path.join("Sprites",sprite)).convert()
        self.image.set_colorkey(BASE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.tpX=tpX
        self.tpY=tpY
    def update(self,player):
        if collide(self,player):
            player.rect.x=self.tpX
            player.rect.y=self.tpY
class Background(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        super().__init__()
        self.image=pygame.image.load(path.join("Sprites",sprite)).convert()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
class Animation(pygame.sprite.Sprite):
    def __init__(self,x,y,duration,speed,*sprites):
        super().__init__()
        self.speed=speed*30
        self.spriteCooldown=self.speed
        self.duration=duration*30
        self.sprites=[]
        for sprite in sprites:
            realSprite=pygame.image.load(path.join("Sprites",sprite)).convert()
            realSprites.set_colorkey(BASE)
            self.sprites.append(realSprite)
        self.currentSprite=0
        self.image=self.sprites[0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self):
        self.spriteCooldown-=1
        if not self.spriteCooldown:
            self.spriteCooldown=self.speed
            self.currentSprite+=1
            self.image=self.sprites[self.currentSprite]
        self.duration-=1
        if not self.duration:
            self.kill()
