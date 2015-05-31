from os import *
import pygame
pygame.init()
weapons={
    "Melee":{
        "Null":{"damage":1,"speed":1,"range":1,"effect":False,"sharpness":1,"knockback":1,"tag":"You have yet to obtain a melee weapon...","level":0,"sprite":pygame.image.load(path.join("Sprites","Null.png"))},
        "Spear":{
            "Staff":{"damage": 5,"speed":2,"range":3,"effect":False,"sharpness":2,"knockback":3,"tag":"A stick...Nothing more,nothing less.","level":1,"sprite":pygame.image.load(path.join("Sprites","Staff.png"))},
            "Spear":{"damage": 12,"speed":4,"range":4,"effect":False,"sharpness":5,"knockback":5,"tag":"This staff has a sharpened stone edge for extra piercing power.","level":2,"sprite":pygame.image.load(path.join("Sprites","Spear.png"))},
            "Royal Guard":{"damage":27,"speed":4,"range":4,"effect":False,"sharpness":8,"knockback":7,"tag":"A spear often used to defend castles.","level":3,"sprite":pygame.image.load(path.join("Sprites","Royal_Guard.png"))},
            "Trident":{"damage": 19,"speed":3,"range":4,"effect":False,"sharpness":6,"knockback":8,"tag":"A weaker spear light enough to be held with a shield","level":3,"sprite":pygame.image.load(path.join("Sprites","Trident.png"))},
            "Scythe":{"damage": 17,"speed":5,"range":5,"effect":False,"sharpness":6,"knockback":10,"tag":"A heavy slashing weapon with immense power.","level":2,"sprite":pygame.image.load(path.join("Sprites","Scythe.png"))},
            "Reaper":{"damage": 30,"speed":6,"range":6,"effect":False,"sharpness":11,"knockback":11,"tag":"A dark aura eminates from this dark weapon.","level":3,"sprite":pygame.image.load(path.join("Sprites","Reaper.png"))},
        },
        "Sword":{
            "Knife":{"damage": 3,"speed":1,"range":1,"effect":False,"sharpness":3,"knockback":2,"tag":"This small, quick weapon is hated by vegetables everywhere.","level":1,"sprite":pygame.image.load(path.join("Sprites","Knife.png"))},
            "Short Sword":{"damage": 9,"speed":3,"range":2,"effect":False,"sharpness":6,"knockback":4,"tag":"A short, double edged sword,what more do you want? A laser?","level":2,"sprite":pygame.image.load(path.join("Sprites","Short_Sword.png"))},
            "Long Sword":{"damage": 24,"speed":4,"range":3,"effect":False,"sharpness":8,"knockback":6,"tag":"A forged steel sword with enough power to cut through rock.","level":2,"sprite":pygame.image.load(path.join("Sprites","Long_Sword.png"))},
            "Fire Sword":{"damage": 18,"speed":3,"range":2,"effect":{"id":0,"effectChance":(1/8),"duration":2},"sharpness":7,"knockback":9,"tag":"It's a short sword that's on fire...Don't ask how it works,just kill stuff.","level":3,"sprite":pygame.image.load(path.join("Sprites","Fire_Sword.png"))},
            "Heavy Broadsword":{"damage": 26,"speed":5,"range":3,"effect":{"id":1,"effectChance": 1/6,"duration":3},"sharpness":13,"knockback":14,"tag":"A powerful sword that can break shields.","level":3,"sprite":pygame.image.load(path.join("Sprites","Heavy_Broadsword.png"))},
            "Dual Bladed Sword":{"damage":28,"speed":4,"range":3,"effect":False,"sharpness":10,"knockback":11,"tag":"A long sword, with another long sword on the back.","level":3,"sprite":pygame.image.load(path.join("Sprites","Dual_Bladed_Sword.png"))},
            "Energy Sword":{"damage": 23,"speed":3,"range":3,"effect":{"id":0,"effectChance":(1/7),"duration":2},"sharpness":12,"knockback":11,"tag":"Kind of a laser...","level":4,"sprite":pygame.image.load(path.join("Sprites","Energy_Sword.png"))},
        },
        "Hammer":{
            "Hammer":{"damage":7,"speed":4,"range":3,"effect":False,"sharpness":1,"knockback":3,"tag":"A single-handed hammer with power to spare.","level":1,"sprite":pygame.image.load(path.join("Sprites","Hammer.png"))},
            "Axe":{"damage":14,"speed":3,"range":2,"effect":False,"sharpness":5,"knockback":9,"tag":"Quite useful for chopping wood...","level":2,"sprite":pygame.image.load(path.join("Sprites","Axe.png"))},
            "Mace":{"damage":17,"speed":4,"range":3,"effect":False,"sharpness":5,"knockback":12,"tag":"They say, if you go high up into the mountains, you can still hear the screams of the last person hit with this weapon.","level":2,"sprite":pygame.image.load(path.join("Sprites","Mace.png"))},
            "Facial Reconstructor":{"damage":16,"speed":4,"range":3,"effect":False,"sharpness":5,"knockback":10,"tag":"Hammer Time!","sprite":pygame.image.load(path.join("Sprites","Facial_Reconstructor.png"))},
            "War Axe":{"damage":20,"speed":3,"range":4,"effect":False,"sharpness":10,"knockback":13,"tag":"This powerful axe is quite popular with warlocks.","level":3,"sprite":pygame.image.load(path.join("Sprites","War_Axe.png"))},
            "Mjolnir":{"damage":23,"speed":4,"range":2,"effect":{"id":2,"effectChance":1/8,"duration":3},"sharpness":6,"knockback":13,"tag":"The mighty and powerful hammer once wielded by the god of thunder himself, Thor.","level":3,"sprite":pygame.image.load(path.join("Sprites","Mjolnir.png"))},
            "Flail":{"damage":25,"speed":4,"range":4,"effect":False,"sharpness":7,"knockback":16,"tag":"A weapon so powerful, it destroys concrete like sheets of glass.","level":3,"sprite":pygame.image.load(path.join("Sprites","Flail.png"))},
        }
    },"Ranged":{
        "Null":{"damage":1,"speed":1,"effect":False,"sharpness":1,"knockback":1,"velocity":1,"tag":"You have yet to obtain a ranged weapon...","level":0,"sprite":pygame.image.load(path.join("Sprites","Null.png"))},
        "Bow":{
            "Bow":{"damage":4,"speed":2,"effect":False,"sharpness":3,"knockback":1,"velocity":5,"tag":"Legolas engaged.","level":1,"sprite":pygame.image.load(path.join("Sprites","Bow.png"))},
            "Long Bow":{"damage":11,"speed":3,"effect":False,"sharpness":7,"knockback":4,"velocity":8,"tag":"A bow with a longer string and much more firing power","level":2,"sprite":pygame.image.load(path.join("Sprites","Long_Bow.png"))},
            "Crossbow":{"damage":15,"speed":4,"effect":False,"sharpness":8,"knockback":6,"velocity":11,"tag":"The silent but deadly killer.... I heard that giggle.","level":2,"sprite":pygame.image.load(path.join("Sprites","Crossbow.png"))},
            "Multi Bow":{"damage":16,"speed":4,"effect":False,"sharpness":8,"knockback":7,"velocity":12,"tag":"An upgraded crossbow with capacity for multiple arrows to be fired at once.","level":3,"sprite":pygame.image.load(path.join("Sprites","Multi_Bow.png"))},
            "Angel Bow":{"damage":23,"speed":3,"effect":False,"sharpness":11,"knockback":7,"velocity":9,"tag":"A bow that once belonged to Valkyre, it eminates an aura of light.","level":3,"sprite":pygame.image.load(path.join("Sprites","Angel_Bow.png"))},
            "Toxic Bow":{"damage":19,"speed":3,"effect":{"id":5,"effectChance":1/7,"duration":4},"sharpness":9,"knockback":8,"velocity":9,"tag":"This bow fires arrows with a toxic venom infused into it.","level":3,"sprite":pygame.image.load(path.join("Sprites","Toxic_Bow.png"))},
        },
        "Gun":{
            "Musket":{"damage":3,"speed":3,"effect":False,"sharpness":2,"knockback":3,"velocity":11,"tag":"..... It's just there....","level":1,"sprite":pygame.image.load(path.join("Sprites","Musket.png"))},
            "Rifle":{"damage":8,"speed":3,"effect":False,"sharpness":5,"knockback":5,"velocity":15,"tag":"A standard rifle, it can shoot through a brick wall.","level":2,"sprite":pygame.image.load(path.join("Sprites","Rifle.png"))},
            "Mini Cannon":{"damage":17,"speed":6,"effect":{"id":1,"effectChance":1/6,"duration":8},"sharpness":3,"knockback":7,"velocity":11,"tag":"Yes,there will be a large cannon.","level":2,"sprite":pygame.image.load(path.join("Sprites","Mini_Cannon.png"))},
            "Cannon":{"damage":31,"speed":7,"effect":{"id":1,"effectChance":1/5,"duration":8},"sharpness":4,"knockback":15,"velocity":13,"tag":"This is known throughout the lands as\"MINTA!\" or OUCH!","level":3,"sprite":pygame.image.load(path.join("Sprites","Cannon.png"))},
            "Sniper Rifle":{"damage":24,"speed":5,"effect":False,"sharpness":7,"knockback":9,"velocity":26,"tag":"The shots from this high powered rifle can break the sound barrier.","level":3,"sprite":pygame.image.load(path.join("Sprites","Sniper_Rifle.png"))},
            "Machine Gun":{"damage":12,"speed":1,"effect":False,"sharpness":5,"knockback":3,"velocity":19,"tag":"Because who needs accuracy when you can fire 30 shots per second?","level":3,"sprite":pygame.image.load(path.join("Sprites","Machine_Gun.png"))},
            },
        "Magic":{
            "Fireball":{"damage":2,"speed":3,"effect":{"id":0,"effectChance":1/3,"duration":5},"sharpness":1,"knockback":4,"velocity":3,"tag":"A weak mage staff capable of shooting small fireballs.","level":1,"sprite":pygame.image.load(path.join("Sprites","Fireball.png"))},
            "Snowball":{"damage":6,"speed":4,"effect":{"id":8,"effectChance":1/6,"duration":10},"sharpness":4,"knockback":6,"velocity":7,"tag":"A staff the has frozen entire lakes with it's incredible power","level":2,"sprite":pygame.image.load(path.join("Sprites","Snowball.png"))},
            "Flame Staff":{"damage":11,"speed":3,"effect":{"id":0,"effectChance":1/4,"duration":5},"sharpness":3,"knockback":7,"velocity":9,"tag":"Cooks enemies and marshmallows!","level":2,"sprite":pygame.image.load(path.join("Sprites","Flame_Staff.png"))},
        }
    }
}
Shields={
    "Null":{"block":0,"resistance":0,"damage":0,"tag":pygame.image.load(path.join("Sprites","Null.png")),}
}
Accesories={
    "Rings":{
    }
}
