from Definitions import *
def gameReset(wallList,itemList,enemyList,player,doorList):
    wallList.empty()
    enemyList.empty()
    itemList.empty()
    doorList.empty()
    game={
            "items":[
                Item(400,75,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Staff.png")).convert(),(32,32)),"if not self.meleeClass:\n    self.currentMelee=weapons[\"Melee\"][\"Spear\"][\"Staff\"]\n    self.meleeClass=\"spear\"\n    self.meleeName=\"Staff\"\n    itemList.remove(item)"),
                Item(400,200,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Knife.png")).convert(),(32,32)),"if not self.meleeClass:\n    self.currentMelee=weapons[\"Melee\"][\"Sword\"][\"Knife\"]\n    self.meleeClass=\"sword\"\n    self.meleeName=\"Knife\"\n    itemList.remove(item)"),
                Item(400,325,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Hammer.png")).convert(),(32,32)),"if not self.meleeClass:\n    self.currentMelee=weapons[\"Melee\"][\"Hammer\"][\"Hammer\"]\n    self.meleeClass=\"hammer\"\n    self.meleeName=\"Hammer\"\n    itemList.remove(item)"),
                Item(750,75,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Bow.png")).convert(),(32,32)),"if not self.rangedClass:\n    self.currentRanged=weapons[\"Ranged\"][\"Bow\"][\"Bow\"]\n    self.rangedClass=\"bow\"\n    self.rangedName=\"Bow\"\n    itemList.remove(item)"),
                Item(750,200,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Musket.png")).convert(),(32,32)),"if not self.rangedClass:\n    self.currentRanged=weapons[\"Ranged\"][\"Gun\"][\"Musket\"]\n    self.rangedClass=\"gun\"\n    self.rangedName=\"Musket\"\n    itemList.remove(item)"),
                Item(750,325,True,pygame.transform.scale(pygame.image.load(path.join("Sprites" ,"Fireball.png")).convert(),(32,32)),"if not self.rangedClass:\n    self.currentRanged=weapons[\"Ranged\"][\"Magic\"][\"Fireball\"]\n    self.rangedClass=\"magic\"\n    self.rangedName=\"Fireball\"\n    itemList.remove(item)")
            ],"walls":[
                Wall(-5000,-5000,"Rock.png")
            ],"enemies":[
                Star(500,300,player,0)
            ],"doors":[
                Door(1008,192,-5000,-5000,"Blue_Dungeon_Door_Right.png")
            ]
        }
    for wall1 in range(0,4):
        for wall2 in range(0,9):
            game["walls"].append(Wall(-3618+wall1*64,-5064-wall2*64,"Water.png"))
    for wall in range(-1,8):
        game["walls"].append(Wall(-64,64*wall,"Blue_Dungeon_Block.png"))
    for wall in range(-1,3):
        game["walls"].append(Wall(1024,wall*64,"Blue_Dungeon_Block.png"))
        game["walls"].append(Wall(1024,wall*64+320,"Blue_Dungeon_Block.png"))
    for wall in range(0,16):
        game["walls"].append(Wall(wall*64,-64,"Blue_Dungeon_Block.png"))
        game["walls"].append(Wall(wall*64,448,"Blue_Dungeon_Block.png"))
    for wall1 in range(0,11):
        for wall2 in range(0,10):
            game["walls"].append(Wall(-4322+wall1*64,-5000-wall2*64,"Water.png"))
    for wall in range(0,5):
        game["walls"].append(Wall(-4368,-5192-wall*64,"Water.png"))
    for wall in range(0,7):
        game["walls"].append(Wall(-4258+wall*64,-4936,"Water.png"))
    for wall in game["walls"]:
        wallList.add(wall)
    for item in game["items"]:
        itemList.add(item)
    for enemy in game["enemies"]:
        enemyList.add(enemy)
    for door in game["doors"]:
        doorList.add(door)
class Player(pygame.sprite.Sprite):
    effects=[0,0,0,0,0,0,0,0,0,0,0,0]
    armor=None
    shield=None
    currentMelee=weapons["Melee"]["Null"]
    meleeName="???"
    currentRanged=weapons["Ranged"]["Null"]
    rangedName="???"
    ranged=None
    accessory=None
    spriteDelay=False
    maxSpeed=3
    speed=3
    hp=25
    maxHp=25
    newHp=False
    xChange=0
    yChange=0
    level=1
    xp=0
    attackBase=0
    defenseBase=0
    defense=0
    defensive=0
    armorRating=1
    blockBase=0
    rightCounter=0
    leftCounter=0
    upCounter=0
    downCounter=0
    meleeClass=""
    rangedClass=""
    facing="down"
    meleeAttackCooldown=0
    rangedAttackCooldown=0
    knockback=[]
    knockbackCounter=0
    worldXChange=0
    worldYChange=0
    canMove=True
    left=False
    right=False
    up=False
    down=False
    isMelee=False
    isRanged=False
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(path.join("Sprites" ,"Player_Down.png")).convert()
        self.image.set_colorkey(BASE)
        self.rect=self.image.get_rect()
        self.rect.x=25
        self.rect.y=200
        self.meleeWeapon=self.MeleeWeapon()
        self.rangedWeapon=self.RangedWeapon()
    def goUp(self):
        self.up=True
        self.left=False
        self.right=False
        self.down=False
    def goLeft(self):
        self.left=True
        self.down=False
        self.right=False
        self.up=False
    def goRight(self):
        self.right=True
        self.left=False
        self.down=False
        self.up=False
    def goDown(self):
        self.down=True
        self.left=False
        self.right=False
        self.up=False
    def worldChange(self,wallList,enemyList,itemList,backgroundList,doorList):
        if self.rect.x<=55:
            diff=self.rect.x-55
            self.rect.x=55
            for wall in wallList:
                wall.rect.x-=diff
            for enemy in enemyList:
                enemy.rect.x-=diff
            for item in itemList:
                item.rect.x-=diff
            for background in backgroundList:
                background.rect.x-=diff
            for door in doorList:
                door.rect.x-=diff
            self.worldXChange+=diff
        elif self.rect.x>=619:
            diff=self.rect.x-619
            self.rect.x=619
            for wall in wallList:
                wall.rect.x-=diff
            for enemy in enemyList:
                enemy.rect.x-=diff
            for item in itemList:
                item.rect.x-=diff
            for background in backgroundList:
                background.rect.x-=diff
            for door in doorList:
                door.rect.x-=diff
            self.worldXChange+=diff
        if self.rect.y<=63:
            diff=self.rect.y-63
            self.rect.y=63
            for wall in wallList:
                wall.rect.y-=diff
            for enemy in enemyList:
                enemy.rect.y-=diff
            for item in itemList:
                item.rect.y-=diff
            for background in backgroundList:
                background.rect.y-=diff
            for door in doorList:
                door.rect.y-=diff
            self.worldYChange+=diff
        elif self.rect.y>=400:
            diff=self.rect.y-400
            self.rect.y=400
            for wall in wallList:
                wall.rect.y-=diff
            for enemy in enemyList:
                enemy.rect.y-=diff
            for item in itemList:
                item.rect.y-=diff  
            for background in backgroundList:
                background.rect.y-=diff
            for door in doorList:
                door.rect.y-=diff
            self.worldYChange+=diff
    def update(self,wallList,itemList,enemyList,weaponLists,backgroundList,doorList):
        if self.spriteDelay:
            self.spriteDelay=False
            self.setSprite()
        if self.effects[0]:
            self.effects[0]-=1
            self.hp-=self.maxHp*3/4000
        if self.effects[3]:
            self.effects[3]-=1
            self.block=0
        else:
            self.block=self.blockBase
        if self.effects[6]:
            self.effects[6]-=1
            self.speed=0
        else:
            self.speed=self.maxSpeed
        if self.effects[7]:
            self.effects[7]-=1
            self.defense=self.defensive/2
        else:
            self.defense=self.defensive
        if self.effects[8]:
            self.effects[8]-=1
            self.speed=self.maxSpeed/2
        else:
            self.speed=self.maxSpeed
        if self.effects[10]:
            self.effects[10]-=1
            if self.effects[8]:
                self.speed=self.maxSpeed*3/8
            else:
                self.speed=self.maxSpeed*3/4
            if self.effects[7]:
                self.defense=self.defensive*3/8
            else:
                self.defense=self.defensive*3/4
        else:
            self.speed=self.maxSpeed
            self.defense=self.defensive
        if self.effects[1]:
            self.effects[1]-=1
        if not self.knockback or randrange(0,601)==600:
            if self.effects[1]:
                if self.right or self.left or self.up or self.down:
                    chosen=choice(["x+","y+","x-","y-"])
                    exec("self.rect."+chosen+"=self.speed")
                    if chosen=="x+":
                        self.rightCounter+=1
                        self.facing="right"
                    elif chosen=="y+":
                        self.downCounter+=1
                        self.facing="down"
                    elif chosen=="x-":
                        self.leftCounter+=1
                        self.facing="left"
                    elif chosen=="y-":
                        self.upCounter+=1
                        self.facing="up"
            else:
                if self.right:
                    self.rect.x+=self.speed
                    self.rightCounter+=1
                    self.facing="right"
                elif self.left:
                    self.rect.x-=self.speed
                    self.leftCounter+=1
                    self.facing="left"
                elif self.up:
                    self.rect.y-=self.speed
                    self.upCounter+=1
                    self.facing="up"
                elif self.down:
                    self.rect.y+=self.speed
                    self.downCounter+=1
                    self.facing="down"
        if self.effects[2]:
            self.effects[2]-=1        
        reseted=False
        if self.isMelee:
            self.meleeAttackCooldown-=0.1
            if self.meleeAttackCooldown<=0:
                self.reset(weaponLists,True)
                reseted=True
                self.isMelee=False
        if self.isRanged:
            self.rangedAttackCooldown-=0.1
            if self.rangedAttackCooldown<=0 and not reseted:
                self.reset(weaponLists,True,True)
                self.isRanged=False
        if not self.effects[0]:
            self.hp+=1/300
        if type(self.canMove)==int:
            self.canMove-=1
            if self.canMove==0:
                self.canMove=True
        if self.canMove==True:
            self.setSprite()
        blockHitList=pygame.sprite.spritecollide(self,wallList,False)
        for block in blockHitList:
            if self.facing=="up":
                self.rect.top=block.rect.bottom
            elif self.facing=="down":
                self.rect.bottom=block.rect.top
            elif self.facing=="right":
                self.rect.right=block.rect.left
            else:
                self.rect.left=block.rect.right
            self.knockback=[]
        if self.knockback:
            exec("self.rect."+self.knockback[1]+self.knockback[0]+"=8")
            self.knockbackCounter-=8
            if self.knockbackCounter<=0:
                self.knockback=[]
        for item in pygame.sprite.spritecollide(self,itemList,False):
            if item.pickupAble:
                exec(item.code)
        if self.xp>=self.level*50:
            self.levelUp()
        if self.hp>self.maxHp:
            self.hp=self.maxHp
        if self.newHp:
            if self.newHp>self.hp:
                self.hp+=1
                if self.newHp<self.hp:
                    self.hp=self.newHp
                    self.newHp=False
            elif self.newHp<self.hp:
                self.hp-=1
                if self.newHp>self.hp:
                    self.hp=self.newHp
                    self.newHp=False
        self.meleeWeapon.update(self)
        self.rangedWeapon.update(self)
        self.worldChange(wallList,enemyList,itemList,backgroundList,doorList)
    def levelUp(self):
        self.level+=1
        self.newHp=self.maxHp
        self.xp=0
        self.meleeAttackCooldown=0
        self.rangedAttackCooldown=0
        levelUpTitle=font.render("LEVEL UP!",1,YELLOW)
        screen.blit(levelUpTitle,(225,250))
        pygame.display.flip()
        sleep(2)
        if self.level>=10 and self.currentMelee["level"]==1:
            screen.fill(WHITE)
            if self.meleeName=="Staff":
                option1=(weapons["Melee"]["Spear"]["Spear"],"Spear")
                option2=(weapons["Melee"]["Spear"]["Scythe"],"Scythe")
            elif self.meleeName=="Knife":
                option1=(weapons["Melee"]["Sword"]["Short Sword"],"Short Sword")
                option2=(weapons["Melee"]["Sword"]["Long Sword"],"Long Sword")
            else:
                option1=(weapons["Melee"]["Hammer"]["Axe"],"Axe")
                option2=(weapons["Melee"]["Hammer"]["Facial Reconstructor"],"Facial Reconstructor")
                option3=(weapons["Melee"]["Hammer"]["Mace"],"Mace")
            weaponSelectTitle=font.render("CHOOSE YOUR UPGRADE!",1,YELLOW)
            screen.blit(weaponSelectTitle,(25,200))
            if self.meleeName=="Staff"or self.meleeName=="Knife":
                img1=option1[0]["sprite"].convert()
                img2=option2[0]["sprite"].convert()
                img1.set_colorkey(BASE)
                img2.set_colorkey(BASE)
                screen.blit(img1,(200,300))
                screen.blit(img2,(500,300))
                selected=False
                pygame.display.flip()
                while not selected:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if mouseOver(200,264,300,364):
                                self.currentMelee=option1[0]
                                self.meleeName=option1[1]
                                selected=True
                            elif mouseOver(500,564,300,364):
                                self.currentMelee=option2[0]
                                self.meleeName=option2[1]
                                selected=True
            else:
                img1=option1[0]["sprite"].convert()
                img2=option2[0]["sprite"].convert()
                img3=option3[0]["sprite"].convert()
                img1.set_colorkey(BASE)
                img2.set_colorkey(BASE)
                img3.set_colorkey(BASE)
                screen.blit(img1,(154,300))
                screen.blit(img2,(318,300))
                screen.blit(img3,(472,300))
                selected=False
                pygame.display.flip()
                while not selected:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if mouseOver(154,218,300,364):
                                self.currentMelee=option1[0]
                                self.meleeName=option1[1]
                                selected=True
                            elif mouseOver(318,382,300,364):
                                self.currentMelee=option2[0]
                                self.meleeName=option2[1]
                                selected=True
                            elif mouseOver(472,536,300,364):
                                self.currentMelee=option3[0]
                                self.meleeName=option3[1]
                                selected=True
        if self.level>=15 and self.currentRanged["level"]==1:
            screen.fill(WHITE)
            if self.rangedName=="Bow":
                option1=(weapons["Ranged"]["Bow"]["Long Bow"],"Long Bow")
                option2=(weapons["Ranged"]["Bow"]["Crossbow"],"Crossbow")
            elif self.rangedName=="Musket":
                option1=(weapons["Ranged"]["Gun"]["Mini Cannon"],"Mini Cannon")
                option2=(weapons["Ranged"]["Gun"]["Rifle"],"Rifle")
            else:
                option1=(weapons["Ranged"]["Magic"]["Snowball"],"Snowball")
                option2=(weapons["Ranged"]["Magic"]["Flame Staff"],"Flame Staff")
            weaponSelectTitle=font.render("CHOOSE YOUR UPGRADE!",1,YELLOW)
            screen.blit(weaponSelectTitle,(25,200))
            img1=option1[0]["sprite"].convert()
            img2=option2[0]["sprite"].convert()
            img1.set_colorkey(BASE)
            img2.set_colorkey(BASE)
            screen.blit(img1,(200,300))
            screen.blit(img2,(500,300))
            selected=False
            pygame.display.flip()
            while not selected:
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if mouseOver(200,264,300,364):
                            self.currentRanged=option1[0]
                            self.rangedName=option1[1]
                            selected=True
                        elif mouseOver(500,564,300,364):
                            self.currentRanged=option2[0]
                            self.rangedName=option2[1]
                            selected=True
        if self.level>=20 and self.currentMelee["level"]==2:
            if self.meleeName=="Spear"or self.meleeName=="Long Sword":
                screen.fill(WHITE)
                if self.meleeName=="Spear":
                    option1=(weapons["Melee"]["Spear"]["Trident"],"Trident")
                    option2=(weapons["Melee"]["Spear"]["Royal Guard"],"Royal Guard")
                else:
                    option1=(weapons["Melee"]["Sword"]["Heavy Broadsword"],"Heavy Broadsword")
                    option2=(weapons["Melee"]["Sword"]["Dual Bladed Sword"],"Dual Bladed Sword")
                img1=option1[0]["sprite"].convert()
                img2=option2[0]["sprite"].convert()
                img1.set_colorkey(BASE)
                img2.set_colorkey(BASE)
                screen.blit(img1,(200,300))
                screen.blit(img2,(500,300))
                selected=False
                pygame.display.flip()
                while not selected:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if mouseOver(200,264,300,364):
                                self.currentMelee=option1[0]
                                self.meleeName=option1[1]
                                selected=True
                            elif mouseOver(500,564,300,364):
                                self.currentMelee=option2[0]
                                self.meleeName=option2[1]
                                selected=True
            else:
                if self.meleeName=="Scythe":
                    self.currentMelee=weapons["Melee"]["Spear"]["Reaper"]
                    self.meleeName="Reaper"
                elif self.meleeName=="Short Sword":
                    self.currentMelee=weapons["Melee"]["Sword"]["Fire Sword"]
                    self.meleeName="Fire Sword"
                elif self.meleeName=="Axe":
                    self.currentMelee=weapons["Melee"]["Hammer"]["War Axe"]
                    self.meleeName="War Axe"
                elif self.meleeName=="Facial Reconstructor":
                    self.currentMelee=weapons["Melee"]["Hammer"]["Mjolnir"]
                    self.meleeName="Mjolnir"
                elif self.meleeName=="Mace":
                    self.currentMelee=weapons["Melee"]["Hammer"]["Flail"]
                    self.meleeName="Flail"
        if self.level>=30 and self.meleeName=="Fire Sword":
            self.currentMelee=weapons["Melee"]["Sword"]["Energy Sword"]
            self.meleeName="Energy Sword"
    def reset(self,weaponLists,isHit,ranged=False):
        if not ranged:
            for weaponList in weaponLists:
                weaponList.empty()
        self.canMove=True
        if isHit:
            self.meleeAttackCooldown=0
            self.rangedAttackCooldown=0
        self.spriteDelay=True
    def setSprite(self):
        if self.facing=="right":
            if self.rightCounter%16>=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Right1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Right2.png")).convert()
        elif self.facing=="left":
            if self.leftCounter%16>=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Left1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Left2.png")).convert()
        elif self.facing=="up":
            if self.upCounter%16<=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Up1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Up2.png")).convert()
        else:
            if self.downCounter%16>=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Down1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Player_Down2.png")).convert()
    def death(self,wallList,itemList,enemyList,weaponLists,backgroundList,doorList):
        self.currentMelee=weapons["Melee"]["Null"]
        self.currentRanged=weapons["Ranged"]["Null"]
        self.meleeName="???"
        self.rangedName="???"
        self.meleeClass=""
        self.rangedClass=""
        self.facing="down"
        self.down=False
        self.right=False
        self.up=False
        self.left=False
        self.newHp=25
        self.rect.x=100
        self.rect.y=100
        for weaponList in weaponLists:
            weaponList.empty()
        for background in backgroundList:
            background.rect.x+=self.worldXChange
            background.rect.y+=self.worldYChange
        self.worldXChange=0
        self.worldYChange=0
        gameReset(wallList,itemList,enemyList,self,doorList)
    class MeleeWeapon():
        def update(self,player):
            if player.currentMelee:
                if player.effects[8]:
                    self.damage=(player.currentMelee["damage"]+player.attackBase+player.level)/2
                else:
                    self.damage=player.currentMelee["damage"]+player.attackBase+player.level
                self.attackRange=player.currentMelee["range"]
                self.speed=player.currentMelee["speed"]
                self.tag=player.currentMelee["tag"]
                self.knockback=player.currentMelee["knockback"]*8+player.level
                self.sprite=player.currentMelee["sprite"].convert()
                self.sharpness=player.currentMelee["sharpness"]+int(player.level/5)
                self.effect=player.currentMelee["effect"]
                self.sprite.set_colorkey(BASE)
                if player.effects[10]:
                    if player.effects[8]:
                        self.damage=(player.currentMelee["damage"]+player.attackBase+player.level)*3/8
                    else:
                        self.damage=(player.currentMelee["damage"]+player.attackBase+player.level)*3/4
                else:
                    self.damage=player.currentMelee["damage"]+player.attackBase+player.level
        def attack(self,weaponList,player):
            if not player.effects[2]:
                player.right=False
                player.left=False
                player.up=False
                player.down=False
                player.isMelee=True
                if player.facing=="right":
                    weapon=Weapon(player.rect.x+24,player.rect.y,self.attackRange*4,32,self.damage,weaponList,self.sharpness,player.facing,self.knockback,self.effect)
                    if player.meleeClass=="spear":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right4.png")).convert()
                    elif player.meleeClass=="sword":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right3.png")).convert()
                    else:
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right5.png")).convert()
                elif player.facing=="left":
                    weapon=Weapon(player.rect.x,player.rect.y,self.attackRange*4,32,self.damage,weaponList,self.sharpness,player.facing,self.knockback,self.effect)
                    if player.meleeClass=="spear":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left4.png")).convert()
                    elif player.meleeClass=="sword":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left3.png")).convert()
                    else:
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left5.png")).convert()
                elif player.facing=="up":
                    weapon=Weapon(player.rect.x,player.rect.y,32,self.attackRange*4,self.damage,weaponList,self.sharpness,player.facing,self.knockback,self.effect)
                    player.image=pygame.image.load(path.join("Sprites" ,"Player_Up3.png")).convert()
                else:
                    weapon=Weapon(player.rect.x,player.rect.y+26,32,self.attackRange*4,self.damage,weaponList,self.sharpness,player.facing,self.knockback,self.effect)
                    if player.meleeClass=="spear":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down4.png")).convert()
                    elif player.meleeClass=="sword":
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down3.png")).convert()
                    else:
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down5.png")).convert()
                player.meleeAttackCooldown=self.speed
                player.canMove=30
    class RangedWeapon():
        def update(self,player):
            self.damage=player.currentRanged["damage"]+player.level
            self.speed=player.currentRanged["speed"]
            self.tag=player.currentRanged["tag"]
            self.effect=player.currentRanged["effect"]
            self.velocity=player.currentRanged["velocity"]
            self.knockback=player.currentRanged["knockback"]*8
            self.sprite=player.currentRanged["sprite"].convert()
            self.sharpness=player.currentRanged["sharpness"]+int(player.level/5)
            self.sprite.set_colorkey(BASE)
        def attack(self,weaponList,player):
            if not player.effects[2]:
                player.right=False
                player.left=False
                player.up=False
                player.down=False
                player.isRanged=True
                if player.facing=="right":
                    if player.rangedClass=="bow":
                        weapon=Projectile(player.rect.x+24,player.rect.y+16,self.damage,weaponList,self.sharpness,"right",self.knockback,self.effect,self.velocity,"Arrow_Right.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right6.png")).convert()
                        if player.rangedName=="Multi Bow":
                            otherWeapon=Projectile(player.rect.x+18,player.rect.y,self.damage/2,weaponList,self.sharpness,"right",self.knockback/2,self.effect,self.velocity,"Arrow_Right.png",True)
                            otherOtherWeapon=Projectile(player.rect.x+18,player.rect.y+32,self.damage/2,weaponList,self.sharpness,"right",self.knockback/2,self.effect,self.velocity,"Arrow_Right.png",True)
                    elif player.rangedClass=="gun":
                        weapon=Projectile(player.rect.x+24,player.rect.y+16,self.damage,weaponList,self.sharpness,"right",self.knockback,self.effect,self.velocity,"Bullet_Right.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right7.png")).convert()
                    else:
                        weapon=Projectile(player.rect.x+24,player.rect.y+16,self.damage,weaponList,self.sharpness,"right",self.knockback,self.effect,self.velocity,"Magic_Projectile.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Right8.png")).convert()
                elif player.facing=="left":
                    if player.rangedClass=="bow":
                        weapon=Projectile(player.rect.x,player.rect.y+16,self.damage,weaponList,self.sharpness,"left",self.knockback,self.effect,self.velocity,"Arrow_Left.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left6.png")).convert()
                        if player.rangedName=="Multi Bow":
                            otherWeapon=Projectile(player.rect.x-10,player.rect.y,self.damage/2,weaponList,self.sharpness,"left",self.knockback/2,self.effect,self.velocity,"Arrow_Left.png",True)
                            otherOtherWeapon=Projectile(player.rect.x-10,player.rect.y+32,self.damage/2,weaponList,self.sharpness,"left",self.knockback/2,self.effect,self.velocity,"Arrow_Left.png",True)
                    elif player.rangedClass=="gun":
                        weapon=Projectile(player.rect.x,player.rect.y+16,self.damage,weaponList,self.sharpness,"left",self.knockback,self.effect,self.velocity,"Bullet_Left.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left7.png")).convert()
                    else:
                        weapon=Projectile(player.rect.x,player.rect.y+16,self.damage,weaponList,self.sharpness,"left",self.knockback,self.effect,self.velocity,"Magic_Projectile.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Left8.png")).convert()
                elif player.facing=="up":
                    if player.rangedClass=="bow":
                        weapon=Projectile(player.rect.x+16,player.rect.y+4,self.damage,weaponList,self.sharpness,"up",self.knockback,self.effect,self.velocity,"Arrow_Up.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Up3.png")).convert()
                        if player.rangedName=="Multi Bow":
                            otherWeapon=Projectile(player.rect.x,player.rect.y-2,self.damage/2,weaponList,self.sharpness,"up",self.knockback/2,self.effect,self.velocity,"Arrow_Up.png",True)
                            otherOtherWeapon=Projectile(player.rect.x+32,player.rect.y-2,self.damage/2,weaponList,self.sharpness,"up",self.knockback/2,self.effect,self.velocity,"Arrow_Up.png",True)
                    elif player.rangedClass=="gun":
                        weapon=Projectile(player.rect.x+16,player.rect.y+4,self.damage,weaponList,self.sharpness,"up",self.knockback,self.effect,self.velocity,"Bullet_Up.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Up3.png")).convert()
                    else:
                        weapon=Projectile(player.rect.x+16,player.rect.y+4,self.damage,weaponList,self.sharpness,"up",self.knockback,self.effect,self.velocity,"Magic_Projectile.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Up3.png")).convert()
                else:
                    if player.rangedClass=="bow":
                        weapon=Projectile(player.rect.x+16,player.rect.y+36,self.damage,weaponList,self.sharpness,"down",self.knockback,self.effect,self.velocity,"Arrow_Down.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down6.png")).convert()
                        if player.rangedName=="Multi Bow":
                            otherWeapon=Projectile(player.rect.x,player.rect.y+30,self.damage/2,weaponList,self.sharpness,"down",self.knockback/2,self.effect,self.velocity,"Arrow_Down.png",True)
                            otherOtherWeapon=Projectile(player.rect.x+32,player.rect.y+30,self.damage/2,weaponList,self.sharpness,"down",self.knockback/2,self.effect,self.velocity,"Arrow_Down.png",True)
                    elif player.rangedClass=="gun":
                        weapon=Projectile(player.rect.x+16,player.rect.y+36,self.damage,weaponList,self.sharpness,"down",self.knockback,self.effect,self.velocity,"Bullet_Down.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down7.png")).convert()
                    else:
                        weapon=Projectile(player.rect.x+16,player.rect.y+36,self.damage,weaponList,self.sharpness,"down",self.knockback,self.effect,self.velocity,"Magic_Projectile.png")
                        player.image=pygame.image.load(path.join("Sprites" ,"Player_Down8.png")).convert()
                player.rangedAttackCooldown=self.speed
                player.canMove=30
